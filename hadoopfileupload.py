#!/usr/bin/python2

import cgi
import commands,time

print  "content-type:text/html"
print  ""

page=cgi.FieldStorage()
filelocation=page.getvalue('fileaddress')
commands.getoutput("sudo hadoop fs -mkdir /user")
commands.getoutput("sudo hadoop dfsadmin -setSpaceQuota 600M /user")
time.sleep(2)

commands.getoutput("sudo hadoop fs -put "+filelocation+"  hdfs://172.17.0.2:10005/user/")

time.sleep(2)

print "File Uploaded Successfully" 
