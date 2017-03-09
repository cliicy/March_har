import cgi
form = cgi.FieldStorage();
name = form.getValue('h_usrname');
pwd = form.getValue('h_password');
print "Content-Type: text/html; charset=utf-8\n\n";

#class usr_pwd_chg:        
#     def POST(self, name):
#        inputall =web.input(name=None,pwd=None)
#        name= inputall.name
#        pwd= inputall.pwd
#        print print name ,pwd