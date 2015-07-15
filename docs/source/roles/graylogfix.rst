==========
graylogfix
==========

Dependencies:

- f500.elasticsearch
- graylog2.graylog

This role fixes some parts of other third party roles.

The elasticsearch fix will be fixed in future versions, see `Github issue 11594 <https://github.com/elastic/elasticsearch/issues/11594>`_.

The graylog part uses a newer graylog repository and fixes the web defaults template. This is fixed in newer versions of the graylog role than 1.0 but at the time it was not published.
