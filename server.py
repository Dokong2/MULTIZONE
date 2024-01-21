import socket
import threading
import socketserver
import os
from datetime import datetime
import time
server_socket = None
connlist = []
now = time
#?
while True:
    os.system('cls')
    print("MULTIZONE ㅣ Server")
    print("호완 버전 : 1.0")
    print("서버를 시작하려면 [serverstart]")
    start = input(">>")
    if start == "serverstart":
        try:
            print("포트를 입력하세요.")
            port = int(input(">>"))
            host = "127.0.0.1"
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("서버 소켓이 생성되었습니다!")
            server_socket.bind((host, port))
            print("서버 소켓이 바인드 되었습니다.")
            print("서버 생성이 완료되었습니다.")
        except ValueError:
            print("포트 값이 유효하지 않습니다. 오타를 확인해주세요.")
            print("홈으로 돌아가려면 아무 값이나 입력하세요.")
            input("")
        except OSError:
            print("아이피 주소에 이상이 있습니다. 아이피 주소가 정상정으로 설정됬는지 확인해주세요.")
            print("홈으로 돌아가려면 아무 값이나 입력하세요.")
            input("")
        except OverflowError:
            print("에러 : 포트 값이 너무 큽니다. 포트값의 범위는 [0~65535]입니다.")
            print("홈으로 돌아가려면 아무 값이나 입력하세요.")
            input("")
        except:
            print("알수 없는 에러가 났습니다.")
            print("홈으로 돌아가려면 아무 값이나 입력하세요.")
            input("")


def accepts():
    global server_socket
    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept()
        print(now.strftime('%Y-%m-%d %H:%M:%S'), "클라이언트가 접속했습니다." + "주소 : " + str(address))
        connlist.append(conn)

def recvingandsend():
    global connlist
    global conn
    while True:
        data = conn.recv(1024).decode()
        print(data)
        for connlist in conn:
            conn.send(data.encode())

