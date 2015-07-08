#!/usr/bin/python
import base64
import httplib
import json


DOCUMENTATION = '''
---
module: grayloginputs
short_description: Adds inputs to graylog
description:
  - Adds an input to graylog if one with the same title does not yet exist
options:
  title:
    description:
      - The input name. If an input with the same name already exists, nothing will be changed. Graylog supports multiple inputs with the same name but you cannot know the ids beforehand.
    required: true
  configuration:
    description:
      - Another dictionary of configuration values. These are the values you also see in the graylog web interface under /system/inputs. The available options can be found by requesting /system/inputs/types/{inputtype} via the rest api.
    required: true
  node:
    description:
      - If present, create the input only on that node. If null, create a global input.
    required: false
    default: ''
  type:
    description:
      - Input type. A list of available inputs can be found by requesting /system/inputs/types via the rest api.
    required: true
  user:
    description:
     - The username for authentication.
    required: true
  password:
    description:
      - The password for authentication.
    required: true
  host:
    description:
      - the IP of the graylog web server.
    required: false
    default: "127.0.0.1"
  port:
    description:
      - the port of the graylog web server.
    required: false
    default: 12900
  timeout:
    description:
      - the timeout for the api requests.
    required: false
    default: 10
author: "David Zuber (zuber.david@gmx.de)"
'''

EXAMPLES = '''
# Create global gelf udp input node
- grayloginputs:
    title: myinput
    host: "127.0.0.1"
    port: 12900
    configuration:
       port: 12201
       bind_address: 0.0.0.0
    type: 'org.graylog2.inputs.gelf.udp.GELFUDPInput'
    node: ''
    user: 'admin'
    password: 'admin'

# Create input nodes based on a variable
# Assert you have a variables file with following config:
#graylog_inputs:
#  myinput1:
#    node: ''
#    type: org.graylog2.inputs.gelf.udp.GELFUDPInput
#    configuration:
#      bind_address: '0.0.0.0'
#      port: 12201
#  myinput2:
#    node: ''
#    type: org.graylog2.inputs.gelf.udp.GELFUDPInput
#    configuration:
#      bind_address: '0.0.0.0'
#      port: 12202
- grayloginputs:
    title: "{{item}}"
    host: "127.0.0.1"
    configuration: "{{graylog_inputs[item]['configuration']}}"
    user: 'admin'
    password: 'admin'
    type: "{{graylog_inputs[item]['type']}}"
    node: "{{graylog_inputs[item]['node']}}"
  with_items: graylog_inputs.keys()
'''

RETURN = '''
title:
    description: The title of the created input
    returned: success
    type: string
    sample: "myinput"
inputid:
    description: The id of the created input
    returned: success
    type: string
    sample: 124afedec349779a
status:
    description: the response status code of the rest api request
    returned: failure
    type: integer
    sample: 404
reason:
    description: The reason for the response
    returned: failure
    type: string
    sample: "Not found!"
sentbody:
    description: The body sent when creating the input in the post request.
    returned: failure, when failing at creating the input (not checking if it exists).
    type: string
    sample: {title:myinput,type:org.graylog2.inputs.gelf.udp.GELFUDPInput}
'''

HEADERS = {'Content-type': 'application/json'}
APIENDPOINT = '/system/inputs'


def check_exists(module, conn):
    conn.request('GET', APIENDPOINT, headers=HEADERS)
    r = conn.getresponse()
    if r.status != 200:
        module.fail_json(msg="Failed to check inputs", status=r.status, reason=r.reason)
    data = r.read()
    js = json.loads(data)
    for inp in js['inputs']:
        title = inp['message_input']['title']
        if title == module.params['title']:
            module.exit_json(changed=False, title=title, inputid=None)


def create_input(module, conn):
    p = module.params
    isglobal = not bool(p['node'])
    data = {'title': p['title'],
            'configuration': p['configuration'],
            'global': isglobal,
            'node': p['node'],
            'type': p['type'],
            }
    js = json.dumps(data)
    conn.request('POST', APIENDPOINT, headers=HEADERS, body=js)
    r = conn.getresponse()
    if r.status != 201:
        module.fail_json(msg='Failed to create input', status=r.status, reason=r.reason, sentbody=data)
    return inputid


def main():
    module = AnsibleModule(
    argument_spec = dict(
        title     = dict(required=True),
        configuration = dict(required=True),
        node      = dict(default=''),
        type      = dict(required=True),
        user      = dict(required=True),
        password  = dict(required=True),
        host      = dict(default='127.0.0.1'),
        port      = dict(default=12900),
        timeout   = dict(default=10),
    ),
    supports_check_mode=True
    )
    host = module.params['host']
    port = module.params['port']
    authstring = '%s:%s' % (module.params['user'], module.params['password'])
    auth = base64.encodestring(authstring).replace('\n', '')
    HEADERS['Authorization'] = 'Basic %s' % auth

    conn = httplib.HTTPConnection(host, port)
    check_exists(module, conn)
    if module.check_mode:
        module.exit_json(changed=True)
    inputid = create_input(module, conn)
    module.exit_json(changed=True, title=module.params['title'], inputid=inputid)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
