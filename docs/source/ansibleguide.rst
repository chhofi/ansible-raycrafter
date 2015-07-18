.. _ansibleguide:

=============
Ansible Guide
=============

First, create an inventory file for the environment. There are two categories: ``masterservers`` and ``hlrs``. The first category will deploy a RayCrafter Master Server. The second will setup everything at the cluster.

For example create a file ``hosts`` with the content::

  # content of hosts inventory file
  [masterservers]
  141.62.110.220
  
  [hlrs]
  hornet.hww.de

Run the main playbook ``sites.yml``, which includes the production and hlrs playbook::

  $ ansible-playbook -i hosts sites.yml

If you're testing with vagrant, and the VM is already running, you can use this command::

  $ ansible-playbook -i vagrant_ansible_inventory_default --private-key=~/.vagrant.d/insecure_private_key vagrant.yml
