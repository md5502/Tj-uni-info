import uuid

from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import path
from django.utils.text import slugify
from django_jalali.admin.widgets import AdminjDateWidget, AdminSplitjDateTime
from django_jalali.db import models as jmodels  # Import jalali models

from events.utils import generate_csv_response

from .models import Event, EventImage, EventUser


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    exclude = ("slug",)

    actions = ["registered_users"]

    # Display fields in list view
    list_display = ["title", "location", "schedule_date", "created_at", "capacity"]
    list_filter = ["location", "schedule_date"]
    search_fields = ["title", "location"]

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
