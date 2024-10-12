import jdatetime
import markdown
from django.db.models import Q

from .selectors import get_event_list, get_event_main_image, get_event_with_given_slug, get_extra_images


def build_events_list_context(request):
    """Build the context for listing all events, optionally filtered by a search query.

    Args:
        request (HttpRequest): The HTTP request object, potentially containing a search query in the GET parameters.

    Returns:
        dict: A dictionary containing the context with a list of
            events, each including title, date, image, location, and slug.
    """
    context = {
        "events": [],
    }

    events = get_event_list()

    # Check for search query and filter events
    search_query = request.GET.get("search")
    if search_query:
        events = events.filter(Q(title__icontains=search_query))

    # Build event details for each event
    for event in events:
        event_main_image = get_event_main_image(event)
        event_date = jdatetime.datetime.fromgregorian(date=event.schedule_date).strftime("%Y/%m/%d")

        # Append event details to the context
        context["events"].append(
            {
                "title": event.title,
                "date": event_date,
                "image": event_main_image,
                "location": event.location,
                "slug": event.slug,
            },
        )

    return context


def build_event_context(slug):
    """Build the context for a detailed view of a specific event identified by its slug.

    Args:
        slug (str): The slug of the event to be retrieved.

    Returns:
        dict: A dictionary containing event details such as
             title, slug, date, location, main image, extra images, and description in HTML.
    """
    context = {}

    event = get_event_with_given_slug(slug)

    # Populate the context with event details
    context["main_image"] = get_event_main_image(event)
    context["extra_images"] = get_extra_images(event)
    context["event_title"] = event.title
    context["event_slug"] = event.slug
    context["event_date"] = event.schedule_date
    context["event_register_deadline"] = event.register_deadline
    context["location"] = event.location
    context["capacity"] = event.capacity

    # Convert markdown description to HTML
    context["event_description_html"] = markdown.markdown(event.description)

    return context
