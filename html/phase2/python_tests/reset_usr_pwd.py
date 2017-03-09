#!/usr/bin/env python
from subprocess import Popen
#import web

#class index:        
#    def GET(self, name):
#        inputall =web.input(name=None,pwd=None)
#        name= inputall.name
#        pwd= inputall.pwd
#        print print name ,pwd
#    def POST(self, name):
#        inputall =web.input(name=None,pwd=None)
#        name= inputall.name
#        pwd= inputall.pwd
#        print print name ,pwd


cmd='"c:\Program Files (x86)\CA\SCM\hchu.exe" -b cscr501 -ousr chebe09 -npw h121 -eh  harvest.eh'
p = Popen(cmd)
print (p)