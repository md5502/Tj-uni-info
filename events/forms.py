from django import forms

from .models import EventUser


class EventUserRegistration(forms.ModelForm):
    class Meta:
        model = EventUser
        fields = ["name", "fname", "phone_number", "email"]
        labels = {
            "name": "نام",
            "fname": "نام خانوادگی",
            "phone_number": "شماره تماس",
            "email": "ایمیل",
        }
