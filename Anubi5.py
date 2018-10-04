import os 
import sys 
from time import sleep
import Backdoor

os.system("clear")
	
		
ascii =  """                                                                        

 $$$$$$\                      $$\       $$\ $$$$$$$\  
$$  __$$\                     $$ |      \__|$$  ____| 
$$ /  $$ |$$$$$$$\  $$\   $$\ $$$$$$$\  $$\ $$ |      
$$$$$$$$ |$$  __$$\ $$ |  $$ |$$  __$$\ $$ |$$$$$$$\  
$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\_____$$\ 
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |$$\   $$ |
$$ |  $$ |$$ |  $$ |\$$$$$$  |$$$$$$$  |$$ |\$$$$$$  |
\__|  \__|\__|  \__| \______/ \_______/ \__| \______/ 
                                                      
                                                   
									                                                                
\t\t\t\t\t\t\t\tversion 0.1"""
print  "\033[0;31m" + ascii +"\033[0m"
print "\t\033[0;38m   This Tool To BuildU up Malwares and Backdoors inside deb package Linux\033[0m  "
print  ""
print  ""
print  ""

	
while True:
    comando = raw_input("\033[4;36mcommand\033[0m\033[0;36m>\033[0m ")
    if comando == "deb_inject_backdoor":
         Backdoor.debinject()
    if comando == "exit":
         os.system("clear")
         print "Thx For Usage ;)"
         sleep(0.5)
         sys.exit(0)
    if comando == "help":
         print "info\nlist_backdoor\nhelp"
    if comando == "list_backdoor":
         print "deb_inject"
    if comando == "info":
         Backdoor.typing('Coded By AbdelRhman Anter\n x-cution team\n')
    if comando == "help(info)":
         print "Greatz and describe of software"
    if comando == "help(list_backdoor)":
         print "Listener Of Backdoors"
    if comando == "help(deb_inject)":
         print "Deb Auto Infector (Social Enginer Backdoor)"
    if comando == "help(help)":
         print "Preview Describe Of Commands"
