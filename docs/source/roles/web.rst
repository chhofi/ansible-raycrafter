===
Web
===

Dependencies:

- supervisor

Create user and usergroup for django.
Create a virtualenv for the django project.

Configure the virutalenv postactivate, so django environment variables are set.

Set up the git repo of the django project.

Install additional packages. In the current configuration ``./install_os_dependencies.sh install`` is executed in the project directory. You likely have to change this.

Create supervisor config files.
Make the django user owner of the virtual env path.

---------
Variables
---------

========================== ======================================================================================================================== ==================================================
Name                       Default                                                                                                                  Description
========================== ======================================================================================================================== ==================================================
git_repo                   https://github.com/RayCrafter/djangotest.git                                                                             Link to the git repository
git_branch                 master                                                                                                                   Git branch to checkout
setup_git_repo             true                                                                                                                     If false, do not setup git repository
project_name               djangotest                                                                                                               Name of your django project
application_name           "{{ project_name }}"                                                                                                     
virtualenv_root            "/webapps"                                                                                                               Location for where to create virtual env
virtualenv_path            "{{ virtualenv_root }}/{{ application_name }}"                                                                           Path to the virtual env
project_path               "{{ virtualenv_path }}/{{ project_name }}"                                                                               Path to the django project
requirements_file          "{{ project_path }}/requirements.txt"                                                                                    Path to the pip requirements file of te project
superuser_name             superuser                                                                                                                Django superuser to create
superuser_email            superuser@example.com                                                                                                    Email of the django superuser
superuser_password         password                                                                                                                 Password of the django superuser
db_user                    "{{ application_name }}"                                                                                                 The user for database access
db_name                    "{{ application_name }}"                                                                                                 Name of the database
db_password                password                                                                                                                 Password for accessing the database
web_user                   "{{ application_name }}"                                                                                                 Username for the user running gunicorn
web_group                  webapps                                                                                                                  Groupname for the gunicorn user
nginx_static_dir           "{{ virtualenv_path }}/static/"                                                                                          Static files dir to be served via nginx
nginx_media_dir            "{{ virtualenv_path }}/media/"                                                                                           Media files dir to be served via nginx
django_settings_file       "config.settings.production"                                                                                             Path to the settings. Has to be importable.
django_wsgi_file           config.wsgi                                                                                                              Path to the wsgi file. Has to be importable.
django_secret_key          "akr2icmg1n8%z^3fe3c+)5d0(t^cy-2_25rrl35a7@!scna^1#"                                                                     Secret key for kryptography within django.
django_run_syncdb          false                                                                                                                    Run syncdb command. For older django versions.
django_run_db_migrations   yes                                                                                                                      Run migrate command. For django >= 1.7
django_run_collectstatic   yes                                                                                                                      Run the collectstatic django command.
django_email_host          ~                                                                                                                        Hostname of the email server
django_email_port          1025                                                                                                                     Port of the email server
django_email_host_user     ~                                                                                                                        Username for the email server
django_email_host_password ~                                                                                                                        Password for the email server
django_environment         | DJANGO_SETTINGS_MODULE: "{{ django_settings_file }}"                                                                   Dict with environmentvariables to set for django.
                           | DJANGO_SECRET_KEY: "{{ django_secret_key }}"
                           | MEDIA_ROOT: "{{ nginx_media_dir }}"
                           | STATIC_ROOT: "{{ nginx_static_dir }}"
                           | DATABASE_URL: "postgres://{{ db_user }}:{{ db_password}}@127.0.0.1:5432/{{ db_name }}"
                           | DJANGO_EMAIL_HOST: "{{ django_email_host|default(omit) }}"
                           | EMAIL_PORT: "{{ django_email_port}}"
                           | EMAIL_HOST_USER: "{{ django_email_host_user|default(omit) }}"
                           | EMAIL_HOST_PASSWORD: "{{ django_email_host_password|default(omit) }}"
                           | DJANGO_DEFAULT_FROM_EMAIL: "{{ application_name}} <noreply@{{ ansible_eth0.ipv4.address }}>"
                           | BROKER_URL: "{{ django_broker_url|default(omit) }}"
========================== ======================================================================================================================== ==================================================
