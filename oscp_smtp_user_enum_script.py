#!/usr/bin/python
#######################################
# my Twitter 
# my LinkedIn

# This is Simple Python Script To Make User Enumeration
# On SMTP Service By Using One of Two Commands
# <VRFY> Command or <RCPT TO> Command
# Usage : python script.py 192.168.1.1 users_list.txt
#######################################
import socket
import time
import sys

class PC:
	HEADER='\033[95m'
	OKBLUE='\033[94m'
	OKCYAN='\033[96m'
	OKGREEAN='\033[92m'
	WARNING='\033[93m'
	FAIL='\033[91m'
	ENDC='\033[0m'
	BOLD='\033[1m'
	UNDERLINE='\033[4m'

def VRFY(host,users,port):

	print PC.OKCYAN+"[*] USING %s <VRFY> %s Command %s" % (PC.WARNING,PC.OKCYAN,PC.ENDC)
	f=open(users,"r")
	w=open("results_smtp_user_enum.txt","w+")
	lines=f.readlines()
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	print PC.OKCYAN+"[*] Connecting With %s %s : %d %s" % (PC.WARNING,host,port,PC.ENDC)
	recv=s.recv(1024)
	print PC.OKCYAN+"[*] Receving Bunner : %s %s %s " % (PC.WARNING,recv,PC.ENDC)
	c=1
	for user in lines:
		s.send("VRFY " + user)
		recv=s.recv(1024)
		if "2.0.0" in recv:
			
			print PC.OKGREEAN+"[+] Found user: %s %s %s" % (PC.BOLD,user.rstrip(),PC.ENDC)
			w.write(user)
		else:
			
			print PC.FAIL+"[-] NOT Found : %s %s %s " % (PC.BOLD,user.rstrip(),PC.ENDC) 
		time.sleep(1)
		c+=1
		if c == 20:
			s.close()
			time.sleep(2)
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((host,port))
			s.recv(1024)
			c=1
			continue

	s.close()
	print PC.HEADER+"[*] Enumeration Done"+PC.ENDC





def RCPT(host,users,port):

	print PC.CYAN+"[*] USING %s <RCPT TO> %s Command %s" % (PC.WARNING,PC.CYAN,PC.ENDC)
	f=open(users,"r")
	w=open("result_smtp_user_enum.txt","w+")
	lines=f.readlines()
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	print PC.OKCYAN+"[*] Connecting With %s %s : %d %s" % (PC.WARNING,host,port,PC.ENDC)
	recv=s.recv(1024)
	print PC.OKCYAN+"[*] Receving Bunner : %s %s %s " % (PC.WARNING,recv,PC.ENDC)
	c=1
	s.send("MAIL FROM:x\r\n")
	s.recv(1024)
	time.sleep(2)
	for user in lines:
		s.send("RCPT TO: " + user)
		recv=s.recv(1024)
		if "2.1.5" in recv:
			
			print PC.OKGREEN+"[+] Found user : %s %s %s" % (PC.BOLD,user,PC.ENDC)
			w.write(user)
		else:
			
			print PC.FAIL+"[-] NOT Found : %s %s %s " % (PC.BOLD,user,PC.ENDC) 
		time.sleep(1)
		c+=1
		if c == 20:
			s.close()
			time.sleep(2)
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((host,port))
			s.recv(1024)
			s.send("MAIL FROM:x\r\n")
			s.recv(1024)
			c=1
			continue

	s.close()
	print PC.HEADER+"[*] Enumeration Done"+PC.ENDC


def chk(host,port):

	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	s.recv(1024)
	s.send("VRFY\r\n")
	recv=s.recv(1024)
	time.sleep(1)
	if "5.5.2" in recv:
		command="RCPT"
	else:
		command="VRFY"
	return command

if len(sys.argv) < 2:
	print "Usage : %s <host> <users-list> <port-default(25)>" % (sys.argv[0])
elif len(sys.argv) == 3:
	host=sys.argv[1]
	users=sys.argv[2]
	port=25
	print PC.HEADER+"[*] Start SMTP User Enumeration "+PC.ENDC
	if chk(host,port) == "VRFY":
		VRFY(host,users,port)
	elif chk(host,port) == "RCPT":
		RCPT(host,users,port)
else:
	host=sys.argv[1]
	users=sys.argv[2]
	port=int(sys.argv[3])	
	print PC.HEADER+"[*] Start SMTP User Enumeration "+PC.ENDC
	if chk(host,port) == "VRFY":
		VRFY(host,users,port)
	elif chk(host,port) == "RCPT":
		RCPT(host,users,port)
	
	

