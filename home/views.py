from django.shortcuts import render

from association.models import Association
from events.models import Event
from events.selectors import get_event_main_image
from professor_staff.models import Professor, Staff
from shahid.models import Shahid


def home(request):
    top_events = Event.objects.order_by("-schedule_date")[:4]

    events = []
    for event in top_events:
        events.append({
            "title": event.title,
            "schedule_date": event.schedule_date,
            "description": event.description,
            "image": get_event_main_image(event),
            "slug": event.slug,
        })

    main_event = events[0]

    professors = Professor.objects.order_by("-created_at")[:4]
    staffs = Staff.objects.order_by("-created_at")[:4]
    associations = Association.objects.order_by("-created_at")[:2]
    shahids = Shahid.objects.order_by("-created_at")[:4]

    return render(request, "home/home.html", {
        "events": events,
        "main_event": main_event,
        "professors": professors,
        "staffs": staffs,
        "associations": associations,
        "shahids": shahids,
    })
