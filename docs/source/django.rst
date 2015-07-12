.. _django:

======
Django
======

You can use any django project you want but you might have to configure some things.
The best way to start is to use the Cookiecutter-Django_ template. It will create the
whole project skeleton for you and is ready to use with this project.

Note that the default values in the playbooks assume that your project structure looks something like this::

  myproject
  ├── manage.py
  ├── myproject
  │   ├── apps
  │   │   └── __init__.py
  │   ├── templates
  │   │   ├── 403.html
  │   │   ├── 404.html
  │   │   ├── 500.html
  │   │   └── base.html
  │   ├── __init__.py
  │   ├── celery.py
  ├── config
  │   ├── settings
  │   │   ├── base.py
  │   │   ├── __init__.py
  │   │   ├── local.py
  │   │   └── production.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── README.md
  └── requirements.txt

The main things to note are the locations of the ``manage.py``, ``wsgi.py`` and ``celery.py`` files.  If your project's structure is a little different, you may need to change the values in these 3 files:

- ``roles/web/tasks/setup_django_app.yml``
- ``roles/web/templates/gunicorn_start.j2``
- ``roles/celery/templates/celery_start.j2``

Also, if your app needs additional system packages installed, you can add them in ``roles/web/tasks/install_additional_packages.yml``.

--------
Settings
--------

Your django project settings have to be setup in a way so that they can be set via environment variables. A good way is 12-Factor_ based settings via django-environ_.
Check the Cookiecutter-Django_ settings. They are setup so that the following environment variables take effect:

* ``DJANGO_SETTINGS_MODULE``
* ``DJANGO_SECRET_KEY``
* ``MEDIA_ROOT``
* ``STATIC_ROOT``
* ``DATABASE_URL``
* ``DJANGO_EMAIL_HOST``
* ``EMAIL_PORT``
* ``EMAIL_HOST_USER``
* ``EMAIL_HOST_PASSWORD``
* ``DJANGO_DEFAULT_FROM_EMAIL``
* ``BROKER_URL``

+++++++
Logging
+++++++

To log to the Graylog_ server, you have to configure your logger. The best way is to use Graypy_.
It transmits logs via UDP or alternatively with RabbitMQ_.
Here is a sample from the test project::

  LOGGING = {
      'handlers': {
          'graypy': {
              'class': 'graypy.GELFHandler',
              'host': 'localhost',
              'port': 12201,
          },
          ...
      },
      'loggers': {
          'django.request': {
              'handlers': ['graypy', ...],
              'level': 'WARNING',
              'propagate': True,
          },
  	...
      }
  }


.. _Graylog: https://www.graylog.org/
.. _Graypy: https://pypi.python.org/pypi/graypy
.. _RabbitMQ: https://www.rabbitmq.com/
.. _django-environ: https://github.com/joke2k/django-environ
.. _12-Factor: http://12factor.net/
.. _Cookiecutter-Django: https://github.com/RayCrafter/cookiecutter-django
