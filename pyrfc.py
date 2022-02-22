#!/usr/bin/env python3

from urllib.request import urlopen
import sys, os
import readline

def logo():
    logo = """
    d8888b. db    db d8888b. d88888b  .o88b.
    88  `8D `8b  d8' 88  `8D 88'     d8P  Y8
    88oodD'  `8bd8'  88oobY' 88ooo   8P
    88~~~      88    88`8b   88~~~   8b
    88         88    88 `88. 88      Y8b  d8
    88         YP    88   YD YP       `Y88P'

        type 'quit' to exit, 'help' to display the help
"""
    print(logo)

########################################
#Displays the rfc number [num] with 'less' command
def less_rfc(num):
    os.system(f"less PYRFC/rfc_{num}")

#########################################
def back():
    input('PYRFC ~ press enter to return ')

##########################################
#Builds the pyrfc folder if isn't exists, and makes the rfc file from 'rfcc' data
def make(rfcc, num, read):
    if not os.path.exists("PYRFC"):
        os.mkdir("PYRFC")
    with open(f"PYRFC/rfc_{num}", "w") as rff:
        rff.write(rfcc)
    rff.close()

    print(f"PYRFC mes ~ rfc_{num} successfully downloaded !")

    if read:
        less_rfc(num)

    back()

##########################################
#Download & displays the rfc number [num]
def pyrfc(num, read=False):
    try:
        url=f"http://www.ietf.org/rfc/rfc{num}.txt"
        rfcf=urlopen(url).read().decode()
        make(rfcf, num, read)
    except Exception as e:
        print(e)
        print("PYRFC err ~ faild, check your internet connection !")
        back()

#########################################
#Displays the rfc number [num] if exists
def read(num):
    if not os.path.exists(f"PYRFC/rfc_{num}"):
        print(f"PYRFC err ~ rfc {num} isn't exists !")
        d = input("PYRFC que ~ do you want to download it? [y/n] ~ ").upper()
        if d == "Y":
            pyrfc(num, read=True)
    else:
        less_rfc(num)

##########################################
def _help():
    os.system("less help")

###########################################
#Check & Runs the user command from command-line args
def argcheck(args):
    validcommand = args[1]

    if validcommand == "-r":
        read(args[2]) if len(args)>2 else print('PYRFC err ~ the rfc number not found !')
    elif validcommand == "-d":
        pyrfc(args[2]) if len(args)>2 else print('PYRFC err ~ the rfc number not found !')
    elif validcommand == "-dr":
        pyrfc(args[2], read=True) if len(args)>2 else print('PYRFC err ~ the rfc number not found !')
    else:
        _help()

##########################################
#Check & Runs the user command
def comcheck(com):
    validcommand = com[0]

    if validcommand == "read":
        read(com[1])
    elif validcommand == "downld":
        pyrfc(com[1])
    elif validcommand == "dowar":
        pyrfc(com[1], read=True)
    elif validcommand == "help":
        _help()
    elif validcommand == "quit":
        sys.exit()
    else:
        print(f"PYRFC err ~ '{validcommand}' command not found !")
        back()
        env()

###########################################
#Runs in PYRFC environment
def env():
    while True:
        os.system("clear")
        logo()
        pyrf=input("PYRFC X ").split(" ")
        comcheck(pyrf)

############################################
def main():
    args = sys.argv
    try:
        argcheck(args) if len(args) > 2  else env()
    except:
        if len(args) != 1:
            _help()

if __name__ == "__main__":
    main()
