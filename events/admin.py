import uuid

from django.contrib import admin
from django.utils.text import slugify

from .models import Event, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    exclude = ("slug",)

    def save_model(self, request, obj, form, change):
        # Generate slug only if it's not provided
        if not obj.slug:
            obj.slug = slugify(
                f"{str(uuid.uuid4()).split('-')[0]} {obj.title}",
                allow_unicode=True,
            )
        super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)
admin.site.register(EventImage)