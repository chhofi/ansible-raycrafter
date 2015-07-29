========
gridftp
========

Install and configure gridftp client

---------
Variables
---------

========================= ========================================================================================= ==================================================
Name                      Default                                                                                   Description
========================= ========================================================================================= ==================================================
gridftp_user              "gridftp"                                                                                 The user that uses gridftp
gridftp_repo_url          "http://toolkit.globus.org/ftppub/gt6/installers/repo/globus-toolkit-repo_latest_all.deb" Argument for adding the globus apt repository
gridftp_package           "globus-data-management-client"                                                           The name of the package to install for the
                                                                                                                    gridftp client.
gridftp_cert_file         "{{playbook_dir}}/files/ssl/gridftpcert.pem"                                              Your certificate for GridFTP
gridftp_key_file          "{{playbook_dir}}/files/ssl/gridftpkey.pem"                                               Your certificate key for GridFTP
gridftp_ca_package_url    "http://winnetou.surfsara.nl/deisa/certs/globuscerts.tar.gz"                              Url for downloading the CA certificates.
gridftp_repo_creates_file "globus-toolkit-6-stable-trusty.list"                                                     The file that gets created when installing the
                                                                                                                    repo. This is used as a simple check, whether the
                                                                                                                    repo is installed.
========================= ========================================================================================= ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
packages              Install packages
gridftp               Tag for all tasks in this role
===================== ==========================================================================
