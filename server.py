import threading
import socket

host = "127.0.0.1" #local
port = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host,port))
server.listen()


clients = []
nicknames = []


def broadcast(message): #broadcast a message to all the clients on the server
	for client in clients: #for every client in clients list
		client.send(message)


def handle(client): #get message from client and then broadcast to all the clients 
	while True:
		try:
			message = client.recv(1024) #try to recieve a mess from the client and if it succeeds broadcast it
			broadcast(message)
		except: #if any errors
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			nicknames.remove(nickname)
			broadcast(f'{nickname} left the chat'.encode('ascii'))
			break



def recieve():
	while True: #allowing clients to connect
		client, address = server.accept() #accept method gets a connection then we get a client and adress of the client
		print(f"connected with {str(address)}")

		client.send("NICK".encode("ascii"))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)

		print(f"nickname of the client is {nickname}")
		broadcast(f"{nickname} joined the chat".encode("ascii"))
		client.send("connected to the server".encode("ascii"))

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

print("server listening")
recieve()






















