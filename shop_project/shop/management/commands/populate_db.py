from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import *
import random

fake = Faker('ru_RU')

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **options):
        users = []
        profiles = []
        products = []

        # Генерируем фейковых пользователей
        for i in range(50):
            username = fake.user_name()
            password = fake.password(length=10)
            new_user = User(username=username, email=fake.email())
            new_user.set_password(password)
            new_user.save()

            profile = Profile(user=new_user, phone_number=fake.phone_number(), address_city=fake.city())
            profile.save()
            users.append(new_user)
            profiles.append(profile)

        # Генерируем продукцию
        categories = ['Фрукты', 'Овощи', 'Напитки']
        for _ in range(70):
            product = Product(name=f"{categories[random.randrange(len(categories))]} : {fake.word()}",
                              description=fake.text(),
                              price=round(random.uniform(10, 100), 2),
                              quantity=random.randint(1, 100))
            product.save()
            products.append(product)

        # Создаем случайные заказы
        for user in users[:20]:
            order = Order(client=user,
                          total_amount=sum([p.price for p in random.sample(products, k=random.randint(1, len(products)))])
                          )
            order.save()
            selected_products = random.sample(products, k=random.randint(1, len(products)))
            for prod in selected_products:
                item = OrderItem(order=order, product=prod, quantity=random.randint(1, 10))
                item.save()