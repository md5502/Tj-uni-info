from django.db import models
from mdeditor.fields import MDTextField


class Event(models.Model):
    title = models.CharField("عنوان", max_length=100)
    description = MDTextField(verbose_name="توضیحات")
    slug = models.SlugField("شناسه", unique=True, allow_unicode=True, null=True, blank=True)
    schedule_date = models.DateTimeField("تاریخ برگذاری")
    location = models.CharField("مکان برگذاری", max_length=200, default="سالن همایش قاسم سلیمانی")
    created_at = models.DateTimeField("ساخته شده در", auto_now_add=True)
    updated_at = models.DateTimeField("ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "رخداد"
        verbose_name_plural = "رخداد ها"

    def __str__(self) -> str:
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, verbose_name="رخداد", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("عکس", upload_to="events_images/")

    class Meta:
        verbose_name = "عکس رخداد"
        verbose_name_plural = "عکس های رخداد"

    def __str__(self) -> str:
        return f"Image for {self.event.title}"


class EventUser(models.Model):
    name = models.CharField("نام", max_length=100)
    fname = models.CharField("نام خانوادگی", max_length=100)
    phone_number = models.CharField("شماره تلفن", max_length=20)
    email = models.EmailField("آدرس ایمیل", max_length=254)
    event = models.ForeignKey(Event, verbose_name="رخداد", on_delete=models.CASCADE, related_name="registered_users")

    created_at = models.DateTimeField("ساخته شده در", auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField("ویرایش شده در", auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "شرکت‌کننده"
        verbose_name_plural = "شرکت‌کننده ها"
        unique_together = ["event", "email"]

    def __str__(self):
        return self.name
