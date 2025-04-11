import qrcode
from django.http import HttpResponse


def generate_qr_code(request, slug):
    base_url = request.build_absolute_uri("/")
    qr_data = request.build_absolute_uri(f"{base_url}/{slug}/")
    qr = qrcode.make(qr_data)
    response = HttpResponse(content_type="image/png")
    qr.save(response, "PNG")
    return response
