import os
import sys

from django.contrib import auth
from django.db import utils

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ django_settings_file }}")

import django
django.setup()

try:
    usermodel = auth.get_user_model()
    try:
        usermodel.objects.create_superuser(
            '{{ superuser_name }}',
            '{{ superuser_email }}',
            '{{ superuser_password }}')
    except utils.IntegrityError:
        pass

    assert usermodel.objects.get(username='{{ superuser_name }}')
except Exception as e:
   raise SystemExit(1, e.message)
