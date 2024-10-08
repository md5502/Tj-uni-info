from django.urls import path

from .views import event_detail, event_registration, events_list

app_name = "events"

urlpatterns = [
    path("", events_list, name="events_list"),
    path("<str:slug>/", event_detail, name="event_detail"),
    path("register/<str:slug>/", event_registration, name="event_registration"),
]
