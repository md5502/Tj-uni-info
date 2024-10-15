from django.db import models
from django_jalali.db.models import jDateTimeField


class WorkExperience(models.Model):
    title = models.CharField(max_length=1000, verbose_name="عنوان")
    from_date = models.DateField(verbose_name="تاریخ شروع")
    to_date = models.DateField(verbose_name="تاریخ پایان")

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "سابقه کاری"
        verbose_name_plural = "سوابق کاری"

    def __str__(self) -> str:
        return self.title


class EducationalRecord(models.Model):
    title = models.CharField(max_length=1000, verbose_name="عنوان")
    date = models.DateField(verbose_name="تاریخ")

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "سابقه تحصیلی"
        verbose_name_plural = "سوابق تحصیلی"

    def __str__(self) -> str:
        return self.title


class Paper(models.Model):
    title = models.CharField(max_length=1000, verbose_name="عنوان")
    date = models.DateField(verbose_name="تاریخ انتشار")
    link = models.URLField(verbose_name="لینک", null=True, blank=True)

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self) -> str:
        return self.title


class AcademicActivity(models.Model):
    title = models.CharField(max_length=1200, verbose_name="عنوان")

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "فعالیت دانشگاهی"
        verbose_name_plural = "فعالیت های دانشگاهی"

    def __str__(self) -> str:
        return self.title


class ResearchArea(models.Model):
    title = models.CharField(max_length=1200, verbose_name="عنوان")

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "حوزه تحقیق"
        verbose_name_plural = "حوزه‌های تحقیقاتی"

    def __str__(self) -> str:
        return self.title


class ExternalLink(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    related_link = models.URLField(verbose_name="لینک")

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "لینک خارجی"
        verbose_name_plural = "لینک های خارجی"

    def __str__(self) -> str:
        return self.title


class TeachingCourse(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    semester = models.CharField(verbose_name="ترم درسی", max_length=300, null=True, blank=True)

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "درس تدریسی"
        verbose_name_plural = "دروس تدریسی"

    def __str__(self) -> str:
        return self.title


class Professor(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    fname = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    position = models.CharField(max_length=100, verbose_name="سمت کاری", null=True, blank=True)
    location = models.CharField(max_length=100, verbose_name="محل کار", null=True, blank=True)
    tag = models.CharField(verbose_name="تگ کاری", max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="شماره تلفن")
    profile_image = models.ImageField(
        verbose_name="عکس",
        upload_to="professors/profiles",
        default="professors/profiles/default.svg",
    )
    slug = models.SlugField(verbose_name="شناسه", allow_unicode=True, blank=True, null=True)
    research_areas = models.ManyToManyField(ResearchArea, verbose_name="حوزه‌های تحقیقاتی", blank=True)
    educational_records = models.ManyToManyField(EducationalRecord, verbose_name="سوابق تحصیلی", blank=True)
    teaching_courses = models.ManyToManyField(TeachingCourse, verbose_name="دروس تدریسی", blank=True)
    work_experiences = models.ManyToManyField(WorkExperience, verbose_name="سوابق کاری", blank=True)
    papers = models.ManyToManyField(Paper, verbose_name="مقالات", blank=True)
    academic_activities = models.ManyToManyField(AcademicActivity, verbose_name="فعالیت های دانشگاهی", blank=True)
    external_links = models.ManyToManyField(ExternalLink, verbose_name="لینک های خارجی", blank=True)

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "استاد"
        verbose_name_plural = "اساتید"

    def __str__(self) -> str:
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    fname = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    position = models.CharField(max_length=100, verbose_name="سمت کاری")
    tag = models.CharField(verbose_name="تگ کاری", max_length=30, null=True, blank=True)
    location = models.CharField(max_length=100, verbose_name="محل کار", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="شماره تلفن")
    slug = models.SlugField(verbose_name="شناسه", allow_unicode=True, blank=True, null=True)
    profile_image = models.ImageField(
        verbose_name="عکس",
        upload_to="staff/profiles",
        default="staff/profiles/default.svg",
    )

    educational_records = models.ManyToManyField(EducationalRecord, verbose_name="سوابق تحصیلی", blank=True)
    papers = models.ManyToManyField(Paper, verbose_name="مقالات", blank=True)
    teaching_courses = models.ManyToManyField(TeachingCourse, verbose_name="دروس تدریسی", blank=True)
    external_links = models.ManyToManyField(ExternalLink, verbose_name="لینک های خارجی", blank=True)
    academic_activities = models.ManyToManyField(AcademicActivity, verbose_name="فعالیت های دانشگاهی", blank=True)
    work_experiences = models.ManyToManyField(WorkExperience, verbose_name="سوابق کاری", blank=True)

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "کارمند"
        verbose_name_plural = "کارمندان"

    def __str__(self) -> str:
        return self.name
