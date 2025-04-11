import markdown
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from events.models import Event

from .models import Association


def get_association_list(request) -> QuerySet:
    search_query = request.GET.get("q")
    if search_query:
        return Association.filter(Q(name__icontains=search_query))

    return Association.objects.all()


def get_association_via_slug(slug: str):
    """ دریافت انجمن و رخدادهای مرتبط از طریق `slug` و تفکیک رخدادها بر اساس زمان """
    association = get_object_or_404(Association, slug=slug)

    association_content_type = ContentType.objects.get_for_model(Association)

    all_events = Event.objects.filter(content_type=association_content_type, object_id=association.id)
    upcoming_events = all_events.filter(schedule_date__gte=now()).order_by("schedule_date")
    past_events = all_events.filter(schedule_date__lt=now()).order_by("-schedule_date")


    if association.goals:
        md = markdown.Markdown(extensions=["fenced_code"])
        association.goals = md.convert(association.goals)


    return association, upcoming_events, past_events
