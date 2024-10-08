from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))
    slug = models.SlugField(_("slug"), unique=True, allow_unicode=True, null=True, blank=True)
    schedule_date = models.DateTimeField(_("schedule date"))
    location = models.CharField(_("location"), max_length=200, default="سالن همایش قاسم سلیمانی")
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self) -> str:
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, verbose_name=_("event"), on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(_("image"), upload_to="events_images/")

    def __str__(self) -> str:
        return f"Image for {self.event.title}"


class EventUser(models.Model):
    name = models.CharField(_("name"), max_length=100)
    fname = models.CharField(_("family name"), max_length=100)
    phone_number = models.CharField(_("phone number"), max_length=20)
    email = models.EmailField(_("email"), max_length=254)
    event = models.ForeignKey(Event, verbose_name=_("event"), on_delete=models.CASCADE)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, null=True, blank=True)

    class Meta:
        unique_together = ["event", "email"]

    def __str__(self):
        return self.name
