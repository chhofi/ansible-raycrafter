.. _quickstart:

---------------
Quickstart
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
If you want to create your own Django_ project I recommend to use the Cookiecutter_ template: Cookiecutter-Django_. It is supposed to work out of the box with this setup. For more specific information on how to setup your Django_ project see the :ref:`Django <django>`.

+++++++
Vagrant
+++++++

After installing Ansible_, Vagrant_ and VirtualBox_ you simply execute::

  vagrant up

Wait a few minutes for the magic to happen. Access the Django_ site by goingto this URL: https://192.168.33.15

Access the Graylog_ web-interface via: https://192.168.33.15:9000

That's it. One command, a little waiting and you are good to go.
For information on how to setup remote machines without vagrant see the :ref:`Ansible Guide<ansibleguide>`.

.. _Graylog: https://www.graylog.org/
.. _VirtualBox: https://virtualbox.org/
.. _Vagrant: https://vagrantup.com/
.. _Ansible: http://www.ansible.com/
.. _Raycrafter: https://github.com/RayCrafter
.. _Git: https://git-scm.com/
.. _Django: https://www.djangoproject.com/
.. _Djangotest: https://github.com/RayCrafter/djangotest
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Cookiecutter-Django: https://github.com/RayCrafter/cookiecutter-django
