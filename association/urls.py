from django.urls import path

from .views import association_detail, association_list

app_name = "association"

urlpatterns = [
    path("", association_list, name="association_list" ),
    path("<str:slug>/", association_detail, name="association_detail" ),
]
