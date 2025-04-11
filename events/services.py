import markdown

from .selectors import get_event_main_image, get_extra_images


def build_events_list_context(events):
    context = {
        "events": [],
    }

    for event in events:
        event_main_image = get_event_main_image(event) or "default_image.png"

        # اطمینان از اینکه schedule_date مقدار دارد
        if event.schedule_date:
            event_date = event.schedule_date
        else:
            event_date = "تاریخ نامشخص"

        # افزودن اطلاعات رویداد به لیست
        context["events"].append(
            {
                "title": event.title,
                "date": event_date,
                "image": event_main_image,
                "slug": event.slug,
            },
        )

    return context



def build_event_context(event):

    context = {}
    is_registration_open = event.capacity > 0 and event.register_deadline >= timezone.now().date()
    # Populate the context with event details
    context["main_image"] = get_event_main_image(event)
    context["extra_images"] = get_extra_images(event)
    context["event_title"] = event.title
    context["event_slug"] = event.slug
    context["event_date"] = event.schedule_date
    context["event_register_deadline"] = event.register_deadline
    context["location"] = event.location
    context["capacity"] = event.capacity
    context["is_registration_open"] = is_registration_open

    # Convert markdown description to HTML
    context["event_description_html"] = markdown.markdown(event.description)

    return context

from django.utils import timezone
