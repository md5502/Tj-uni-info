from django.db import models
from django_jalali.db.models import jDateTimeField
from mdeditor.fields import MDTextField


class User(models.Model):
    first_name = models.CharField("نام", max_length=100)
    last_name = models.CharField("نام خانوادگی", max_length=100)
    email = models.EmailField("ایمیل", max_length=254)
    description = models.TextField("توضیحات کوتاه", max_length=300)
    profile_image = models.ImageField(
        verbose_name="عکس پروفایل",
        upload_to="association/users/profiles",
        default="association/users/profiles/default.svg",
    )

    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)

    class Meta:
        verbose_name = "عضو"
        verbose_name_plural = "اعضا"

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class AssociationUser(models.Model):
    position = models.CharField("سمت", max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    association_id = models.ForeignKey("Association", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user_id", "association_id")
        verbose_name = "عضو انجمن"
        verbose_name_plural = "اعضای انجمن"

    def __str__(self):
        return f"{self.user_id} {self.association_id}"


class Association(models.Model):
    ASSOCIATION_CHOICES = (
        ("p", "پرورشی"),
        ("A", "آموزشی"),
        ("f", "فرهنگی"),
    )
    name = models.CharField("نام", max_length=100)
    association_type = models.CharField(
        "نوع انجمن",
        max_length=100,
        choices=ASSOCIATION_CHOICES,
        default=ASSOCIATION_CHOICES[0][1],
    )
    description = models.TextField("توضیحات")

    association_users = models.ManyToManyField(
        to=User,
        through=AssociationUser,
        related_name="users",
    )
    goals = MDTextField(verbose_name="اهداف")
    social_media_link = models.URLField("لینک شبکه اجتماعی", max_length=200, blank=True, null=True)
    site_link = models.URLField("لینک وبسایت", max_length=200, blank=True, null=True)
    channel_link = models.URLField("لینک کانال", max_length=200, blank=True, null=True)
    created_at = jDateTimeField(verbose_name="ساخته شده در", auto_now_add=True)
    updated_at = jDateTimeField(verbose_name="ویرایش شده در", auto_now=True)
    profile_image = models.ImageField(
        verbose_name="لوگو انجمن",
        upload_to="association/logos",
        default="association/logos/default.svg",
    )

    class Meta:
        verbose_name = "انجمن"
        verbose_name_plural = "انجمن ها"

    def __str__(self):
        return self.name
