from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """ Функция для создания суперпользователя. """
        user = User.objects.create(
            email='test@admin.ru',
            first_name='Admin',
            last_name='Adminov',
            role='admin',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        user.set_password('zxc123')
        user.save()
