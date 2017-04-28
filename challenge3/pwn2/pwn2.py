import socket
from math import *
import time
from ctypes import CDLL
libc = CDLL('libc.so.6')

host = "103.237.98.32"
port = 25032

ar = []

def request():
    s = socket.socket()
    s.connect((host,port))
    print s.recv(1024)
    print s.recv(1024)
    s.send(str(576)+'\n')
    print s.recv(1024)
    print s.recv(1024)
    now = int(floor(time.time()))
    libc.srand(now)
    random_num = libc.rand()
    s.send(str(random_num)+'\n')
    txt =  s.recv(1024)+s.recv(1024)
    return txt

def main():
    ans = request()
    print ans

if __name__ == '__main__':
    main()
