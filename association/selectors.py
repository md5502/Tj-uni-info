from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404

from .models import Association


def get_association_list(request) -> QuerySet:
    search_query = request.GET.get("search")
    if search_query:
        return Association.filter(Q(name__icontains=search_query))

    return Association.objects.all()


def get_association_via_slug(slug) -> QuerySet:
    return get_object_or_404(Association, slug=slug)
