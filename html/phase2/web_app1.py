import web
from subprocess import Popen
import os
import getpass 
import sqlite3
import random
import hashlib
import xmlrpclib
import sys
from string import Template
#import requests
#import urllib2
#from ntlm import HTTPNtlmAuthHandler
#import httplib, urllib



urls = (
    '/','index',
    #'/(.*)', 'index'
    '/hauth','hauth'
)

app = web.application(urls, globals())

'''
class index:
    def GET(self,name):
        return "hello world!"
'''
'''
class index:        
    def GET(self, name):
        #i = web.input(times=1)
        #if not name: name = 'World'
        #print 'Hello,', name + '!'
        #web.header('Content-Type', 'text/html; charset=UTF-8')
        return 'aaaaa'        
'''

#harchucmd_list=["\"c:\Program Files (x86)\CA\SCM\hchu.exe\"","-b cscr501",
#             "-eh E:\w3school\html\phase2\harvest.eh"]

#hppo_list=["\"c:\Program Files (x86)\CA\SCM\hppolset.exe\"","-b cscr501",
#             "-eh E:\w3school\html\phase2\harvest.eh"]
#hppo_optfile="-fc -f e:\w3school\har_usr_op.txt"

harcmd_list=["\"c:\Program Files (x86)\CA\SCM\husrmgr.exe\"","-b cscr501",
             "-eh E:\w3school\html\phase2\harvest.eh","-cpw -ow"]

tmpcmd=' '
valid_user=getpass.getuser()

not_allowed="ohh No, You can\'t change other\'s harvest password"
har_username_not_found="ohh No, Your harvest account doesn't exist"
succeed="Succeed to change your harvest password!"
fail="Oh God!Fail to change your harvest password!"
op_fail="Oh God!Fail to uppdate the flag of forcechange!Please remember the temp password to login!"

file_root="e:\w3school"
mail_eml="e:\w3school\hpwd_change.eml"
har_mailbody="e:\w3school\har_mail_body"
send_mailpy="E:\w3school\sendmail.py"


def send_mail_har_usr(user, tmp_pwd):
    mail_tpl = mail_eml
    replace_tokens = {  'mail_to':user+'@arcserve.com',
                        'user':user,
                        'tmp_pwd':tmp_pwd,
                     }
    send_mail(mail_tpl, **replace_tokens)
    

def send_mail(mail_template,**replace_items):
    with open(mail_template,'r') as f:
        tmp_con = Template(f.read())
        msg = tmp_con.safe_substitute(**replace_items)  

    mail_f = open(har_mailbody,'w')
    mail_f.write(msg)
    mail_f.close()
    sendm_cmd="type %s | python %s" %(har_mailbody,send_mailpy)
    os.system(sendm_cmd)
    os.remove(har_mailbody)




def user_auth(auth_tag):
    salt_key = 'bldwebauth'
    ori_info, hash_info = auth_tag.split('/')
    user, dummy = ori_info.split('-', 1)
    valid_user = user
    hash_result = hashlib.md5(ori_info + salt_key + "\n").hexdigest()
    if hash_result == hash_info:
        valid_user=valid_user
        return  valid_user
    else:
        return "current user=%s" %user  


class hauth:       
    def GET(name):
        return "hello auth!"
    
    def POST(name):
        #return "hello auth post!"  
        iall = web.input()
        if iall.has_key("auth_tag"):
            auth_user=user_auth(iall.auth_tag)
            #return auth_user
            #name= iall.name
            #pwd= inputall.pwd
            pwd=random.randint(100000,999999)
            str_pwd=str(pwd)
            
            
            #newpwd='%s %s' %('-npw',str_pwd)
            conn = sqlite3.connect('E:\\w3school\\html\\phase2\\arc_har_user.db')
            cur=conn.cursor()
            cur.execute("select username,realname from arc_har_usres")
            #return cur.fetchall() #to show all of the records in db
            
            for row in cur:                     
                if row[1] == auth_user:
                    #usrname='%s %s' %('-ousr',row[0])
                    opt_file='%s\%s_update.txt' %(file_root,row[0])
                    rule_f = open(opt_file,'w')
                    rule_f.write(row[0])
                    rule_f.write("\t")
                    rule_f.write(str_pwd)
                    rule_f.write("\t\t\t\t\t")
                    resetcmd='%s %s' %(tmpcmd.join(harcmd_list),opt_file)
                    rule_f.close()                                      
                    #resetcmd='%s %s %s' %(tmpcmd.join(harcmd_list),usrname,newpwd)
                    #return resetcmd #for test
                    ret = os.system(resetcmd)
                    if ret == 0:
                        send_mail_har_usr(auth_user, str_pwd)
                        os.remove(path)
                        os.remove(opt_file)
                        return succeed
                    else:
                        return fail
                #else:
                 #   return message
            message='%s %s' %(har_username_not_found,auth_user)     
            return message
    
class index:  
    def GET(self, name):
        inputall =web.input(name=None,pwd=None)
        name= inputall.name
        pwd= inputall.pwd
        #print name ,pwd
        return "hello world get!"
    def POST(self,name):
        i = web.input()
        if i.has_key("auth_tag"):
            return i.auth_tag      
 
        env = web.ctx.env
        request_method = env['REQUEST_METHOD']  
        request_path = env['REQUEST_URI']
        request_username =  os.environ.get('USERNAME')
        user1 = "aaa"
        authtag = "bbb"                
        message='%s---%s---%s---%s---%s' %(request_method,request_path,request_username,user1,authtag)
        return message         
        
'''
        inputall =web.input(name=None,pwd=None)
        name= inputall.name
        pwd= inputall.pwd 
        
        usrname='%s %s' %('-ousr',name)
        newpwd='%s %s' %('-npw',pwd)
        conn = sqlite3.connect('E:\\w3school\\html\\phase2\\arc_har_user.db')
        cur=conn.cursor()
        cur.execute("select username,realname from arc_har_usres")
        #return cur.fetchall()
        cIP=request.META['REMOTE_ADDR']
        message='%s %s %s %s' %(not_allowed,name,winname,cIP)
        for row in cur:
            if row[0] == usrname:
                if row[1] == winname:
                    resetcmd='%s %s %s' %(tmpcmd.join(harcmd_list),usrname,newpwd)
                    ret = os.system(resetcmd)
                    if ret == 0:
                        return succeed
                    else:
                        return fail
                else:
                    return message
                    
        return message
'''

if __name__ == "__main__":
    app.run()