from django.urls import path

from config.views import generate_qr_code

from .views import association_detail, association_list

app_name = "association"

urlpatterns = [
    path("", association_list, name="association_list" ),
    path("<str:slug>/", association_detail, name="association_detail" ),
    path("<str:slug>/qr/", generate_qr_code, name="generate_qr_code"),
]
