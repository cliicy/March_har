from subprocess import Popen
import os

harcmd_list=["\"c:\Program Files (x86)\CA\SCM\hchu.exe\"","-b cscr501",
             "-eh E:\w3school\html\phase2\harvest.eh"]
tmpcmd=' '



name= "chebe09"
pwd= "abcd21"
usrname='%s %s' %('-ousr',name)
newpwd='%s %s' %('-npw',pwd)   
resetcmd='%s %s %s' %(tmpcmd.join(harcmd_list),usrname,newpwd)
print resetcmd
#p=Popen(resetcmd)
val=os.system(resetcmd)
print val

