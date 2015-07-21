.. _configuration:

=============
Configuration
=============

---------
Inventory
---------

In the ansible inventory file you can configure which machines to provision. See the `Ansible inventory documentation <http://docs.ansible.com/intro_inventory.html>`_.

--------
Playbook
--------

The next big step is your playbook. Here you can configure which roles to use on your hosts and what variables to use. Have a look at ``production.yml`` or ``vagrant.yml``.

---------
Variables
---------

The default playbooks use files in the ``env_vars`` directory to define most of the variables.
There is one config for using Vagrant and one for production.

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

There are some files that you might want to replace/encrypt, such as ssl/ssh keys.
For ssl certificates, create/override ``/files/ssl/application.pem``, ``/files/ssl/application.key_unencrypted``. The key should be encryptes::

  $ openssl aes-256-cbc -salt -a -e -in files/ssl/application.key_unencrypted -out files/ssl/application.key -k "YourSSLKeyPassword"

Do not commit the unencrypted version of the key!

You should also create an ssh-key for the master server so he can access the cluster via ssh.
Create a ssh keypair with::

  $ ssh-keygen -t rsa -b 4096 -C "raycrafter master server"

Move them to ``/files/ssh/id_rsa_unencrypted`` and ``/files/ssh/id_rsa.pub``.
Encrypt the key::

    $ openssl aes-256-cbc -salt -a -e -in files/ssh/id_rsa_unencrypted -out files/ssh/id_rsa -k "YourSSHKeyPassword"

Do not commit the unencrypted version of the key!

Store the password in ``/env_vars/secret.yml`` as ``ssl_key_password`` and ``ssh_key_password``. Make sure you envrypt that file with ansible vault::

  $ ansible-vault encrypt ./env_vars/secret.yml
