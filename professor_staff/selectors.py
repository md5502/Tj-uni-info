from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404

from .models import Professor, Staff


def get_professor_list(request) -> QuerySet:
    search_query = request.GET.get("q", "")
    if search_query:
        return Professor.objects.filter(Q(name__icontains=search_query) | Q(fname__icontains=search_query))
    return Professor.objects.all()


def get_professor_via_slug(slug) -> QuerySet:
    return get_object_or_404(Professor, slug=slug)


def get_staff_list(request) -> QuerySet:
    search_query = request.GET.get("q", "")
    if search_query:
        return Staff.objects.filter(Q(name__icontains=search_query) | Q(fname__icontains=search_query))
    return Staff.objects.all()


def get_staff_via_slug(slug):
    return get_object_or_404(Staff, slug=slug)
