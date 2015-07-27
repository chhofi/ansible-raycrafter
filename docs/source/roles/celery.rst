======
celery
======

Dependencies:

- web
- supervisor

Copies the startup and supervisor scripts. Will start workers and celerycam.
Celerycam is a monitoring service for celery workers and tasks.
Create log dirs and files.
Notifies supervisor to restart the celery app.

---------
Variables
---------

======================== ======================================================= ==================================================
Name                     Default                                                 Description
======================== ======================================================= ==================================================
celery_user              {{ gunicorn_user }}                                     The user which executes celery workers
celery_group             {{ gunicorn_group }}                                    The usergroup
celery_application_name  celery                                                  The name off the celery programm
celery_scripts_dir       {{ virtualenv_path }}/scripts/celery                    Path to the celery executable
celery_template_file     {{ celery_application_name }}_start.j2                  The template to use for the start script
celerycam_template_file: "celerycam_start.j2"                                    The template to use for celerycam. A monitor
                                                                                 service.
celery_worker_app        {{ application_name }}                                  The celery app name (used in the -A flag of the
                                                                                 celery executable)
celery_log_dir           {{ virtualenv_path }}/logs                              Dir for the log files
celery_log_file          {{ celery_log_dir }}/{{ celery_application_name }}.log  Full path to the log file
celerycam_log_file       "{{ celery_log_dir }}/celerycam.log"                    Full path to the celery cam log file
celery_num_workers       2                                                       Starts this many workers
======================== ======================================================= ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
celery                Tag for all tasks
supervisor            All supervisor related tasks, like copying the config or
                      restarting the app
===================== ==========================================================================
