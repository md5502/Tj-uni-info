from django import forms

from .models import EventUser


class EventUserRegistration(forms.ModelForm):
    class Meta:
        model = EventUser
        fields = ["name", "fname", "phone_number", "student_number", "branch", "email"]
        labels = {
            "name": "نام",
            "fname": "نام خانوادگی",
            "phone_number": "شماره تماس",
            "student_number": "شماره دانشجویی",
            "branch": "رشته تحصیلی",
            "email": "ایمیل",
        }
