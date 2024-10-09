from django.contrib import admin

from .models import (
    AcademicActivity,
    EducationalRecord,
    ExternalLink,
    Paper,
    Professor,
    ResearchArea,
    Staff,
    TeachingCourse,
    WorkExperience,
)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("name", "fname", "position", "location", "phone_number")
    search_fields = ("name", "fname", "position")
    list_filter = ("position", "location")


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "fname", "position", "location", "phone_number")
    search_fields = ("name", "fname", "position")
    list_filter = ("position", "location")



@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "from_date", "to_date")
    search_fields = ("title",)
    list_filter = ("from_date", "to_date")


@admin.register(EducationalRecord)
class EducationalRecordAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title",)
    list_filter = ("date",)


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "link")
    search_fields = ("title",)
    list_filter = ("date",)


@admin.register(AcademicActivity)
class AcademicActivityAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(ExternalLink)
class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "related_link")
    search_fields = ("title", "related_link")


@admin.register(TeachingCourse)
class TeachingCourseAdmin(admin.ModelAdmin):
    list_display = ("title", "semester")
    search_fields = ("title", "semester")


@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
