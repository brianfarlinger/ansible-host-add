#!/bin/python
from pick import pick

hostname = raw_input("What is the FQDN of this server?:")
title = 'Please pick the best category which defines this server'
options = ["kvm", "management", "web", "db", "kvm", "other"]
option, index = pick(options, title)
filepath = "/home/brian/ansible/test"
