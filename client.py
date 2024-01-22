import socket
import threading
host = "127.0.0.1"
port = 0


def recv():
    while True:
        data = client_socket.recv(1024).decode()
        print(data)

def chat():
    chattext = input("PORT : " + str(port) + " ㅣ>>")
    client_socket.send(chattext)

# start


print("MULTIZONE ㅣ client")
print("호완 버전 : 1.0")
print("서버에 접속하려면 [connect]")
while True:
    start = input(">>")
    if start == "connect":
        print("포트를 입력하세요.")
        port = input(">>")
    else:
        print("입력값이 잘못 되었습니다.")

    client_socket = socket.socket()
    client_socket.connect((host, int(port)))
    print("서버에 연결을 성공했습니다.")
    thread1 = threading.Thread(target=recv)
    thread1.start()
    thread2 = threading.Thread(target=chat)
    thread2.start()