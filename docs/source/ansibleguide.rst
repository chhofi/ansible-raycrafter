.. _ansibleguide:

=============
Ansible Guide
=============

First, create an inventory file for the environment. For a simple setup just put in the IPs of the machines to deploy. For example create a file ``hosts`` with the content::

  # content of hosts inventory file
  # just a list of IPs
  # You can categorize them for more complex setups.
  141.62.110.220

Run the production playbook ``production.yml``::

  $ ansible-playbook -i hosts production.yml

If you're testing with vagrant, and the VM is already running, you can use this command::

  $ ansible-playbook -i vagrant_ansible_inventory_default --private-key=~/.vagrant.d/insecure_private_key vagrant.yml
