from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import EventUserRegistration
from .selectors import get_event_with_given_slug, is_user_registered_in_event
from .services import build_event_context, build_events_list_context
from .utils import send_registration_email


def events_list(request):
    context = build_events_list_context(request)
    return render(request, "events/events_list.html", context)


def event_detail(request, slug):
    context = build_event_context(slug)
    return render(
        request,
        "events/event_detail.html",
        context,
    )


def event_registration(request, slug):
    form = EventUserRegistration()
    event = get_event_with_given_slug(slug)
    event_title = event.title
    event_date = event.schedule_date
    event_location = event.location

    if request.method == "POST":
        form = EventUserRegistration(request.POST)
        if form.is_valid():
            event_user = form.save(commit=False)
            email = form.cleaned_data["email"]
            already_user = is_user_registered_in_event(event, email)
            if already_user:
                messages.success(request, "شما قبلا در این رخداد ثبت‌نام کرده‌اید")
                return redirect("events:event_detail", slug)

            event_user.event = event
            event_user.save()
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
            return redirect("events:events_list")

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
