import socket
import pickle
import json
HEADER_SIZE = 10

send_msg = "defcon"


def recv_msg_send(reply_msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('183.82.155.135', 2727))

    recv_msg = ""

    while True:
        full_msg = b""
        new_msg = True
        while True:
            msg = s.recv(16)

            if new_msg:
                #print("new msg len : ", msg[:HEADER_SIZE])
                msglen = int(msg[:HEADER_SIZE], 10)
                new_msg = False

            full_msg += msg

            if len(full_msg)-HEADER_SIZE == msglen:
                decoded_full_msg = pickle.loads(full_msg[HEADER_SIZE:])
                recv_msg = decoded_full_msg
                print(decoded_full_msg)
                break
        send_msg = input()
        s.send(bytes(send_msg, "utf-8"))
        s.close()
        break


while True:
    recv_msg_send(send_msg)
