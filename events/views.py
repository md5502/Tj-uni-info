from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.timezone import now

from .forms import EventUserRegistration
from .models import Event
from .selectors import get_event_list, get_event_with_given_slug, is_user_registered_in_event
from .services import build_event_context, build_events_list_context
from .utils import send_registration_email


def events_list(request):
    events = get_event_list(request)
    context = build_events_list_context(events)
    return render(request, "events/events_list.html", context)


def event_detail(request, slug):
    event = get_event_with_given_slug(slug)
    context = build_event_context(event)
    return render(
        request,
        "events/event_detail.html",
        context,
    )

def event_registration(request, slug):
    event = get_event_with_given_slug(slug)
    current_date = now()

    # بررسی مهلت ثبت‌نام
    if event.register_deadline < current_date:
        messages.error(request, "مهلت ثبت‌نام تمام شده است")
        return redirect("events:event_detail", slug=slug)

    # بررسی ظرفیت رخداد
    if event.capacity <= 0:
        messages.error(request, "ظرفیت این رخداد تکمیل شده است")
        return redirect("events:event_detail", slug=slug)

    form = EventUserRegistration()

    if request.method == "POST":
        form = EventUserRegistration(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]

            # بررسی اینکه کاربر قبلاً در این رخداد ثبت‌نام نکرده باشد
            if is_user_registered_in_event(event=event, email=email):
                messages.error(request, "شما قبلاً در این رخداد ثبت‌نام کرده‌اید")
                return redirect("events:event_detail", slug=slug)

            with transaction.atomic():
                # قفل کردن رکورد برای جلوگیری از Race Condition
                event = Event.objects.select_for_update().get(pk=event.pk)

                # بررسی مجدد ظرفیت، چون ممکن است همزمان چند نفر ثبت‌نام کنند.
                if event.capacity <= 0:
                    messages.error(request, "ظرفیت این رخداد تکمیل شده است")
                    return redirect("events:event_detail", slug=slug)

                # ثبت اطلاعات شرکت‌کننده
                event_user = form.save(commit=False)
                event_user.event = event
                event_user.save()

                # کاهش ظرفیت
                event.capacity -= 1
                event.save()

            # ارسال ایمیل تأیید ثبت‌نام
            full_name = f"{form.cleaned_data['name']} {form.cleaned_data['fname']}"
            send_registration_email(
                user_email=email,
                name=full_name,
                event_title=event.title,
                event_date=event.schedule_date,
                event_location=event.location,
                event_url=request.build_absolute_uri(
                    reverse("events:event_detail", kwargs={"slug": event.slug}),
                ),
            )

            messages.success(request, "شما با موفقیت ثبت‌نام شده‌اید")
            return redirect("events:event_detail", slug=slug)

    return render(
        request,
        "events/event_registration.html",
        {
            "event": event,
            "form": form,
        },
    )

