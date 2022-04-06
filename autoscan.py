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
[1] advanced nmap scan with nmap 
[2] directory hunter with gobuster
[3] admin login hunter with gobuster
[4] check vulns with nikto 
[5] check vulns with skipfish
[6] find subdomains with subfinder
[7] find info about target with whois 
[8] find exploits with searchsploit

// SQLMAP 

[9] sqli with sqlmap 
[10] dbs, --tables
[11] dbs, tables, --dump
[12] sql with sqlmap (advanced mode) 

""")
at = input("number => ")
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
if at == "9":
   atsq1 = input("url => ")
   call(["sqlmap", atsq1 ,"--dbs", "--random-agent"])
   print(Fore.RED + '[URL]' + atsq1)
if at == "10" :
   atsq3 = input("url => ")
   atdbn = input("database name => ") 
   call(["sqlmap", atsq3 ,"-D", atdbn, "--tables", "--random-agent"])
   print(Fore.RED + '[URL]', atsq3 + '\n' + '[DBS]', atdbn)
if at == "11" :
   atsq4 = input("url => ")
   atdbn2 = input("database name => ") 
   attb = input("table name => ") 
   call(["sqlmap", atsq4,"-D", atdbn2, "-T", attb, "--dump", "--random-agent"])
   print(Fore.RED + '[URL]', atsq4 + '\n' + '[DBS]', atdbn2 + '\n' + '[TAB]', attb)
if at == "12" :
   atsq2 = input("url =>")
   call(["sqlmap", atsq2 ,"--tamper=space2comment,between,space2plus", "-v 2", "--hex", "--random-agent", "--skip-waf", "--risk=3", "--level=3"])
