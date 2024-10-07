from django.shortcuts import get_object_or_404, render

from .models import Event, EventImage


def events_list(request):
    events = Event.objects.all()
    context = {
        "events": [],
    }
    for i in events:
        first_image = EventImage.objects.filter(event=i).first().image
        event = {
            "title": i.title,
            "date": i.schedule_date,
            "image": first_image,
            "slug": i.slug,
        }
        context["events"].append(event)

    return render(request, "events/events_list.html", context)


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    event_images = EventImage.objects.filter(event=event)
    extra_images = [i.image for i in event_images[1:]]

    context = {"event": event, "main_image": event_images[0].image, "extra_images": extra_images}

    return render(
        request,
        "events/event_detail.html",
        context,
    )
