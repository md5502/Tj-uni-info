from django.urls import path

from .views import events_list

app_name = "evetns"

urlpatterns = [
    path("", events_list, name="events_list"),
]
