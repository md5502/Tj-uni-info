import random

from django.utils.text import slugify
from faker import Faker

fake = Faker("fa_IR")

# ایجاد 10 کاربر
users = []
for _ in range(10):
    user = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "description": fake.sentence(nb_words=10),
        "profile_image": "association/users/profiles/default.svg",
    }
    users.append(user)

# ایجاد 3 انجمن
associations = []
association_types = ["p", "A", "f"]
for _ in range(3):
    name = fake.company()
    association = {
        "name": name,
        "association_type": random.choice(association_types),
        "description": fake.paragraph(nb_sentences=3),
        "goals": fake.paragraph(nb_sentences=2),
        "social_media_link": fake.url(),
        "site_link": fake.url(),
        "channel_link": fake.url(),
        "logo": "association/logos/default.svg",
        "slug": slugify(name),
    }
    associations.append(association)

# ایجاد 10 عضو انجمن
positions = ["مدیر", "معاون", "دبیر", "عضو فعال", "عضو عادی"]
association_users = []
for _ in range(10):
    association_user = {
        "position": random.choice(positions),
        "user_id": random.choice(users),
        "association_id": random.choice(associations),
    }
    association_users.append(association_user)

# چاپ داده‌های ایجاد شده
print("کاربران:", users)
print("انجمن‌ها:", associations)
print("اعضای انجمن:", association_users)
