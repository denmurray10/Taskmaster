import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taskmaster.settings')
django.setup()
User.objects.create_superuser('Den', '', 'Dennis10!')
