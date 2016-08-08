#!/bin/python

#place this file on the ansible server. I put it in /home/ansible/scripts/
from pick import pick

#defining variables
filepath = "/etc/ansible/hosts"

#the hostname and option variable will come from the server which remotely runs this script using paramiko. 

#writing to the file
with open(filepath, "r") as in_file:
        buf = in_file.readlines()

with open(filepath, "w") as out_file:
        for line in buf:
                if line == "[" + option + "]\n":
                        line = line + hostname + "\n"
                        print "Success! A line has been written to " + filepath
                out_file.write(line)
