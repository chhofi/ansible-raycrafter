========
Gunicorn
========

Dependencies:

- supervisor

Create user and usergroup for gunicorn.
Create a virtualenv for gunicorn.
Install gunicorn.

Create gunicorn start script and logging files.
Create supervisor config files.
Make the gunicorn user owner of the virtual env path.

---------
Variables
---------

========================== ======================================================================================================================== ==================================================
Name                       Default                                                                                                                  Description
========================== ======================================================================================================================== ==================================================
application_name           "gunicorn"                                                                                                               Name of the application that gunicorn serves
virtualenv_root            "/webapps"                                                                                                               Location for where to create virtual env
virtualenv_path            "{{ virtualenv_root }}/{{ application_name }}"                                                                           Path to the virtual env
application_log_dir        "{{ virtualenv_path }}/logs"                                                                                             Path to the log dir
application_log_file       "{{ application_log_dir }}/gunicorn_supervisor.log"                                                                      Path to the log file
gunicorn_user              "{{ application_name }}"                                                                                                 Username for the user running gunicorn
gunicorn_group             webapps                                                                                                                  Groupname for the gunicorn user
gunicorn_num_workers       3                                                                                                                        Numer of gunicorn workers
gunicorn_max_requests      0                                                                                                                        Maximum requests before gunicorn restarts. 0 for
                                                                                                                                                    no limit.
gunicorn_timeout_seconds   30                                                                                                                       Maximum timeout for requests.
gunicorn_workdir           /                                                                                                                        Workdir for executing gunicorn
gunicorn_wsgi_file         ~                                                                                                                        Path to the wsgi file. Has to be importable.
========================== ======================================================================================================================== ==================================================

----
Tags
----

===================== ==========================================================================
Name                  Description
===================== ==========================================================================
virtualenv            Install packages
supervisor            Create configs and restart supervisor
gunicorn              Tag for all tasks
===================== ==========================================================================

