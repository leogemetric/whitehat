import socket

host = "103.237.98.32"
port = 25032

def request(ans):
	s = socket.socket()
	s.connect((host,port))
	s.recv(1024)
	s.recv(1024)
	s.send(str(ans)+'\n')
	return s.recv(1024)

def main():
	for i in range(100,1000):
		if "incorrectly" in request(i):
			continue
		else:
			print i
			break

if __name__ == '__main__':
	main()
