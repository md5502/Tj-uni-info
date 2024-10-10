from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from .models import Professor


def get_professor_list() -> QuerySet :
    return Professor.objects.all()

def get_professor_via_slug(slug):
    return get_object_or_404(Professor, slug=slug)
