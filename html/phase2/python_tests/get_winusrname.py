import getpass 
import sqlite3
import random
import web
from string import Template
import os

#hppo_optfile="e:\w3school\har_usr_op.txt"
tmpcmd=' '
tab_list='\t\t\t\t\t'
mail_eml="e:\w3school\hpwd_change.eml"
har_mailbody="e:\w3school\har_mail_body"
send_mailpy="E:\w3school\sendmail.py"

not_allowed="ohh No, You can\'t change other\'s harvest password"
succeed="Succeed to change your harvest password!"
fail="Oh God!Fail to change your harvest password!"
op_fail="Oh God!Fail to uppdate the flag of forcechange!Please remember the temp password to login!"

harcmd_list=["\"c:\Program Files (x86)\CA\SCM\husrmgr.exe\"","-b cscr501",
             "-eh E:\w3school\html\phase2\harvest.eh","-cpw -ow"]
file_root="e:\w3school"


'''
tem_usern='chebe09'
winname=getpass.getuser()
print winname;
conn = sqlite3.connect('E:\\w3school\\html\\phase2\\arc_har_user.db')
cur=conn.cursor()
cur.execute("select username,realname from arc_har_usres")
for row in cur:
    #print '%s    %s' %(row[0],row[1])
    if row[0] == tem_usern:
        if row[1] == winname:
            print '%s    %s' %(row[0],row[1])
            print ("Yeah, You can change your own harvest password")
        else:
            print '%s    %s' %(row[0],row[1])
            print ("ohh No, You can't change other's harvest password")

#print(c.fetchall())
'''
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
    
pwd=random.randint(100000,999999)
str_pwd=str(pwd)
#str_p='123456'
#send_mail_har_usr('cliicy.luo',str_pwd )
conn = sqlite3.connect('E:\\w3school\\html\\phase2\\arc_har_user.db')
cur=conn.cursor()
cur.execute("select username,realname from arc_har_usres")

for row in cur:
    #print '%s****%s' %(row[0],row[1])
    #print row[0]
    if row[1] == 'buildtest':
        opt_file='%s\%s_update.txt' %(file_root,row[0])
        rule_f = open(opt_file,'w')
        #rule_f.write('%s\t%s%s' %(row[1],'abcd01',tab_list))
        rule_f.write(row[0])
        rule_f.write("\t")
        rule_f.write(str_pwd)
        rule_f.write("\t\t\t\t\t")
        resetcmd='%s %s' %(tmpcmd.join(harcmd_list),opt_file)
        rule_f.close()
        ret = os.system(resetcmd)
        #print resetcmd
        print ret

'''
iall = web.input()
if iall.has_key("auth_tag"):
    auth_user=user_auth(iall.auth_tag)
    #name= iall.name
    #pwd= inputall.pwd
    pwd=random.randint(100000,999999)
    str_pwd=str(pwd)
    
    usrname='%s %s' %('-ousr',auth_user)
    newpwd='%s %s' %('-npw',str_pwd)
    conn = sqlite3.connect('E:\\w3school\\html\\phase2\\arc_har_user.db')
    cur=conn.cursor()
    cur.execute("select username,realname from arc_har_usres")
    message='%s %s' %(not_allowed,auth_user)
    for row in cur:
        if row[0] == usrname:
            if row[1] == auth_user:
                resetcmd='%s %s %s' %(tmpcmd.join(harcmd_list),usrname,newpwd)
                print resetcmd
                #ret = os.system(resetcmd)
                #if ret == 0:
                #    send_mail_har_usr(auth_user, str_pwd)
                #    return succeed
                    #3chgNLog_cmd='%s %s' %(tmpcmd.join(hppo_list),hppo_optfile)
                    #oret = os.system(chgNLog_cmd)
                    #if oret == 0:
                        #return succeed
                    #else:
                     #   return op_fail
                #else:
                #    return fail
            #else:
            #    return message               
    #return message
'''