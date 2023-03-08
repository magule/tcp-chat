import socket
import threading

nickname = input("choose a nickname: ") 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55556))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("error errorrr")
            client.close()
            break


def write():
	while True: #constantly waiting for new messages as soon as u input a new one
		message = f'{nickname}: {input("")}'
		client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread= threading.Thread(target=write)
write_thread.start()

#check on it again. double ug