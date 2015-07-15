===
db
===

Install PostgreSQL and ensure the service is running. Create a PostgreSQL database.

---------
Variables
---------

===================== ======================= ==================================================
Name                  Default                 Description
===================== ======================= ==================================================
db_name               "mydb"                  Name of the PostgreSQL database
db_password           "password"              Password of db_user
db_user               "dbuser"                PostgreSQL user name.
===================== ======================= ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
packages              Install the PostgreSQL package
service               Make sure PostgreSQL is started and enabled
postgres              Tag for all tasks
===================== ==========================================================================

