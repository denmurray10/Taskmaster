import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Taskmaster.settings')
import django
django.setup()
from django.contrib.auth.models import User
User.objects.create_superuser('Den', '', 'Dennis10!')
