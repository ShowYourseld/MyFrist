import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen()
print('server is listing...')

clients = []
usernames = []

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client (client):
    while True:
        try:
            message = client.recv(1024).encode()
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'user {username} has left the chat', client)
            usernames.remove(username)
            break

def receive():
    while True:
        client, addres = server.accept()
        print(F'conneted with{addres}')
        client.send('USERNAME'.encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)
        print(f"Username of the client is {username}")
        broadcast(f"{username} joined the chat!".encode(), client)
        client.send("You are now connected!".encode())
        print(client.recv(1024).decode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()




