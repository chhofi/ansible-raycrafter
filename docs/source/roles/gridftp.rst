========
gridftp
========

Install and configure gridftp client

---------
Variables
---------

======================== ==================================================================== ==================================================
Name                     Default                                                              Description
======================== ==================================================================== ==================================================
gridftp_repo_url         "deb http://toolkit.globus.org/ftppub/gt6/stable/deb trusty contrib" Argument for adding the globus apt repository
gridftp_package          "globus-data-management-client"                                      The name of the package to install for the
                                                                                              gridftp client.
gridftp_cert_file        "{{playbook_dir}}/files/ssl/gridftpcert.pem"                         Your certificate for GridFTP
gridftp_key_file         "{{playbook_dir}}/files/ssl/gridftpkey.pem"                          Your certificate key for GridFTP
gridftp_ca_package_url   "http://winnetou.surfsara.nl/deisa/certs/globuscerts.tar.gz"         Url for downloading the CA certificates.
======================== ==================================================================== ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
packages              Install packages
gridftp               Tag for all tasks in this role
===================== ==========================================================================
