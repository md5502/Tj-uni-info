from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from .models import Professor, Staff


def get_professor_list() -> QuerySet:
    return Professor.objects.all()


def get_professor_via_slug(slug) -> QuerySet:
    return get_object_or_404(Professor, slug=slug)


def get_staff_list() -> QuerySet:
    return Staff.objects.all()

def get_staff_via_slug(slug):
    return get_object_or_404(Staff, slug =slug)
