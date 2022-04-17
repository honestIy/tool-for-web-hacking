import os
import time
import sys
from subprocess import call
from colorama import Fore, Style

os.system("clear")

def menu():
      print(f'''{Fore.LIGHTRED_EX}
      _       ____________  __  _____   ________ __ _____   ________
     | |     / / ____/ __ )/ / / /   | / ____/ //_//  _/ | / / ____/
     | | /| / / __/ / __  / /_/ / /| |/ /   / ,<   / //  |/ / / __  
     | |/ |/ / /___/ /_/ / __  / ___ / /___/ /| |_/ // /|  / /_/ /  
     |__/|__/_____/_____/_/ /_/_/  |_\____/_/ |_/___/_/ |_/\____/   
    {Fore.LIGHTYELLOW_EX}
    type{Fore.GREEN} start {Fore.LIGHTYELLOW_EX}to begin your scan 

''')
menu()

def start():
        print(f'''
{Fore.RED}  
     [!]{Fore.LIGHTYELLOW_EX}  CHOOSE A NUMBER FROM 1 THROUGH 4 TO START YOUR SCAN!
{Fore.CYAN}                            
     [1] recon phase         [2] info gathering        [3] analysis phase                                      
{Fore.LIGHTYELLOW_EX}      
     [-] whois               [-] theHarvester          [-] nikto
     [-] nslookup            [-] dirsearch             [-] nmap vuln
     [-] dig                 [-] dirb                   
     [-] dnsrecon            [-] amass
     [-] fierce              [-] whatweb
     [-] traceroute          [-] nmap port 
''')

s = input(f"     {Fore.GREEN}=> ")

if s == "start":
    start()

loop = True

while loop:
    option = input(f'''{Fore.LIGHTYELLOW_EX}    (pentester/{Fore.CYAN}menu{Fore.LIGHTYELLOW_EX}){Fore.GREEN} => ''')
    if option == "1":

        os.system("clear")

        print(f'''{Fore.WHITE}
RECON
      PHASE 
.----.______ FOLDER
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/

{Fore.RED} [!] {Fore.LIGHTYELLOW_EX} TYPE THE TARGET {Fore.RED}DOMAIN{Fore.LIGHTYELLOW_EX} BELOW''')
        print(Fore.WHITE+"------------------------------------")

        d1 = input(Fore.RED +f'''{Fore.LIGHTYELLOW_EX}(pentester/menu/{Fore.CYAN}reconphase{Fore.LIGHTYELLOW_EX}){Fore.GREEN} => '''+ Fore.GREEN)

        #os.system("mkdir websites/"+ d1 +"")

        #sys.stdout = open("websites/"+d1+"/" + d1 + '.txt', 'w')

        print(Fore.CYAN +'''

starting WHOIS...
            
        '''+ Fore.GREEN)

        os.system("whois " + d1 +"")

        print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''
            
starting NSLOOKUP...
            
            '''+ Fore.GREEN)

            os.system("nslookup " + d1 +"")

            print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''
            
starting DIG...
                
            '''+ Fore.GREEN)

            os.system("dig " + d1 +"")

            print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''
            
starting DNSRECON...
            
            '''+ Fore.GREEN)

            os.system("python dnsrecon/dnsrecon.py -d " + d1 + "")

            print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(f'\n')

            print(Fore.CYAN +'''
            
