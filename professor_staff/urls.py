from django.urls import path

from config.views import generate_qr_code

from .views import professor_detail, professor_list, staff_detail, staff_list

app_name = "professors_staffs"

urlpatterns = [
    path("professors/", professor_list, name="professor_list"),
    path("professors/<str:slug>", professor_detail, name="professor_detail"),
    path("professors/<str:slug>/qr/", generate_qr_code, name="generate_qr_code"),

    path("staffs/", staff_list, name="staff_list"),
    path("staffs/<str:slug>", staff_detail, name="staff_detail"),
    path("staffs/<str:slug>/qr/", generate_qr_code, name="generate_qr_code"),

]
