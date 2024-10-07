from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"))
    slug = models.SlugField(_("slug"))
    schedule_date = models.DateTimeField(_("schedule date"))

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    def __str__(self) -> str:
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, verbose_name=_("event"), on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(_("image"), upload_to="events_images/")

    def __str__(self) -> str:
        return f"Image for {self.event.title}"
