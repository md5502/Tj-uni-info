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
        number_of_events = 10  # Adjust the number of fake events

        for _ in range(number_of_events):
            # Create fake event data
            title = fake.sentence(nb_words=4)
            description = fake.paragraph(nb_sentences=5)
            slug = slugify(title, allow_unicode=True)
            schedule_date = fake.future_datetime()

            # Create event instance
            event = Event.objects.create(
                title=title,
                description=description,
                slug=slug,
                schedule_date=schedule_date,
            )

            # Download and attach random images to the event
            image_url = "https://picsum.photos/800/600"  # Using Lorem Picsum for random images
            image_content = requests.get(image_url).content

            # Create an in-memory file for the image
            image_io = BytesIO(image_content)
            image_name = f"{slug}.jpg"

            # Save the image to the database
            event_image = EventImage(event=event)
            event_image.image.save(image_name, File(image_io), save=True)

            self.stdout.write(self.style.SUCCESS(f"Added event: {title} with image"))
