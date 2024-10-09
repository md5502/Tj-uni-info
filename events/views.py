import jdatetime
import markdown
from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.dateparse import parse_date

from .forms import EventUserRegistration
from .models import Event, EventImage, EventUser


def events_list(request):
    events = Event.objects.all()
    context = {
        "events": [],
    }

    date = request.GET.get("date")
    search_query = request.GET.get("search")

    if date:
        date = parse_date(date)
        events = events.filter(schedule_date=date)

    if search_query:
        events = events.filter(Q(title__icontains=search_query))

    for i in events:
        first_image = EventImage.objects.filter(event=i).first()
        if first_image:
            first_image = first_image.image
        event_date = jdatetime.datetime.fromgregorian(date=i.schedule_date).strftime("%Y/%m/%d")

        event = {
            "title": i.title,
            "date": event_date,
            "image": first_image,
            "location": i.location,  # Add location field
            "slug": i.slug,
        }
        context["events"].append(event)

    return render(request, "events/events_list.html", context)


def event_detail(request, slug):
    context = {}

    event = get_object_or_404(Event, slug=slug)
    event_images = EventImage.objects.filter(event=event)
    if event_images:
        context["main_image"] = event_images[0].image
        extra_images = [i.image for i in event_images[1:]]
        context["extra_images"] = extra_images
    event_description_html = markdown.markdown(event.description)

    context["event"] = event
    event_date = jdatetime.datetime.fromgregorian(date=event.schedule_date).strftime("%Y/%m/%d")
    context["event_date"] = event_date
    context["location"] = event.location
    context["event_description_html"] = event_description_html

    return render(
        request,
        "events/event_detail.html",
        context,
    )


def event_registration(request, slug):
    form = EventUserRegistration()
    event = get_object_or_404(Event, slug=slug)
    event_title = event.title
    event_date = jdatetime.datetime.fromgregorian(date=event.schedule_date).strftime("%Y/%m/%d")
    event_location = event.location  # Add location field

    if request.method == "POST":
        form = EventUserRegistration(request.POST)
        if form.is_valid():

            event_user = form.save(commit=False)
            email = form.cleaned_data["email"]
            already_user = EventUser.objects.filter(event=event, email=email)
            if already_user:
                messages.success(request, "شما قبلا در این رخداد ثبت‌نام کرده‌اید")
                return redirect("events:event_detail", slug)

            event_user.event = event
            event_user.save()
            name = form.cleaned_data["name"] + " " + form.cleaned_data["fname"]
            send_registration_email(
                user_email=email,
                name=name,
                event_title=event_title,
                event_date=event_date,
                event_location=event_location,  # Add location in the email
                event_url=request.build_absolute_uri(reverse("events:event_detail", kwargs={"slug": event.slug})),
            )

            messages.success(request, "شما با موفقیت ثبت‌نام شده‌اید")
            return redirect("events:events_list")
    return render(
        request, "events/event_registration.html",
        {
            "event_date": event_date,
            "event_title": event_title,
            "event_location": event_location,  # Pass location to the template
            "form": form,
        },
    )


def send_registration_email(user_email, name, event_title, event_date, event_location, event_url):
    # Render the HTML email template
    subject = "تأیید ثبت‌نام در رخداد"
    message = render_to_string(
        "emails/event_registration.html",
        {
            "first_name": name,
            "event_title": event_title,
            "event_date": event_date,
            "event_location": event_location,  # Include location in the email
            "event_url": event_url,
        },
    )
    email = EmailMessage(subject, message, to=[user_email])
    email.content_subtype = "html"  # Set the email to HTML format
    email.send()
