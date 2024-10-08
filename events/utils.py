import csv
from io import StringIO

from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string


def generate_csv_response(queryset):
    # Create a file-like object for CSV content
    output = StringIO()

    # Define field names for the CSV
    fieldnames = [
        "نام",
        "نام خانوادگی",
        "شماره تماس",
        "شماره دانشجویی",
        "رشته تحصیلی",
        "ایمیل",
    ]

    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each event and add user data
    for obj in queryset:
        users = obj.registered_users.all()
        if users.exists():
            for user in users:
                user_info = {
                    "نام": user.name,
                    "نام خانوادگی": user.fname,
                    "شماره تماس": user.phone_number if user.phone_number else "***",
                    "شماره دانشجویی": user.student_number,
                    "رشته تحصیلی": user.branch if user.branch else "***",
                    "ایمیل": user.email,
                }
                combined_info = {**user_info}

                writer.writerow(combined_info)

    # Create an HTTP response with the CSV content
    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="registered_users.csv"'

    return response




def send_registration_email(user_email, name, event_title, event_date, event_location, event_url):
    # Render the HTML email template
    subject = "تأیید ثبت‌نام در رخداد"
    message = render_to_string(
        "emails/event_registration.html",
        {
            "first_name": name,
            "event_title": event_title,
            "event_date": event_date,
            "event_location": event_location,  # Include location in the email
            "event_url": event_url,
        },
    )
    email = EmailMessage(subject, message, to=[user_email])
    email.content_subtype = "html"  # Set the email to HTML format
    email.send()
