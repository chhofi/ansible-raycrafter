==========
supervisor
==========

Install supervisor, ensure supervisor is running.

Handlers:

- Restart Supervisor programs
  Append to supervisor_restart_programms if you want to restart another programm.
  This can be done dynamically in a task.
- Supervisor update
- Supervisor reread

---------
Variables
---------

============================= ======================= ==================================================
Name                          Default                 Description
============================= ======================= ==================================================
update_apt_cache              true                    Update apt cache before installing packages
supervisor_restart_programms  []                      Append to this list to register programms
                                                      for restart
============================= ======================= ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
supervisor            For all tasks
packages              Install supervisor package
service               Ensure supervisor service is started
===================== ==========================================================================

