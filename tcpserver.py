import socket
import threading

IP = "0.0.0.0"
PORT = 9999

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print (f'[*] Listening on {IP}:{PORT}')
    
    
    while True:
        client, address = server.accept()
        print (f'[*] Accepted connection from {address[0]}:{address[1]}')	
        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
    
# this is our client-handling thread
def handle_client(client_socket):
    with client_socket as sock:
        # print out what the client sends
        request = sock.recv(1024)	
        print ('[*] Received: {request.decode("utf-8")}')	
        # send back a packet
        sock.send(b"ACK!")
	
if __name__ == '__main__':
        main()
