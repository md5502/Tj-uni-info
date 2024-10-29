import jdatetime
import markdown

from .selectors import get_event_main_image, get_extra_images


def build_events_list_context(events):

    context = {
        "events": [],
    }



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


def build_event_context(event):

    context = {}



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
