import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if not msg:
                break
            print(msg)
        except:
            break

def start_client(host="127.0.0.1", port=5000, nick="User"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    print(sock.recv(1024).decode('utf-8'))
    sock.send(nick.encode('utf-8'))

    thread = threading.Thread(target=receive, args=(sock,), daemon=True)
    thread.start()

    while True:
        msg = input()
        if msg.strip().lower() == "/quit":
            sock.send("/quit".encode('utf-8'))
            break
        sock.send(msg.encode('utf-8'))

    sock.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--nick", default="User")
    args = parser.parse_args()

    start_client(args.host, args.port, args.nick)
