=========
Celerycam
=========

Dependencies:

- web
- supervisor

Copies the startup and supervisor scripts. Will start the celerycam service.
Celerycam is a monitoring service for celery workers and tasks.
Create log dirs and files.
Notifies supervisor to restart the celerycam service.

---------
Variables
---------

========================== ======================================================= ==================================================
Name                       Default                                                 Description
========================== ======================================================= ==================================================
celerycam_user             {{ web_user }}                                          The user which executes celery workers
celerycam_group            {{ web_group }}                                         The usergroup
celerycam_scripts_dir      {{ virtualenv_path }}/scripts/celerycam                 Path to the celery executable
celerycam_template_file    "celerycam_start.j2"                                    The template to use for celerycam. A monitor
                                                                                   service.
celerycam_log_dir          {{ virtualenv_path }}/logs                              Dir for the log files
celerycam_log_file         "{{ celery_log_dir }}/celerycam.log"                    Full path to the celery cam log file
========================== ======================================================= ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
celerycam             Tag for all tasks
supervisor            All supervisor related tasks, like copying the config or
                      restarting the app
===================== ==========================================================================

