from django.shortcuts import render

from .selectors import get_association_via_slug
from .services import build_association_context


def association_list(request):
    context = build_association_context(request)
    return render(request, "associations/list.html", context)


def association_detail(request, slug):
    association = get_association_via_slug(slug)
    context = {"association": association}
    return render(request, "associations/detail.html", context)
