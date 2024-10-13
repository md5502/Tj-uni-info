from django.shortcuts import get_object_or_404

from .models import Shahid


def get_shahid_list():
    return Shahid.objects.all()


def get_shahid_via_slug(slug):
    return get_object_or_404(Shahid, slug=slug)
