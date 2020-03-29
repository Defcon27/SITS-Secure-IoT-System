import socket
import json
import pickle

HEADER_SIZE = 10

PORT = 2727
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('183.82.155.135', PORT))
s.listen(5)
print("Server is running at ", PORT)

data = {1: "hithere",
        2: "go away"}


def send_msg_recv(data):
    resp = ""

    while True:
        clientsocket, address = s.accept()
        print("Connection with " + str(address) + " is established")
        data = input()
        msg = pickle.dumps(data)
        msg = bytes(f"{len(msg):<{HEADER_SIZE}}", "utf-8")+msg
        clientsocket.send(msg)

        client_resp = str(clientsocket.recv(10000), 'utf-8')
        resp = client_resp

        break
        # clientsocket.close()

    return resp


while True:
    resp = send_msg_recv(data)
    print(resp)
