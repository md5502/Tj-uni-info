from django.contrib import admin

from .models import Association, AssociationUser, User


# Define inline form for AssociationUser
class AssociationUserInline(admin.TabularInline):
    model = AssociationUser
    extra = 1  # Number of empty forms to display by default
    verbose_name = "عضو انجمن"
    verbose_name_plural = "اعضای انجمن"
    autocomplete_fields = ["user_id"]  # Optional: Allows searching users easily

# Register User model in admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("-created_at",)

# Register Association model in admin
@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    list_display = ("name", "association_type")
    search_fields = ("name", "association_type")
    list_filter = ("association_type",)
    ordering = ("-created_at",)
    inlines = [AssociationUserInline]  # Add the inline to the Association admin

# Register AssociationUser model in admin
@admin.register(AssociationUser)
class AssociationUserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "association_id", "position")
    search_fields = ("user_id__first_name", "user_id__last_name", "association_id__name", "position")
    list_filter = ("position", "association_id")
    ordering = ("user_id", "association_id")
