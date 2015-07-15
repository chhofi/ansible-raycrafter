====
base
====

This role installs some basic packages, virtualenv and can be configured to create a swap file.

Ensures that these packages are the latest:

- bash
- openssl
- libssl-dev
- libssl-doc

Installs the following packages:

- build-essential
- ntp
- htop
- git
- libpq-dev
- python-dev
- python-pip
- python-pycurl
- '{{ language_pack}}'

Installs virtualenv with pip and ensures that the ntp service is running.


---------
Variables
---------

===================== ======================= ==================================================
Name                  Default                 Description
===================== ======================= ==================================================
create_swap_file      no                      If true/yes, creates a swap file.
language_pack         language-pack-en        The language-pack package name to install.
swap_file_path        /swapfile               Path to the swapfile.
swap_file_size_kb     512                     Note that block size is 1024, so the size of the
                                              size of the swap file will be
                                              1024 x ``swap_file_size_kb``.
update_apt_cache      true                    Update the apt cache before installing packages.
===================== ======================= ==================================================


----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
packages              Install base packages and virutalenv
service               Make sure ntp is running
swap                  Creates the swap file
===================== ==========================================================================
