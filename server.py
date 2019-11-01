import socket
import sys
import threading

def check_connect(client,addr):
	 while True:
	     	data = client.recv(1024)
	     	print(data.decode('utf8')+"$>",end='')

def main():
	print("Waiting connections...")
	client, addr = socket.accept()
	print('New connection!', addr)
	th = threading.Thread(target=check_connect, args=(client,addr))
	th.start()
	while True:
		cmd = input("$>")
		if (cmd == 'msg'):
			client.send(b'msg')
			text = input('text: ')
			client.send(text.encode('utf8'))
			title = input('title: ')	
			client.send(title.encode('utf8'))
		elif(cmd == "commands"):
			print('commands - Help')
			print('msg - Send a message (MsgBox)')

		client.send(cmd.encode('utf-8'))		

if __name__ == '__main__':
	host = '127.0.0.1'
	port = 9090
	srv = (host, port)
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind(srv)
	socket.listen(5)
	main()