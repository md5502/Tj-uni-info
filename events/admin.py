import uuid

from django.contrib import admin
from django.utils.text import slugify

from .models import Event, EventImage, EventUser


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    exclude = ("slug",)

    # Display fields in list view
    list_display = ["title", "location", "schedule_date", "created_at"]
    list_filter = ["location", "schedule_date"]
    search_fields = ["title", "location"]

    def save_model(self, request, obj, form, change):
        # Generate slug only if it's not provided
        if not obj.slug:
            obj.slug = slugify(
                f"{str(uuid.uuid4()).split('-')[0]} {obj.title}",
                allow_unicode=True,
            )
        super().save_model(request, obj, form, change)


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
