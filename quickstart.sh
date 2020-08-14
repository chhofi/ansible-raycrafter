#!/bin/bash

#quickstarts setting up

ansible-galaxy install -r requirements.yml -p ./roles
vagrant up
