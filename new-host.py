#!/bin/python
from pick import pick
import sys, paramiko

#this script should live on the server that provisions new machines

#defining the VM
hostname = raw_input("What is the FQDN of this server?:")
title = 'Please pick the best category which defines this server'
options = ["kvm", "management", "web", "db", "kvm", "other"]
option, index = pick(options, title)
filepath = "/home/brian/ansible/test"

#using paramiko to connect to ansible server and update the hosts file
host = 'ansible.lilac.red'
port = 22
restricted_key = '~/.ssh/restricted_key'

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=user, key_filename=restricted_key)

command = 'python /home/ansible/scripts/add-host.py %s %s' % (hostname, option)
stdin, stdout, stderr = client.exec_command(command)

if not stderr.readlines():
    return stdout.readlines()
else:
    raise IOError
