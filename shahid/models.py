from django.db import models
from django_jalali.db import models as jmodels


class Shahid(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="نام")
    last_name = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    martyrdom_location = models.CharField(max_length=200, verbose_name="محل شهادت")
    martyrdom_date = jmodels.jDateField(verbose_name="تاریخ شهادت")
    birth_date = jmodels.jDateField(null=True, blank=True, verbose_name="تاریخ تولد")
    birth_location = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="محل تولد",
    )
    life_story = models.TextField(null=True, blank=True, verbose_name="زندگی‌نامه")
    will = models.TextField(null=True, blank=True, verbose_name="وصیت‌نامه")
    important_quotes = models.TextField(
        null=True,
        blank=True,
        verbose_name="نقل‌قول‌های مهم",
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True,
        allow_unicode=True,
        verbose_name="شناسه",
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:  # noqa: DJ012
        verbose_name = "شهید"
        verbose_name_plural = "شهدا"


class Image(models.Model):  # noqa: DJ008
    image = models.ImageField(upload_to="shohada_images", verbose_name="عکس")
    owner = models.ForeignKey(
        Shahid,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="شهید",
    )

    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "عکس‌ها"  # noqa: RUF001
