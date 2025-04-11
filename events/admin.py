import uuid

from django import forms
from django.contrib import admin, messages
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.urls import path
from django.utils.text import slugify
from django_jalali.admin.widgets import AdminjDateWidget, AdminSplitjDateTime
from django_jalali.db import models as jmodels  # Import jalali models

from association.models import Association
from events.utils import generate_csv_response
from professor_staff.models import Professor, Staff

from .models import Event, EventImage, EventUser


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1



class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # مقدار اولیه `content_type` را دریافت می‌کنیم
        content_type = self.instance.content_type if self.instance.pk else None

        # اگر مقدار `content_type` مشخص باشد، `object_id` را بر اساس آن تنظیم می‌کنیم
        if content_type:
            model_class = content_type.model_class()
            if model_class:
                self.fields["object_id"].queryset = model_class.objects.all()



class EventAdmin(admin.ModelAdmin):

    form = EventAdminForm

    inlines = [EventImageInline]
    exclude = ("slug",)

    actions = ["registered_users"]

    # Display fields in list view
    list_display = ("title", "schedule_date", "location", "capacity", "organizer_display")
    list_filter = ("schedule_date", "created_at")
    search_fields = ("title", "description", "location")
    ordering = ("-schedule_date",)

    # Specify form field overrides
    formfield_overrides = {
        jmodels.jDateTimeField: {"widget": AdminSplitjDateTime},
        jmodels.jDateField: {"widget": AdminjDateWidget},
    }

    @admin.action(description="دانلود لیست افرادی که در این رخداد ثبت‌نام کرده اند")
    def registered_users(self, request, queryset):
        # Get event IDs and pass them as a parameter in the redirect
        event_ids = queryset.values_list("id", flat=True)
        return redirect(f"download-registered-users/{','.join(map(str, event_ids))}")

    def save_model(self, request, obj, form, change):
        # Generate slug only if it's not provided
        if not obj.slug:
            obj.slug = slugify(
                f"{str(uuid.uuid4()).split('-')[0]} {obj.title}",
                allow_unicode=True,
            )
        super().save_model(request, obj, form, change)

    # Define custom admin URL
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "download-registered-users/<str:event_ids>/",
                self.admin_site.admin_view(self.download_registered_users),
                name="download-registered-users",
            ),
        ]
        return custom_urls + urls

    # Custom view to handle CSV download
    def download_registered_users(self, request, event_ids):
        event_ids = event_ids.split(",")
        events = self.model.objects.filter(id__in=event_ids)
        messages.success(request, "لیست در حال دانلود است")
        return generate_csv_response(events)

    def organizer_display(self, obj):
        """ نمایش نام برگزارکننده در لیست پنل ادمین """
        if obj.organizer:
            return f"{obj.organizer}"
        return "نامشخص"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "content_type":
            allowed_models = [Professor, Staff, Association]
            kwargs["queryset"] = ContentType.objects.filter(model__in=[m._meta.model_name for m in allowed_models])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    organizer_display.short_description = "برگزارکننده"


class EventImageAdmin(admin.ModelAdmin):
    list_display = ["event", "image"]
    list_filter = ["event"]
    search_fields = ["event__title"]


class EventUserAdmin(admin.ModelAdmin):
    list_display = ["name", "fname", "email", "phone_number", "event", "created_at"]
    list_filter = ["event"]
    search_fields = ["name", "fname", "email", "phone_number"]


admin.site.register(Event, EventAdmin)
admin.site.register(EventImage, EventImageAdmin)
admin.site.register(EventUser, EventUserAdmin)
