import socket
import threading

# Client configuration
HOST = '127.0.0.1'  # The server's IP address
PORT = 12345  # The server's port

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
        except:
            print("Connection to the server has been lost.")
            client_socket.close()
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
