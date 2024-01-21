import socket
import threading
host = "127.0.0.1"
port = 0


global host
global port
print("MULTIZONE ㅣ client")
print("호완 버전 : 1.0")
print("서버에 접속하려면 [connect]")
while True:
    start = input(">>")
    if start == "connect":
        print("포트를 입력하세요.")
        port = input(">>")
        connect()
    else:
        print("입력값이 잘못 되었습니다.")
    try:
        global host
        global port
        client_socket = socket.socket()
        client_socket.connect((host, int(port)))
        print("서버에 연결을 성공했습니다.")
    except TimeoutError:
        print("에러 : 서버가 응답하지 않습니다. 서버가 켜져있는지 확인하고 인터넷에 연결되었는지 확인하세요.")
    except OverflowError:
        print("에러 : 포트 값이 너무 큽니다. 포트의 범위는 [0~65535] 안입니다.")
    except ValueError:
        print("에러 : 포트값이 유효하지 않습니다. [에러 : 포트번호는 숫자입니다.]")
    except OSError:
        print("에러 : 아이피 주소가 올바르지 않습니다. 아이피 주소가 유효한지 확인하세요.")
    except:
        print("에러 : 알 수 없는 에러가 발생했습니다. 도움이 된다면 스크린샷을 보내주시면 감사하겠습니다. 추후 패치하겠습니다.")


def recv():
    while True:
        data = conn.recv(1024).decode()

        #와 검나 복잡햌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
