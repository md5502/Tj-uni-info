from django.urls import path

from .views import professor_detail, professor_list

app_name = "professors_staffs"

urlpatterns = [
    path("professors/", professor_list, name="professor_list"),
    path("professors/<str:slug>", professor_detail, name="professor_detail"),
]
