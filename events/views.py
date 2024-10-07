from django.shortcuts import render

from .models import Event


def events_list(request):
    events = Event.objects.all()

    return render(request, "events/list.html", {"events":events})
