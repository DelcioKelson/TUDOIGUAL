import socket



def server():
    host = socket.gethostname()
    port = 12345     # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(2)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024).decode()
        if not data: break
        print("from connected user : " + str(data))
        data = input('-> ')
        conn.send(data.encode())
    conn.close()


if __name__ == '__main__':
    server()