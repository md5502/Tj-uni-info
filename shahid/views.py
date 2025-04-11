import os
import zipfile

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Shahid
from .selectors import get_shahid_list, get_shahid_via_slug
from .services import build_shahid_list_context


def shahid_list(request):
    shahid_list = get_shahid_list(request)
    context = build_shahid_list_context(shahid_list)
    return render(request, "shahid/list.html", context)


def shahid_detail(request, slug):
    shahid = get_shahid_via_slug(slug)
    return render(request, "shahid/detail.html", {"shahid": shahid})


def download_shahid_images(request, slug):
    shahid = get_object_or_404(Shahid, slug=slug)

    # Set the zip file name to Shahid's name
    zip_filename = f"{shahid.first_name}_{shahid.last_name}_images.zip"  # Change this line

    # Create a ZIP file in memory
    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = f"attachment; filename={zip_filename}"

    with zipfile.ZipFile(response, "w") as zip_file:
        for image in shahid.images.all():
            image_path = image.image.path
            zip_file.write(image_path, os.path.name(image_path))

    return response
