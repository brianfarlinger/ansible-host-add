#!/bin/python
import configparser

#Define your hostname and server. 
hostname = "web1"
server_types = {webservers, virtualservers)

#Read the ansible host config file - which uses ini format by default.
config = configparser.ConfigParser()
config.read('/etc/ansible/hosts')

add_host(hostname, servertypes)

def add_host(hostname, list_of_server_types):
  for server_type in list_of_server_types:
    if (server_type in config):
      config.set(server_type, hostname, "")
    else:
      do nothing
  config.write(open("/etc/ansible/hosts', w))
