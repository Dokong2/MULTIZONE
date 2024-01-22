import socket
import threading
import time

host = "127.0.0.1"
port = 0
client_soket = None

def recving():
    global client_socket
    while True:
        data = client_socket.recv(1024).decode()
        print(data)

def chat():
     while True:
        global port
        global client_socket
        chattext = input("PORT : " + str(port) + " ㅣ>>")
        client_socket.send(chattext.encode())
        time.sleep(0.3)

# start


print("MULTIZONE ㅣ client")
print("호완 버전 : 1.0")
print("서버에 접속하려면 [connect]")
start = input(">>")
if start == "connect":
    print("포트를 입력하세요.")
    port = input(">>")
    client_socket = socket.socket()
    client_socket.connect((host, int(port)))
    print("서버에 연결을 성공했습니다.")
    thread1 = threading.Thread(target=recving)
    thread2 = threading.Thread(target=chat)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("스레드 모두 종료.")

else:
    print("입력값이 잘못 되었습니다.")

