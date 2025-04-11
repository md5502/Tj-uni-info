from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_jalali.db.models import jDateField, jDateTimeField


class Event(models.Model):
    title = models.CharField("عنوان", max_length=100)
    description = models.TextField(verbose_name="توضیحات")

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="نوع برگزارکننده",
    )

    object_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="شناسه برگزارکننده",
    )
    organizer = GenericForeignKey("content_type", "object_id")

    slug = models.SlugField("شناسه", unique=True, allow_unicode=True, null=True, blank=True)
    schedule_date = jDateTimeField(verbose_name="تاریخ برگزاری")
    register_deadline = jDateField(verbose_name="تاریخ مهلت ثبت‌نام")
    location = models.CharField("مکان برگزاری", max_length=200, default="سالن همایش قاسم سلیمانی")
    capacity = models.PositiveIntegerField("ظرفیت رخداد", default=0, blank=True)
    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "رخداد"
        verbose_name_plural = "رخدادها"

    def __str__(self) -> str:
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title, allow_unicode=True) + '-' +  str(self.pk)
    #     super().save(*args, **kwargs)



class EventImage(models.Model):
    event = models.ForeignKey(Event, verbose_name="رخداد", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("عکس", upload_to="events_images/")

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "عکس رخداد"
        verbose_name_plural = "عکس های رخداد"

    def __str__(self) -> str:
        return f"Image for {self.event.title}"


class EventUser(models.Model):
    name = models.CharField("نام", max_length=100)
    fname = models.CharField("نام خانوادگی", max_length=100)
    phone_number = models.CharField("شماره تلفن", max_length=20, null=True, blank=True)
    student_number = models.CharField("شماره دانشجویی", max_length=20)
    email = models.EmailField("آدرس ایمیل", max_length=254)
    branch = models.CharField(verbose_name="رشته تحصیلی", max_length=100, null=True, blank=True)
    event = models.ForeignKey(Event, verbose_name="رخداد", on_delete=models.CASCADE, related_name="registered_users")

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "شرکت‌کننده"
        verbose_name_plural = "شرکت‌کننده ها"
        unique_together = ["event", "email"]

    def __str__(self):
        return self.name
