from django.shortcuts import render

from .selectors import get_association_list, get_association_via_slug
from .services import build_association_context


def association_list(request):
    associations = get_association_list(request)
    context = build_association_context(associations)
    return render(request, "associations/list.html", context)


def association_detail(request, slug):
    association, upcoming_events, past_events = get_association_via_slug(slug)
    context = {"association": association, "upcoming_events": upcoming_events, "past_events": past_events}
    return render(request, "associations/detail.html", context)
