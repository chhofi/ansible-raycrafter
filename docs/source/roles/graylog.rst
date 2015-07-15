=======
Graylog
=======

Dependencies:

- graylog2.graylog

Configure the Graylog server/web-interface via the REST API. You can create inputs or whole
contentpacks.

---------
Variables
---------

================================= ======================= ==========================================================================
Name                              Default                 Description
================================= ======================= ==========================================================================
graylog_rest_host                 127.0.0.1               The host of the REST API
graylog_rest_port                 12900                   The port of the REST API
graylog_root_password_unencrypted admin                   The password of http auth
graylog_inputs                    {}                      A dict with configuration parameters for inputs.
                                                          Keys are the names of the input.
                                                          If the name exists, do not create input.
                                                          Values are dicts with keys:
                                                          type, node, configuration
                                                          Type is the input type. Node the node id.
                                                          Without a node it, create a global input.
                                                          Configuration is the config dict for the node type
                                                          and depends on each type. Check the rest api doc
                                                          of graylog.
graylog_contentpacks:             []                      List of json configurations. Gets directly submitted via rest.
                                                          Best to use like:
                                                          ``"{{lookup('file', playbook_dir + '/files/contentpacks/<name>.json')}}"``
================================= ======================= ==========================================================================

----
Tags
----

===================== ==========================================================================
Name                  Description
===================== ==========================================================================
graylog               For all tasks
===================== ==========================================================================
