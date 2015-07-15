=========
memcached
=========

Install memcached.

---------
Variables
---------

========================== ======================= ==================================================
Name                       Default                 Description
========================== ======================= ==================================================
update_apt_cache           true                    Update apt cache before installing packages
memcached_listen           127.0.0.1               the IP address to listen on
memcached_port             11211                   the port to listen on
memcached_user             nobody                  The user to start the daemon
memcached_max_memory_mb    64                      The memory cap.
memcached_max_connections  1024                    Maximum connections.
========================== ======================= ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
packages              Install the memcached package
memcached             For all tasks
service               Ensure the memcached service is running
===================== ==========================================================================

