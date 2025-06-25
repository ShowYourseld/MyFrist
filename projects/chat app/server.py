import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12345))
server.listen()
print('server is listening...')

clients = []
usernames = []

def broadcast(message, sender=None):
    for client in clients:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break  # Client disconnected
            broadcast(message, client)
        except:
            break
    # Handle disconnect
    if client in clients:
        index = clients.index(client)
        username = usernames[index]
        broadcast(f'user {username} has left the chat'.encode())
        clients.remove(client)
        usernames.remove(username)
        client.close()

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {address}')
        client.send('USERNAME'.encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)
        print(f"Username of the client is {username}")
        broadcast(f"{username} joined the chat!".encode(), client)
        client.send("You are now connected!".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()