starting FIERCE...
            
            '''+ Fore.GREEN)

            os.system("fierce --domain " + d1 +"")

            print(f'\n')


        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''

starting TRACEROUTE...
            
            '''+ Fore.GREEN)

            os.system("traceroute " + d1 +"")

            print(f'\n')

            #sys.stdout.close()

            m = input(f'''{Fore.LIGHTRED_EX}[?]{Fore.CYAN} do you want to scan more? (y/n): '''+ Fore.GREEN)
            if m == "y":
                start()

    elif option == "2":

        os.system("clear")

        print(f'''{Fore.WHITE}
INFO     
     GATHERING 
.----.______  FOLDER
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/
        
{Fore.RED} [!] {Fore.LIGHTYELLOW_EX} TYPE THE TARGET {Fore.RED}DOMAIN{Fore.LIGHTYELLOW_EX} BELOW''')

        print(Fore.WHITE+"------------------------------------")

        d1 = input(f'''{Fore.LIGHTYELLOW_EX}(pentester/menu/{Fore.CYAN}infogathering{Fore.LIGHTYELLOW_EX}){Fore.GREEN} => '''+ Fore.GREEN)

        print(Fore.CYAN +'''

starting THEHARVESTER...
            
        '''+ Fore.GREEN)

        os.system("python3 theHarvester/theHarvester.py -d "+ d1 +" -b google")

        print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +f'''
            
starting DIRSEARCH...

{Fore.LIGHTRED_EX} make sure you select an extension (ex: php,asp)           
            '''+ Fore.GREEN)

            extensions = input(Fore.RED +f'''[!] {Fore.CYAN}extensions => '''+ Fore.GREEN)
            os.system("python dirsearch/dirsearch.py -e "+ extensions +" -u "'https://' + d1 +"")

            print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''

starting DIRB...
            
            '''+ Fore.GREEN)

            os.system("dirb "'https://' + d1 +"")

            print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''

starting WHATWEB...
            
            '''+ Fore.GREEN)

            os.system("whatweb "'https://' + d1 +"")

            print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''

starting AMASS...
            
            '''+ Fore.GREEN)

            print(f'''
            
{Fore.LIGHTRED_EX}[!]{Fore.CYAN} OPTIONS: intel|enum|viz|track|db|dns 
            {Fore.GREEN}
            ''')

            options = input(Fore.RED +f'''[!] {Fore.CYAN}extensions => '''+ Fore.GREEN)

            os.system("amass " + options + "-d " + d1 +"")

            print(f'\n')


            print(Fore.CYAN +'''

starting NMAP...

        '''+ Fore.GREEN)

            print(f'''
{Fore.LIGHTRED_EX}[!]{Fore.CYAN} OPTIONS: -A|-O|-sV|-sS|-F|-sL etc... {Fore.LIGHTYELLOW_EX}(you can use more than one)
            {Fore.GREEN}
        ''')

            options = input(Fore.RED +f'''[!] {Fore.CYAN}option => '''+ Fore.GREEN)

            os.system("sudo nmap "+ options +" " + d1 +"")

            print(f'\n')


        if c == "y":
            m = input(f'''{Fore.LIGHTRED_EX}[?]{Fore.CYAN} do you want to scan more? (y/n): '''+ Fore.GREEN)
            if m == "y":
                start()

    elif option == "3":

        os.system("clear")

        print(f'''{Fore.WHITE}
ANALYSIS 
        PHASE     
.----.______  FOLDER
|           |
|    ___________
|   /          /
|  /          /
| /          /
|/__________/
        
{Fore.RED} [!] {Fore.LIGHTYELLOW_EX} TYPE THE TARGET {Fore.RED}DOMAIN{Fore.LIGHTYELLOW_EX} BELOW''')

        print(Fore.WHITE+"------------------------------------")

        d1 = input(f'''{Fore.LIGHTYELLOW_EX}(pentester/menu/{Fore.CYAN}analysisphase{Fore.LIGHTYELLOW_EX}){Fore.GREEN} => '''+ Fore.GREEN)

        print(Fore.CYAN +'''

starting NIKTO...

        '''+ Fore.GREEN)

        options = input(Fore.RED +f'''[!] {Fore.CYAN}option => '''+ Fore.GREEN)

        os.system("nikto -h " + d1 +"")

        print(f'\n')

        c = input(Fore.YELLOW +f'''continue? ({Fore.GREEN}y/{Fore.LIGHTRED_EX}n{Fore.YELLOW}) => '''+ Fore.GREEN)
        if c == "y":

            print(Fore.CYAN +'''

starting NMAP VULN SCANNER...
            
            '''+ Fore.GREEN)

            os.system("nmap --script vuln " + d1 +"")

            print(f'\n')

        if c == "y":
            m = input(f'''{Fore.LIGHTRED_EX}[?]{Fore.CYAN} do you want to scan more? (y/n): '''+ Fore.GREEN)
            if m == "y":
                start()


