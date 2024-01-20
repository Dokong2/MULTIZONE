import socket
import threading
import WanduThread

connlist = []

def home():
    print("MULTIZONE ㅣ Server")
    print("호완 버전 : 1.0")
    print("서버를 시작하려면 [serverstart]")
    start = input(">>")
    if start == "serverstart":
        print("포트를 입력하세요.")
        port = int(input(">>"))
        host = "192.0.0.1"
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("서버 소켓이 생성되었습니다! [soket sock_stream]")
        server_socket.bind((host, port))
        print("서버 소켓이 바인드 되었습니다.")
        print("서버 생성이 완료되었습니다.")

def accepts():
    while True:
        conn, address = server_socket.accept()
        print("클라이언트가 접속했습니다. 세션 : " + str(conn) + "주소 : " + str(address))
        connlist.append(conn)


WanduThread.threadstart(accepts(), None, None)