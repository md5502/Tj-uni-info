import os
import zipfile

import qrcode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Shahid


def shahid_list(request):
    shahids = Shahid.objects.all()

    return render(request, "shahid/list.html", {"shahid_list": shahids})


def shahid_detail(request, slug):
    shahid = get_object_or_404(Shahid, slug=slug)
    return render(request, "shahid/detail.html", {"shahid": shahid})




def generate_qr_code(request, slug):
    shahid = get_object_or_404(Shahid, slug=slug)
    qr_data = request.build_absolute_uri(f"/shahid/{shahid.slug}/")
    qr = qrcode.make(qr_data)

    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response





def download_shahid_images(request, slug):
    shahid = get_object_or_404(Shahid, slug=slug)

    # Set the zip file name to Shahid's name
    zip_filename = f"{shahid.name}_{shahid.lname}_images.zip"  # Change this line

    # Create a ZIP file in memory
    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = f"attachment; filename={zip_filename}"

    with zipfile.ZipFile(response, "w") as zip_file:
        for image in shahid.images.all():
            image_path = image.image.path  # Get the image path
            zip_file.write(image_path, os.path.basename(image_path))  # Write the image to the ZIP file

    return response
