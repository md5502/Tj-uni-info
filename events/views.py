from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.timezone import now

from .forms import EventUserRegistration
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
    form = EventUserRegistration()
    event = get_event_with_given_slug(slug)
    current_date = now()

    if event.register_deadline < current_date:
        messages.error(request, "مهلت ثبت‌نام تمام شده است")
        return redirect("events:event_detail", slug=slug)

    # Check if the event is full
    if event.capacity == 0:
        messages.error(request, "ظرفیت تمام شده است")
        return redirect("events:event_detail", slug=slug)

    event_title = event.title
    event_date = event.schedule_date
    event_location = event.location

    if request.method == "POST":
        form = EventUserRegistration(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            already_user = is_user_registered_in_event(event, email)

            if already_user:
                messages.error(request, "شما قبلا در این رخداد ثبت‌نام کرده‌اید")
                return redirect("events:event_detail", slug=slug)

            event_user = form.save(commit=False)
            event_user.event = event
            event_user.save()

            # Decrease the event's capacity by 1
            event.capacity -= 1
            event.save()

            full_name = form.cleaned_data["name"] + " " + form.cleaned_data["fname"]
            send_registration_email(
                user_email=email,
                name=full_name,
                event_title=event_title,
                event_date=event_date,
                event_location=event_location,
                event_url=request.build_absolute_uri(reverse("events:event_detail", kwargs={"slug": event.slug})),
            )

            messages.success(request, "شما با موفقیت ثبت‌نام شده‌اید")
            return redirect("events:event_detail", slug=slug)

    return render(
        request,
        "events/event_registration.html",
        {
            "event_date": event_date,
            "event_title": event_title,
            "event_location": event_location,
            "form": form,
        },
    )
