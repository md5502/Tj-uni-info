from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
    path("events/", include("events.urls")),
    path("shohada/", include("shahid.urls")),
    path("professor-staff/", include("professor_staff.urls")),

    path("mdeditor/", include("mdeditor.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]


admin.site.site_header = _("Tj uni info admin")
