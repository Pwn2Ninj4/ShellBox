# ShellBox
Utilidad creada en Python para generar reverse shells en distintos lenguajes de programación

<h2>USO:</h2>
$ python3 ShellBox.py -h
usage: ShellBox.py [-h] [-l] [-p] [-v] [-s]

ShellBox.py: Reverse Shell Generator
[+]By Pwn2Ninja
[+]Black0ut

optional arguments:
  -h, --help       show this help message and exit
  -l , --lhost     Specify local host ip
  -p , --lport     Specify a local port
  -v , --version   Specify the lenguage to generate the reverse shell
                   [bash, python, nc1, nc2, php, ruby, perl]
  -s , --shell     Specify shell type to use (not always applicable)
                   [sh, zsh, ksh, tcsh, bash, dash]
