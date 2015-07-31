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

Install the software above.

Install all ansible requirements. You might have to specify a path for the roles where you have permissions. You can use the example below. Make sure not to commit the downloaded roles.::

  $ ansible-galaxy install -r requirements.yml -p ./roles

+++++++++++++
Configuration
+++++++++++++

The main configuration files are in ``env_vars/``.
Here you configure your setup, like the location of your Git_ project, the project name, and application name which will be used throughout the Ansible_ configuration.
For more information see :ref:`configuration`.

.. Note:: The current configuration requires some important files like ssh keys and ssl
          certificates. See :ref:`configuration` for more information. It will not work out of
          the box. You also need the password for ansible-vault, because ``env_vars/secret.yml``
          is encrypted. In the :ref:`configuration` section, you will find all necessary
          information on how to create your own secret configuration file and how to encrypt it.

I set some default values in ``env_vars`` based on a test project Djangotest_.
If you want to create your own Django_ project I recommend to use the Cookiecutter_ template: Cookiecutter-Django_. It is supposed to work out of the box with this setup. For more specific information on how to setup your Django_ project see :ref:`django`.

+++++++
Vagrant
+++++++

After installing Ansible_, Vagrant_ and VirtualBox_ you simply execute::

  vagrant up

.. Note:: You need the ansible vault password in order to do that. If you do not have the password,
          you need to create your own secret keys. See the configuration section for more
          information. You have to create a ``env_vars/secret.yml``, which you can encrypt
          with ansible vault. In there you set passwords. You also need the passwords for
          the encrypted shh and ssl keys. If you do not have these passwords, create your
          own keys. See the configuration section.

You have to create a ``vaultpwfile.txt`` with the vault password in it.
Wait a few minutes for the magic to happen. Access the Django_ site by goingto this URL: https://192.168.33.15

Access the Graylog_ web-interface via: https://192.168.33.15:9000

That's it. For information on how to setup remote machines without vagrant see the :ref:`Ansible Guide<ansibleguide>`.

~~~~~~~~~~~~~~~~~~~~~~~~~~~
Additional vagrant commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~

SSH to the box::

  vagrant ssh

Re-provision the box to apply the changes you made to the Ansible configuration::

  vagrant provision

Reboot the box::

  vagrant reload

Shut the box down::

  vagrant halt


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
