import socket
import threading

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'USERNAME':
                client.send(input().encode())
            else:
                print(message)

        except Exception as e:
                print("An error occurred!", e)
                client.close()
                break

def write():
    while True:
        message = input()
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()