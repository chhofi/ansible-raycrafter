.. _configuration:

=============
Configuration
=============

---------
Inventory
---------

In the ansible inventory file you can configure which machines to provision. See the `Ansible inventory documentation <http://docs.ansible.com/intro_inventory.html>`_.
The :ref:`ansibleguide` explains how to create an inventory file.

--------
Playbook
--------

The next big step is your playbook. Here you can configure which roles to use on your hosts and what variables to use. Have a look at ``site.yml``. It includes several other playbooks and provisions a master server, crafternodes and the cluster.

---------
Variables
---------

The default playbooks use files in the ``env_vars`` directory to define most of the variables.

Secret variables like passwords are stored in ``env_vars/secret.yml``. You can encrypt this file with `Ansible Vault <http://docs.ansible.com/playbooks_vault.html>`_. You can decrypt them for editing. You should always encrypt this file when commiting to a public repository::

  $ ansible-vault encrypt ./env_vars/secret.yml

You should check the `documentation of each role <roles>`_ for in-depth explanation of each variable.

The contents of ``env_vars/secret.yml`` should be something like but with actual passwords::

  ---
  superuser_password: <yourpassword>
  db_password: <secret pw>
  rabbitmq_admin_password: <supersecretpw>
  rabbitmq_appliaction_password: <bulletproofpw>
  django_secret_key: <cryptographic secure key!!>
  django_email_host_password: ~
  graylog_password_secret: 2jueVqZpwLLjaWxV # generate with pwgen -s 96 1
  graylog_root_password_sha2: 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
  graylog_root_password_unencrypted: admin
  graylog_web_secret: 2jueVqZpwLLjaWxV # generate with pwgen -s 96 1
  ssl_key_password: <pw you used for encryption of the file>
  ssh_key_password: <pw you used for encryption of the file>

-----
Files
-----

There are some files that you have to create such as ssh/ssl keys.

For ssl certificates, create/override ``/files/ssl/application.pem``, ``/files/ssl/application.key`` with your certificate and private key.

In order to use GridFTP, you need to have a X.509 certificate and key. See the `HLRS GridFTP Wiki <https://wickie.hlrs.de/platforms/index.php/Data_Transfer_with_GridFTP>`_. By default, you have to put them in ``/files/ssl/usercert.pem`` and ``/files/ssl/userkey.pem``.
See :ref:`raycrafterdoc:gridftp`.

You should also create an ssh-key for the crafternodes so they can access the cluster via ssh.
Create a ssh keypair with::

  $ ssh-keygen -t rsa -b 4096 -C "raycrafter master server"

Move them to ``/files/ssh/id_rsa`` and ``/files/ssh/id_rsa.pub``.
The keys will be added to authorized hosts on the cluster by the role ``hlrsenv``.
