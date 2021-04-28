#!/usr/bin/python3

import os
import subprocess
import sys


class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

print(bcolors.YELLOW)
banner = """
 ______   ___   ___   ______   ______   _________  ______   ______       
/_____/\ /__/\ /__/\ /_____/\ /_____/\ /________/\/_____/\ /_____/\      
\:::__\/ \::\ .:  \ .\::::_\/_\::::_\/_\__.::.__\/\::::_\/_\:::_ \ \     
 \:\ \  __\::\/_\ .\ .\:\/___/.\:\/___/\  \::\ \   \:\/___/.\:(_) ) )_   
  \:\ \/_/.\:: ___::\ .\::___\/_\::___\/_  \::\ \   \::___\/_\: __ `\ \  
   \:\_\ \ .\: \  \::\ .\:\____/.\:\____/\  \::\ \   \:\____/.\ \ `\ \ \ 
    \_____\/ \__\/ \::\/ \_____\/ \_____\/   \__\/    \_____\/ \_\/ \_\/ 
----------------------------------------------------------------------------                                                                         
"""
banner2 = """
        _,',             _.-''``-...___..--';)
       /_ /'.      __..-' ,      ,--...--'''
      <\    .`--'''       `     /'
       `-';'               ;   ; ;
 __...--''     ___...--_..'  .;.'
(,__....----'''       (,..--''   
------------------------------------------------------------------------------
"""
print(banner2)
print(banner)
print(bcolors.ENDC)

def arg_check():
    if len(sys.argv) != 2:
        message  = "[!]Need More Args!!!!"
        message2 = f"Usage: {sys.argv[0]} <path of cheefsheet_file>"
        message3 = f"Example: {sys.argv[0]} ~/cheatsheets/cheatsheet.txt"
        max_length = len(message3)
        padding = max_length - len(message)
        padding2 = max_length - len(message2)    

        hatch = "+"+"-"*max_length+"+"
        print(bcolors.RED)
        print(hatch)
        print("|"+message+" "*padding+"|")
        print("|"+message2+" "*padding2+"|")
        print("|"+message3+"|")
        print(hatch)
        print(bcolors.ENDC)

        del message,message2,message3,max_length,padding,padding2,hatch

        sys.exit()

def file_load():
    
    try:

        file_path = sys.argv[1]
        print(bcolors.BLUE)
        print(f"successfuly load: {file_path}")
        print(bcolors.ENDC)
        return file_path

    except:
        print(bcolors.RED)
        print(f"Failed to load: {file_path}")
        print(bcolors.ENDC)
        sys.exit()

    return file_path

def info_proc():
    
    print(bcolors.GREEN)
    print("Enter Some Info: lhost lport rhost rport")
    prompt = "> "
    print("[+]Enter Lhost")
    lhost = input(prompt)
    print("[+]Enter Lport ")
    lport = input(prompt)
    print("[+]Enter Rhost")
    rhost = input(prompt)
    print("[+]Enter Rport")
    rport = input(prompt)

    print(bcolors.ENDC)
    return lhost,lport,rhost,rport

def libra(file_path,lhost,lport,rhost,rport):

    prompt = "> "
    print(f"LoadFile: {file_path}")

    while True:
        print(bcolors.YELLOW)
        print("Enter the Keyword")
        print("+-----------------------------------+")
        print("|Enter The Any KeyWord like a \"john\"|")
        print("|\"exit\"  => quit this program       |")
        print("|\"reset\" => reset the info          |")
        print("|\"info\"  => show info               |")
        print("|\"all\"   => show all                |")
        print("+-----------------------------------+")
        cmd = input(prompt)
        f = open(file_path,"r")
        print(bcolors.BLUE)
        
        for i in f:
        
            if cmd in i:
                i = i.replace("{lhost}",lhost)
                i = i.replace("{lport}",lport)
                i = i.replace("{rhost}",rhost)
                i = i.replace("{rport}",rport)
                print(i)                

        if cmd == "exit":
            print(bcolors.RED)
            print("[!]Quit")
            print(bcolors.ENDC)
            sys.exit()
       
        if cmd == "info":
            
            print(bcolors.RED)

            print("[+]Currently Setting \n")
            
            print(f"LHOST => {lhost}")
            print(f"LPORT => {lport}")
            print(f"RHOST => {rhost}")
            print(f"RPORT => {rport}\n")
            
            print("\"reset\": reset the info")    

            print(bcolors.ENDC)

        if cmd == "all":

            f = open(file_path,"r")
            for i in f:
                i = i.replace("{lhost}",lhost)
                i = i.replace("{lport}",lport)
                i = i.replace("{rhost}",rhost)
                i = i.replace("{rport}",rport)
                print(i)


        if cmd == "reset":
            
            break

if __name__ == "__main__":

    arg_check()
    file_path = file_load()
    while True:
        lhost,lport,rhost,rport = info_proc()
        ope = libra(file_path,lhost,lport,rhost,rport)
        
