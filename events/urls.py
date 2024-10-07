from django.urls import path

from .views import events_list, event_detail

app_name = "events"

urlpatterns = [
    path("", events_list, name="events_list"),
    path("<str:slug>/", event_detail, name="event_detail"),
]
