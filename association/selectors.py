from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from .models import Association


def get_association_list() -> QuerySet:
    return Association.objects.all()


def get_association_via_slug(slug) -> QuerySet:
    return get_object_or_404(Association, slug=slug)
