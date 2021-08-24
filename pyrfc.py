from urllib.request import urlopen
import sys, os
import readline
from time import sleep

def logo():
    logo = """
    d8888b. db    db d8888b. d88888b  .o88b. 
    88  `8D `8b  d8' 88  `8D 88'     d8P  Y8 
    88oodD'  `8bd8'  88oobY' 88ooo   8P      
    88~~~      88    88`8b   88~~~   8b      
    88         88    88 `88. 88      Y8b  d8 
    88         YP    88   YD YP       `Y88P'
"""
    print(logo)

def less(num):
    os.system(f"less pyrfc/rfc_{num}")

##########################################
def make(rfcc, num, read):
    if not os.path.exists("pyrfc"):
        os.mkdir("pyrfc")
    with open(f"pyrfc/rfc_{num}", "w") as rff:
        rff.write(rfcc)
    rff.close()

    print(f"pyrfc s ~ rfc_{num} ok")

    if read:
        less(num)

##########################################
def pyrfc(num, read=False):
    try:
        url=f"http://www.ietf.org/rfc/rfc{num}.txt"
        rfcf=urlopen(url).read().decode()
        make(rfcf, num, read)
    except:
        print("pyrfc e ~ faild, check your internet connection")

#########################################        
def read(num):
    if not os.path.exists(f"pyrfc/rfc_{num}"):
        print(f"pyrfc e ~ rfc {num} is not exists")
        d = input("pyrfc q ~ do you want to download [y/n] ~ ").upper()
        if d == "Y":    
            pyrfc(num, read=True)
    else:
        less(num)
 
##########################################
def _help():
    os.system("less help")

###########################################
def check(args):
    if args[1] == "-d":
        num = args[2]
        pyrfc(num)
    elif args[1] == "-dr":
        pyrfc(args[2], read=True)
    elif args[1] == "-r":
        read(args[2])
    else:
        _help()

##########################################

commands = ["read", "downld", "dar", "quit", "help"]


def comcheck(com):
    if "read" in com:
        read(com[1])
    elif "downld" in com:
        pyrfc(com[1])
    elif "dar" in com:
        pyrfc(com[1], read=True)
    elif "help" in com:
        _help()
    elif "quit" in com:
        exit()
    else:
        print("pyrfc e ~ command not found !")
        sleep(1)
        env()

#########################################
def env():
    while True:
        os.system("clear")
        logo()
        pyrf=input("pyrfc   ").split(" ")
        comcheck(pyrf)        
############################################

def run():
    args = sys.argv
    check(args) if len(args) > 2  else env()
run()
