from django.urls import path

from .views import professor_detail, professor_list, staff_detail, staff_list

app_name = "professors_staffs"

urlpatterns = [
    path("professors/", professor_list, name="professor_list"),
    path("professors/<str:slug>", professor_detail, name="professor_detail"),
    path("staffs/", staff_list, name="staff_list"),
    path("staffs/<str:slug>", staff_detail, name="staff_detail"),

]
