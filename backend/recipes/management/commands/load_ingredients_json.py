import json

from django.conf import settings
from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(f'{settings.BASE_DIR}/data/ingredients.json') as json_file:
            data = json.load(json_file)
            for d in data:
                db = Ingredient(
                    name=d['name'],
                    measurement_unit=d['measurement_unit']
                )
                db.save()
