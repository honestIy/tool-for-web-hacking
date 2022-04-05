import os
import colorama
from subprocess import call
from colorama import Fore, Style

print(Fore.YELLOW +"""   
                      88              
                      ""              
                                      
8b,dPPYba, ,adPPYYba, 88 8b,dPPYba,   
88P'   "Y8 ""     `Y8 88 88P'   `"8a  
88         ,adPPPPP88 88 88       88  
88         88,    ,88 88 88       88  
88         `"8bbdP"Y8 88 88       88  
""")

print(Fore.GREEN +"""
[1] advanced scan scan with nmap 
[2] directory hunter with gobuster
[3] check vulns with nikto 
[4] check vulns with skipfish
[5] find subdomains with subfinder
[6] whois scanner 

// SQLMAP 

[7] sqli with sqlmap 
[8] dbs, --tables
[9] dbs, tables, --dump
[10] sql with sqlmap (advanced mode) 

""")
at = input("number => ")
if at == "1" :
   atnmap = input("ip or url => ") 
   os.system("sudo nmap -sV -O -Pn -sS " + atnmap + "")
if at == "2" : 
   at3 = input("url => ")
   atdir = input("wordlist dir => ")
   os.system("gobuster dir -u " + at3 + " -w " + atdir + "") 
if at == "3" :
   atnikto = input("link => ") 
   os.system("nikto -h " + atnikto + "")
if at == "4" :
    atskipfish = input("url => ")
    os.system("skipfish -o fstscan " + atskipfish + "")
if at == "5" :
    atsubfinder = input("url => ")
    os.system("subfinder -d " + atsubfinder + "")
if at == "6" :
   atwhois = input ("domain => ")
   os.system("whois " + atwhois + "")
if at == "7":
   atsq1 = input("url => ")
   call(["sqlmap", atsq1 ,"--dbs", "--random-agent"])
if at == "8" :
   atsq3 = input("url => ")
   atdbn = input("database name => ") 
   call(["sqlmap", atsq3 ,"-D", atdbn, "--tables", "--random-agent"])
if at == "9" :
   atsq4 = input("url => ")
   atdbn2 = input("database name => ") 
   attb = input("table name => ") 
   call(["sqlmap", atsq4,"-D", atdbn2, "-T", attb, "--dump", "--random-agent"])
if at == "10" :
   atsq2 = input("url =>")
   call(["sqlmap", atsq2 ,"--tamper=space2comment,between,space2plus", "-v 2", "--hex", "--random-agent", "--skip-waf", "--risk=3", "--level=3"])
else : 
   print("something went wrong ")
