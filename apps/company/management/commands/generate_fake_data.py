# External packages
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from django.utils import timezone

# Internal packages
from ...models import Company


def generate_fake_company_name():
    fake = Faker()
    names = []
    for _ in range(20):
        name = fake.first_name() + ' Company'
        if name not in names:
            names.append(name)
    return names


def save_fake_name_in_db():
    names = generate_fake_company_name()
    for name in names:
        company = Company(name=name)
        company.save()    


class Command(BaseCommand):
    help = "Create fake company names"

    def handle(self, *args, **options):
        save_fake_name_in_db()
