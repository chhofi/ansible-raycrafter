====================
ansible-django-stack
====================

.. image:: https://readthedocs.org/projects/ansible-django-stack/badge/?version=stable&style=flat
    :target: http://ansible-django-stack.readthedocs.org/en/stable/
    :alt: Documentation

Ansible_ Playbook designed for running a Raycrafter_ Master Server.
It installs and configures applications that are needed for production deployments.

It deploys a Django_ project and sets up Gunicorn_ and Nginx_ to serve your site.
PostgreSQL_ is used as database backend for Django_.
Celery_ (with RabbitMQ_ as message broker) for asynchronous task queue/job queue.

On top of that a logging server is deployed. In this case it is Graylog_, which depends
on Elasticsearch_ and MongoDB_.

Overview:

- Nginx_
- Gunicorn_
- PostgreSQL_
- Supervisor_
- Virtualenv_
- Memcached_
- Celery_
- RabbitMQ_
- Elasticsearch_
- MongoDB_
- Graylog_ Server/Web Interface

**Tested with OS:** Ubuntu 14.04 LTS x64

---------------
Getting Started
---------------

A fast way to test the setup is with Vagrant_ and VirtualBox_.

++++++++++++
Requirements
++++++++++++

- Ansible_
- Vagrant_
- VirtualBox_

Install all ansible requirements. You might have to specify a path for the roles where you have permissions. You can use the example below. Make sure not to commit the downloaded roles.::

  $ ansible-galaxy install -r requirements.txt -p ./roles

+++++++++++++
Configuration
+++++++++++++

There are two sets of configurations: ``env_vars/vagrant.yml`` and ``env_vars/production.yml``.
Here you configure your setup, like the location of your Git_ project, the project name, and application name which will be used throughout the Ansible_ configuration.
For more details see the documentation_.

I set some default values in ``env_vars`` based on a test project Djangotest_.
If you want to create your own Django_ project I recommend to use the Cookiecutter_ template: Cookiecutter-Django_. It is supposed to work out of the box with this setup. For more specific information on how to setup your Django_ project see the documentation_.

+++++++
Vagrant
+++++++

After installing Ansible_, Vagrant_ and VirtualBox_ you simply execute::

  vagrant up

Wait a few minutes for the magic to happen. Access the Django_ site by goingto this URL: https://192.168.33.15

Access the Graylog_ web-interface via: https://192.168.33.15:9000

That's it. One command, a little waiting and you are good to go.
For information on how to setup remote machines without vagrant see the documentation_.

------------
Useful Links
------------

- `Ansible - Getting Started <http://docs.ansible.com/intro_getting_started.html>`_
- `Ansible - Best Practices <http://docs.ansible.com/playbooks_best_practices.html>`_
- `Setting up Django with Nginx, Gunicorn,virtualenv, supervisor and PostgreSQL <http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/>`_
- `How to deploy encrypted copies of your SSL keys and other files with Ansible and OpenSSL <http://www.calazan.com/how-to-deploy-encrypted-copies-of-your-ssl-keys-and-other-files-with-ansible-and-openssl/>`_


.. _Nginx: http://nginx.org/
.. _Gunicorn: http://gunicorn.org/
.. _PostgreSQL: http://www.postgresql.org/
.. _Supervisor: http://supervisord.org/
.. _Virtualenv: https://virtualenv.pypa.io/en/latest/
.. _Memcached: http://memcached.org/
.. _Celery: http://www.celeryproject.org/
.. _RabbitMQ: https://www.rabbitmq.com/
.. _Elasticsearch: https://www.elastic.co/products/elasticsearch
.. _MongoDB: https://www.mongodb.org/
.. _Graylog: https://www.graylog.org/
.. _VirtualBox: https://virtualbox.org/
.. _Vagrant: https://vagrantup.com/
.. _Ansible: http://www.ansible.com/
.. _Raycrafter: https://github.com/RayCrafter
.. _Git: https://git-scm.com/
.. _Django: https://www.djangoproject.com/
.. _documentation: http://ansible-django-stack.readthedocs.org/en/latest/
.. _Djangotest: https://github.com/RayCrafter/djangotest
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Cookiecutter-Django: https://github.com/RayCrafter/cookiecutter-django
