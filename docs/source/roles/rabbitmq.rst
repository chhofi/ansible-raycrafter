========
rabbitmq
========

Install rabbitmq, setup vhost and rabbitmq users. Ensure that the service is runnning.

---------
Variables
---------

============================== ========================== ==================================================
Name                           Default                    Description
============================== ========================== ==================================================
update_apt_cache               true                       Update apt cache before installing packages
rabbitmq_admin_user            admin
rabbitmq_admin_password        password
rabbitmq_application_vhost     rabbitmqvshost
rabbitmq_application_user      rabbitmq
rabbitmq_application_password  password
============================== ========================== ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
packages              Install the RabbitMQ package
service               Ensure RabbtiMQ is running
===================== ==========================================================================
