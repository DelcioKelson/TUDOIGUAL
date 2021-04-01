import socket


def client():
    host = socket.gethostname()    
    port = 12345  #The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    message = input(' -> ')
    
    while message.lower().strip() != 'bye':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print('Received from server: ' + data)
        message = input(' -> ')
    s.close()



if __name__ == '__main__':
    client()
