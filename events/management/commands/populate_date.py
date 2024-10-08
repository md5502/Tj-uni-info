from io import BytesIO
import requests
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker

from events.models import Event, EventImage


class Command(BaseCommand):
    help = "Populate the database with fake events and images."

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_events = 10  # تعداد رویدادهای جعلی قابل تنظیم

        for _ in range(number_of_events):
            # ایجاد داده‌های جعلی برای رویداد
            title = fake.sentence(nb_words=4)
            description_paragraphs = fake.paragraphs(nb=5)  # تولید ۵ پاراگراف
            description = "\n\n".join(description_paragraphs)  # اتصال پاراگراف‌ها با خط جدید
            slug = slugify(title, allow_unicode=True)
            schedule_date = fake.future_datetime()

            # ایجاد رویداد
            event = Event.objects.create(
                title=title,
                description=description,
                slug=slug,
                schedule_date=schedule_date,
            )

            # دانلود و ضمیمه کردن تصاویر تصادفی به رویداد
            image_url = "https://picsum.photos/800/600"  # استفاده از Lorem Picsum برای تصاویر تصادفی
            image_content = requests.get(image_url).content

            # ایجاد فایل در حافظه برای تصویر
            image_io = BytesIO(image_content)
            image_name = f"{slug}.jpg"

            # ذخیره تصویر در دیتابیس
            event_image = EventImage(event=event)
            event_image.image.save(image_name, File(image_io), save=True)

            self.stdout.write(self.style.SUCCESS(f"Added event: {title} with image"))
