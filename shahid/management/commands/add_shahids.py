import uuid
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from shahid.models import Shahid  # تغییر دهید به نام اپلیکیشن شما


class Command(BaseCommand):
    help = "Add shahids to the database"

    def handle(self, *args, **kwargs):

        shahids_data = [
            {
                "first_name": "سید علی",
                "last_name": "اندرزگو",
                "martyrdom_location": "تهران",
                "martyrdom_date": "1962-07-23",
                "birth_date": "1342-05-01",
                "birth_location": "تهران",
                "description": "از شهدای سرشناس دفاع مقدس و فرمانده واحد اطلاعات.",
                "will": "خداوند را شکر می‌کنم که توفیق خدمت به مردم و کشورم را به من عطا فرمود. امیدوارم که جوانان این مرز و بوم با ایمان و اراده قوی در راه دفاع از کشور پیشرفت کنند.",
                "important_quotes": "ما باید به انقلاب ادامه دهیم.",
            },
            {
                "first_name": "مهدی",
                "last_name": "باکری",
                "martyrdom_location": "عملیات بیت‌المقدس",
                "martyrdom_date": "1982-05-24",
                "birth_date": "1342-02-25",
                "birth_location": "ارومیه",
                "description": "فرمانده لشکر ۳۱ عاشورا و یکی از بهترین رزمندگان جنگ.",
                "will": "ای جوانان! بدانید که امروز کشور نیازمند شماست. به جبهه‌های حق بیایید و از اسلام و ایران دفاع کنید.",
                "important_quotes": "خود را برای شهادت آماده کنید.",
            },
            {
                "first_name": "محمد",
                "last_name": "بروجردی",
                "martyrdom_location": "عملیات مرصاد",
                "martyrdom_date": "1988-05-27",
                "birth_date": "1342-04-01",
                "birth_location": "بروجرد",
                "description": "یکی از برجسته‌ترین فرماندهان سپاه و رزمندگان اسلام.",
                "will": "من به شهادت در راه خدا امیدوارم و از شما می‌خواهم که به مسیر انقلاب ادامه دهید.",
                "important_quotes": "هرگز تسلیم نخواهید شد.",
            },
            {
                "first_name": "حسین",
                "last_name": "خرازی",
                "martyrdom_location": "خرمشهر",
                "martyrdom_date": "1980-02-23",
                "birth_date": "1342-03-21",
                "birth_location": "شوشتر",
                "description": "فرمانده لشکر ۱۴ امام حسین (ع) و از فرماندهان تاثیرگذار.",
                "will": "ای دوستان! امیدوارم که همواره در راه حق و حقیقت ثابت‌قدم باشید.",
                "important_quotes": "شهادت برای من افتخار است.",
            },
            {
                "first_name": "عباس",
                "last_name": "بابایی",
                "martyrdom_location": "آبادان",
                "martyrdom_date": "1985-02-24",
                "birth_date": "1334-01-01",
                "birth_location": "همدان",
                "description": "از خلبانان برجسته نیروی هوایی و قهرمان جنگ.",
                "will": "در این لحظه که به جبهه می‌روم، از خانواده و دوستان می‌خواهم که در راه حق و حقیقت بایستند.",
                "important_quotes": "پرواز برایم یک عبادت است.",
            },
            {
                "first_name": "محسن",
                "last_name": "حججی",
                "martyrdom_location": "خانطومان",
                "martyrdom_date": "2017-07-21",
                "birth_date": "1362-04-21",
                "birth_location": "نجف‌آباد",
                "description": "شهید مدافع حرم و الگوی ایثار و فداکاری.",
                "will": "من به عشق حسین(ع) به میدان آمدم و از شما می‌خواهم که به دنبال حق و حقیقت باشید.",
                "important_quotes": "من به عشق حسین(ع) به میدان آمدم.",
            },
            {
                "first_name": "سعید",
                "last_name": "قاسمی",
                "martyrdom_location": "شلمچه",
                "martyrdom_date": "1985-04-02",
                "birth_date": "1341-04-25",
                "birth_location": "شیراز",
                "description": "فرمانده گردان و از رزمندگان خط مقدم.",
                "will": "ای رزمندگان اسلام! بر سر این زمین و در زیر این آسمان، من از شما می‌خواهم که همیشه به یاد خدا باشید.",
                "important_quotes": "مرد میدان باشید.",
            },
            {
                "first_name": "علی",
                "last_name": "انصاری",
                "martyrdom_location": "مهران",
                "martyrdom_date": "1985-06-23",
                "birth_date": "1344-01-15",
                "birth_location": "خرم‌آباد",
                "description": "از جوانان با ایمان و با شهامت.",
                "will": "به دوستانم می‌گویم که ایمان و اراده شما در راه خدا مهم‌ترین چیز است.",
                "important_quotes": "منافقین را بشناسید و مقابلشان بایستید.",
            },
            {
                "first_name": "اسماعیل",
                "last_name": "دقایقی",
                "martyrdom_location": "فاو",
                "martyrdom_date": "1986-01-01",
                "birth_date": "1343-07-02",
                "birth_location": "اهواز",
                "description": "شهید عملیات والفجر ۸.",
                "will": "من به عنوان یک مسلمان و ایرانی از شما می‌خواهم که به جبهه‌ها بیایید و در برابر ظلم و ستم بایستید.",
                "important_quotes": "هرگز از مسیر حق منحرف نشوید.",
            },
            {
                "first_name": "جعفر",
                "last_name": "نیک‌روش",
                "martyrdom_location": "پاسگاه زید",
                "martyrdom_date": "1982-06-02",
                "birth_date": "1342-03-16",
                "birth_location": "کرمانشاه",
                "description": "از شهدای عملیات رمضان.",
                "will": "شهادت برای من یک نعمت بزرگ است و امیدوارم که شما نیز به این مقام نائل شوید.",
                "important_quotes": "هرگز به خودت شک نکن.",
            },
            {
                "first_name": "ابراهیم",
                "last_name": "هادی",
                "martyrdom_location": "خرمشهر",
                "martyrdom_date": "1981-02-21",
                "birth_date": "1330-04-10",
                "birth_location": "خرم‌آباد",
                "description": "فرمانده و از مجروحان جنگ.",
                "will": "از شما می‌خواهم که همیشه در یاد شهدا باشید.",
                "important_quotes": "باید به دنبال اهداف عالی باشید.",
            },
            {
                "first_name": "مصطفی",
                "last_name": "چمران",
                "martyrdom_location": "خرمشهر",
                "martyrdom_date": "1981-02-21",
                "birth_date": "1320-01-22",
                "birth_location": "تهران",
                "description": "از شخصیت‌های سیاسی و نظامی.",
                "will": "مقاومت و ایستادگی شما در برابر دشمن، باعث پیروزی و سربلندی این ملت خواهد بود.",
                "important_quotes": "سعی کنید به خدا نزدیک شوید.",
            },
            {
                "first_name": "حسین",
                "last_name": "علم‌الهدی",
                "martyrdom_location": "بصره",
                "martyrdom_date": "1985-04-21",
                "birth_date": "1343-05-10",
                "birth_location": "تهران",
                "description": "فرمانده عملیات انتحاری.",
                "will": "شهادت برای من هدفی بزرگ است و از شما می‌خواهم که هیچ‌گاه در برابر ظلم و ستم تسلیم نشوید.",
                "important_quotes": "شهادت بزرگ‌ترین نعمت است.",
            },
            {
                "first_name": "سید حسن",
                "last_name": "نصرالله",
                "martyrdom_location": "عملیات والفجر ۱",
                "martyrdom_date": "1983-02-22",
                "birth_date": "1345-02-01",
                "birth_location": "لبنان",
                "description": "از رزمندگان مشهور.",
                "will": "من به عشق آزادی و حق به میدان آمده‌ام.",
                "important_quotes": "باید به دشمن رحم نکرد.",
            },
        ]

        for data in shahids_data:
            try:
                shahid = Shahid(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    martyrdom_location=data["martyrdom_location"],
                    martyrdom_date=datetime.strptime(data["martyrdom_date"], "%Y-%m-%d").date(),
                    birth_date=datetime.strptime(data["birth_date"], "%Y-%m-%d").date() if data.get("birth_date") else None,
                    birth_location=data.get("birth_location"),
                    description=data["description"],
                    will=data["will"],
                    important_quotes=data["important_quotes"],
                )
                # ساخت اسلاگ با استفاده از uuid و slugify
                shahid.slug = slugify(
                    f"{str(uuid.uuid4()).split('-')[0]} {shahid.first_name} {shahid.last_name}",
                    allow_unicode=True,
                )
                shahid.save()  # ذخیره شهید در پایگاه داده
                self.stdout.write(self.style.SUCCESS(f"شهادت {shahid} با موفقیت ذخیره شد."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"خطا در ذخیره {data['first_name']} {data['last_name']}: {e}"))
