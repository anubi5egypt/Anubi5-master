#/usr/bin/python

import os
import sys
from time import sleep

try:
    if sys.argv[1] == "setup":
        os.system("mkdir /usr/share/hol")
        sleep(0.2)
        os.system("cp * /usr/share/hol")
        sleep(0.2)
        os.system("rm -rf /usr/share/Anubi5/setup.py")
        sleep(0.2)
        file = open("/usr/bin/Anubi5","w")
        file.write("#/usr/bin/bash\n")
        file.write("\n")
        file.write("python /usr/share/Anubi5/Anubi5.py\n")
        file.close()
        os.system("chmod 777 /usr/bin/Anubi5")
except:
    print "Option not select"
    print "Please, use python "+sys.argv[0]+" setup"
