from django.contrib import auth
from django.db import utils

usermodel = auth.get_uesr_model()
try:
    usermodel.objects.create_superuser(
        '{{ superuser_name }}',
        '{{ superuser_email }}',
        '{{ superuser_password }}')
except utils.IntegrityError:
    pass

assert usermodel.objects.get(name='{{ superuser_name }}')
