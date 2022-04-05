import os
import colorama
from colorama import Fore, Style

os.system("clear")

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
[3] check dbs with sqlmap 
[4] check dbs with sqlmap advanced mode 
[5] check vulns with nikto 
[6] check vulns with skipfish
[7] find subdomains with subfinder 
""")
at = input("number => ")
if at == "1" :
   atnmap = input("ip or url => ") 
   os.system("sudo nmap -sV -O -Pn -sS " + atnmap + "")
if at == "2" : 
   at3 = input("url => ")
   atdir = input("wordlist dir => ")
   os.system("gobuster dir -u " + at3 + " -w " + atdir + "") 
if at == "3":
   atsql = input("url => ")
   os.system("sqlmap -u"+ atsql +"--dbs --random-agent")
if at == "4" :
   atsqla = input("url =>")
   os.system("sqlmap -u " + atsqla + "--tamper=space2comment,between,space2plus -v 2 --hex --random-agent --skip-waf --risk=3 --level=3 --dbs")
if at == "5" :
   atnikto = input("link => ") 
   os.system("nikto -h " + atnikto + "")
if at == "6" :
    atskipfish = input("link => ")
    os.system("skipfish -o fstscan " + atskipfish + "")
if at == "7" :
    atsubfinder = input("link => ")
    os.system("subfinder -d " + atsubfinder + "")
else : 
  print("something went wrong ")
