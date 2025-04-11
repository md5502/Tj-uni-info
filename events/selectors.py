from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Event, EventImage, EventUser


def get_event_list(request):

    search_query = request.GET.get("q", "")
    if search_query:
        return Event.objects.filter(Q(title__icontains=search_query))

    return Event.objects.all()


def get_event_images(event):

    images = EventImage.objects.filter(event=event)
    if images:
        return images
    return None


def get_event_main_image(event):

    images = get_event_images(event)
    if images:
        return images.first().image
    return None


def get_extra_images(event):

    extra_images = get_event_images(event)
    if extra_images:
        return [image.image for image in extra_images[1:]]
    return None


def get_event_with_given_slug(slug):
    return get_object_or_404(Event, slug=slug)


def is_user_registered_in_event(event, email):

    user = EventUser.objects.filter(event=event, email=email)
    return bool(user)
