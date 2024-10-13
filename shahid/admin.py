import uuid

from django.contrib import admin
from django.utils.text import slugify
from django_jalali.admin.widgets import AdminjDateWidget
from django_jalali.db import models as jmodels  # Import jalali models

from .models import Image, Shahid


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # Allows adding an additional image in the Shahid form


class ShahidAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "martyrdom_date",
        "martyrdom_location",
        "birth_date",
        "birth_location",
    )
    exclude = ("slug",)
    # Remove slug from exclude to allow saving
    search_fields = ("first_name", "last_name", "martyrdom_location")
    inlines = [ImageInline]  # Adds inline images related to each Shahid

    formfield_overrides = {
        jmodels.jDateField: {"widget": AdminjDateWidget},
    }
    def save_model(self, request, obj, form, change):
        # Generate slug only if it's not provided
        if not obj.slug:
            obj.slug = slugify(
                f"{str(uuid.uuid4()).split('-')[0]} {obj.first_name} {obj.last_name}",
                allow_unicode=True,
            )
        super().save_model(request, obj, form, change)


class ImageAdmin(admin.ModelAdmin):
    list_display = ("owner", "image")
    search_fields = ("owner__first_name", "owner__last_name")  # Allows searching by Shahid's first and last name


admin.site.register(Shahid, ShahidAdmin)
admin.site.register(Image, ImageAdmin)
