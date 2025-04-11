import re

from django import forms
from django.core.exceptions import ValidationError

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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        event = self.instance.event if self.instance.pk else self.initial.get("event")

        # بررسی فرمت ایمیل
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            raise ValidationError("فرمت ایمیل معتبر نیست.")

        # بررسی عدم تکراری بودن ایمیل برای یک رخداد
        if EventUser.objects.filter(email=email, event=event).exists():
            raise ValidationError("این ایمیل قبلاً برای این رخداد ثبت شده است.")

        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        if phone_number:
            if not re.match(r"^\d{10,15}$", phone_number):
                raise ValidationError("شماره تلفن باید فقط شامل اعداد و بین ۱۰ تا ۱۵ رقم باشد.")

        return phone_number

    def clean_student_number(self):
        student_number = self.cleaned_data.get("student_number")

        if student_number:
            if not re.match(r"^\d{10}$", student_number):
                raise ValidationError("شماره دانشجویی باید دقیقاً ۱۰ رقم باشد.")

        return student_number
