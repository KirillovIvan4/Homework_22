from django.core.management.base import BaseCommand
from online_store.models import Product, Category

class Command(BaseCommand):
    help = 'Add test students to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category,_ = Category.objects.get_or_create(name='Стол')
        tables = [
            {'name':"Стол письменный_1", 'description': "Стол письменный",'category':category, 'purchase_price': '1000'},
            {'name': "Стол письменный_2", 'description': "Стол письменный",'category':category, 'purchase_price': '1000'},
        ]
        for table_data in tables:
            table, created = Product.objects.get_or_create(**table_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added student: {table.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Student already exists: {table.name}'))