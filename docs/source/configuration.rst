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

Also encrypt your ssl certificates in ``files/ssl/``::

  $ ansible-vault encrypt ./files/ssl/application.key

To decrypt use::

  $ ansible-vault decrypt ./env_vars/secret.yml ./files/ssl/application.key

You should check the `documentation of each role <roles>`_ for in-depth explanation of each variable.
