import socket
import threading

clients = {}
lock = threading.Lock()

def broadcast(message, sender=None):
    with lock:
        for nick, client in clients.items():
            if nick != sender:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    del clients[nick]

def handle_client(client, addr, nick):
    welcome = f"[SERVER] {nick} joined the chat!"
    print(welcome)
    broadcast(welcome, sender=nick)
    client.send("Welcome to the chat! Type /quit to exit.".encode('utf-8'))

    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break

            if msg.startswith('/'):
                if msg.startswith('/quit'):
                    client.send("Goodbye!".encode('utf-8'))
                    break
                elif msg.startswith('/list'):
                    nicks = ', '.join(clients.keys())
                    client.send(f"[SERVER] Online: {nicks}".encode('utf-8'))
                else:
                    client.send("[SERVER] Unknown command.".encode('utf-8'))
            else:
                broadcast(f"{nick}: {msg}", sender=nick)

        except:
            break

    with lock:
        del clients[nick]
    client.close()
    broadcast(f"[SERVER] {nick} left the chat.")

def start_server(host="0.0.0.0", port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[SERVER] Listening on {host}:{port}")

    while True:
        client, addr = server.accept()
        client.send("Enter your nickname:".encode('utf-8'))
        nick = client.recv(1024).decode('utf-8').strip()
        with lock:
            clients[nick] = client
        thread = threading.Thread(target=handle_client, args=(client, addr, nick))
        thread.start()

if __name__ == "__main__":
    start_server()
