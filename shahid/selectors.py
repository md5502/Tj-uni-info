from django.db.models import Q
from django.shortcuts import get_object_or_404

from .models import Shahid


def get_shahid_list(request):
    search_query = request.GET.get("search")
    if search_query:
        return Shahid.filter(Q(first_name__icontains=search_query))
    return Shahid.objects.all()


def get_shahid_via_slug(slug):
    return get_object_or_404(Shahid, slug=slug)
