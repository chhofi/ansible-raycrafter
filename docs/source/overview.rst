========
Overview
========

This is an Ansible_ Playbook designed for running a Raycrafter_ Master Server.
It installs and configures applications that are needed for production deployments.

It deploys a Django_ project and sets up Gunicorn_ and Nginx_ to serve your site.
PostgreSQL_ is used as database backend for Django_.
Celery_ (with RabbitMQ_ as message broker) for asynchronous task queue/job queue.

On top of that a logging server is deployed. In this case it is Graylog_, which depends
on Elasticsearch_ and MongoDB_.

Stack:

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
.. _Raycrafter: https://github.com/RayCrafter/
.. _Django: https://www.djangoproject.com/

------------
Architecture
------------

Master Server - HLRS interaction

.. figure:: architecture.png

----------------------
Task Queue with Celery
----------------------

Celery is used to handle long running tasks like transferring files or submitting jobs.

.. figure:: http://blog.langoor.mobi/wp-content/uploads/2013/07/django_celery_architecture.png
   :alt: Celery Architecture

---------------------------
Logging Server with Graylog
---------------------------

Graylog Server setup.

.. figure:: http://docs.graylog.org/en/latest/_images/simple_setup.png
   :alt: Graylog Architecture
