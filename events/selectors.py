import jdatetime
from django.shortcuts import get_object_or_404

from .models import Event, EventImage, EventUser


def get_event_list():
    """Retrieve a list of all events.

    Returns:
        QuerySet: A queryset containing all events.
    """
    return Event.objects.all()


def get_event_images(event):
    """Retrieve all images related to a specific event.

    Args:
        event (Event): The event object for which images are to be retrieved.

    Returns:
        QuerySet or None: A queryset containing the images if available, otherwise None.
    """
    images = EventImage.objects.filter(event=event)
    if images:
        return images
    return None


def get_event_main_image(event):
    """Retrieve the main (first) image of a specific event.

    Args:
        event (Event): The event object for which the main image is to be retrieved.

    Returns:
        ImageField or None: The first image related to the event if available, otherwise None.
    """
    image = get_event_images(event)
    if image:
        return image.first().image
    return None


def get_extra_images(event):
    """Retrieve all extra images (excluding the first one) related to a specific event.

    Args:
        event (Event): The event object for which extra images are to be retrieved.

    Returns:
        list or None: A list of extra images (ImageField) if available, otherwise None.
    """
    extra_images = get_event_images(event)
    if extra_images:
        return [image.image for image in extra_images[1:]]
    return None


def get_event_with_given_slug(slug):
    """Retrieve an event by its slug and format its schedule date to the Jalali calendar.

    Args:
        slug (str): The slug of the event.

    Returns:
        Event: The event object with its date formatted in the Jalali calendar.

    Raises:
        Http404: If the event with the given slug does not exist.
    """
    event = get_object_or_404(Event, slug=slug)
    event.schedule_date = jdatetime.datetime.fromgregorian(date=event.schedule_date).strftime("%Y/%m/%d")
    return event


def is_user_registered_in_event(event, email):
    """Check if a user with a specific email is already registered for an event.

    Args:
        event (Event): The event object.
        email (str): The email address of the user.

    Returns:
        bool: True if the user is registered, otherwise False.
    """
    user = EventUser.objects.filter(event=event, email=email)
    return bool(user)
