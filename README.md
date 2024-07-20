# Python Chat (Sockets)

## Description ENG/RU
Простой многопользовательский чат на Python с использованием TCP-сокетов.
Simple multiplayer chat in Python using TCP sockets.

## Possibilities
- Multiple clients at the same time
- Nicknames
- Commands: /list, /quit
  
## Launch

### Server
```bash
python src/server.py --host 0.0.0.0 --port 5000
```

### Program client
```bash
python src/client.py --host 127.0.0.1 --port 5000 --nick Alice
python src/client.py --host 127.0.0.1 --port 5000 --nick Bob
```

## Creator
Li Vyacheslav

## 📷 Example

![Chat Example](Chat_test.png)
