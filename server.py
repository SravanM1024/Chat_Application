import socket
import threading

# Server configuration
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345  # Choose a port for the chat server

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def client_handler(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
                broadcast(message, client_socket)
            else:
                remove(client_socket)
        except:
            continue

def main():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Client {client_address[0]}:{client_address[1]} has connected.")
        client_handler_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_handler_thread.start()

if __name__ == "__main__":
    main()
