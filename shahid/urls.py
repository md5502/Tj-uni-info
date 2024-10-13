from django.urls import path

from .views import download_shahid_images, generate_qr_code, shahid_detail, shahid_list

app_name = "shahid"

urlpatterns = [
    path("", shahid_list, name="shahid_list"),
    path("<str:slug>/", shahid_detail, name="shahid_detail"),
    path("<str:slug>/qr/", generate_qr_code, name="generate_qr_code"),
    path("shahid/<str:slug>/images/download/", download_shahid_images, name="download_shahid_images"),
]
