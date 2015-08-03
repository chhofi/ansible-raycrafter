.. _ansibleguide:

=============
Ansible Guide
=============

Before you start, see the configuration section. There are some thing you need to setup first.

First, create an inventory file for the environment. There are three categories: ``masterservers``, ``crafternodes`` and ``hlrs``. The first category will deploy a RayCrafter Master Server. The second will setup a note that has ssh access to the cluster and submits jobs or transfers data. The third will setup everything at the cluster.

For example create a file ``hosts`` with the content::

  # content of hosts inventory file
  [masterservers]
  141.62.110.219 ansible_ssh_user=useronserver

  [crafternodes]
  141.62.110.220 ansible_ssh_user=useronserver
  
  [hlrs]
  hornet.hww.de ansible_ssh_user=hlrsaccountname

Run the main playbook ``sites.yml``, which includes the production and hlrs playbook::

  $ ansible-playbook -i hosts sites.yml --ask-vault-pass

If you're testing with vagrant, and the VM is already running, you can use this command::

  $ vagrant provision
