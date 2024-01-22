import socket
import threading
import socketserver
import os
from datetime import datetime
import time
server_socket = None
connlist = []
now = time
conn = ""
def accepts():
    global server_socket
    global connlist
    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept()
        print(now.strftime('%Y-%m-%d %H:%M:%S'), "client is connect. " + "way : " + str(address))
        connlist.append(conn)
        print("[connlist]에 새로운 콘이 들어갔습니다.")
        t1 = threading.Thread(target=recvingandsend,args=(conn,))
        t1.start()


def recvingandsend(conn):
    global connlist
    while True:
        data = conn.recv(1024).decode()
        print("클라이언트에게 샌드 데이터가 왔습니다. 데이터 : " + str(data))
        for conn in connlist:
            conn.send(data.encode())
            print("전송됨. conn : " + str(conn))
        print("모든 클라이언트에게 전송되었습니다. 값 : " + str(data))





# start


os.system('cls')
print("MULTIZONE ㅣ Server")
print("호완 버전 : 1.0")
print("서버를 시작하려면 [open]")
start = input(">>")
if start == "open":
    print("포트")
    port = int(input(">>"))
    host = "127.0.0.1"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("소켓 서버 생성")
    server_socket.bind((host, port))
    print("소켓 서버 바인드 성공")
    print("서버가 생성되었습니다.")
    t2 = threading.Thread(target=accepts)
    t2.start()
    t2.join()
