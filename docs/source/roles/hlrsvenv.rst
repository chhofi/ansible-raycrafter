========
hlrsvenv
========

Download python packages locally and install them in a virtualenv at the cluster.

---------
Variables
---------

======================== ======================================= ==================================================
Name                     Default                                 Description
======================== ======================================= ==================================================
hlrsvenv_localpip3       pip3                                    The pip executable on the local machine to
                                                                 download the python packages.
                                                                 Should be for python3.
hlrsvenv_pypackages      []                                      List of python packages to install.
hlrsvenv_pythonversion   3.4.1                                   The python version to use.
hlrsvenv_pythonmodule    tools/python/{{hlrsvenv_pythonversion}} The module name of python to load.
hlrsvenv_virtualenvpath  .virtualenv                             The path in $HOME for the venv.
======================== ======================================= ==================================================

----
Tags
----
===================== ==========================================================================
Name                  Description
===================== ==========================================================================
packages              Install packages
===================== ==========================================================================
