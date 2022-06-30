import requests
import socket

def monitor(url):
    """
    Question 1: define a url monitor
    :param url:
    :return:
    """
    while True:
        status = requests.get(url).status_code
        if status != 200:
            print("monitor failed. return code is: %d" % status)
            return status

def socket_chat_server(ip, port):
    """
    Question 2: define a chat using socket
    :param ip:
    :param port:
    :return:
    """
    IP_PORT = (ip, port)
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(IP_PORT)

    socket_server.listen(5)
    while True:
        conn, addr = socket_server.accept()
        print("Connected by ", addr)
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print("server receive data: ", data)
                response = input("input server msg >>> ").strip()
                conn.send(response.encode())
                print("send data to client: ", response)

            except ConnectionResetError:
                break
        conn.close()
    socket_server.close()


def socket_chat_client(ip, port):
    """
    Question 2: define a chat using socket
    :param ip:
    :param port:
    :return:
    """
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP_PORT = (ip, port)
    client_sock.connect(IP_PORT)

    while True:
        msg = input("input msg to send >>> ").strip()
        if not msg:
            continue
        client_sock.send(msg.encode())
        recv_data = client_sock.recv(1024)
        print('client recv data ', recv_data.decode())
