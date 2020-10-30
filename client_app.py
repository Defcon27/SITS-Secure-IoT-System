from Sockets.client import recv_msg_send
from RSA.RSA_Light import RSA_LightWeight
import socket
import pickle

HEADER_SIZE = 10


def return_recv_msg_send(reply_msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 2727))

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
                break
        send_msg = reply_msg
        s.send(bytes(send_msg, "utf-8"))
        s.close()
        break

    return recv_msg


if __name__ == "__main__":

    RSA = RSA_LightWeight()

    # AUTH Code to secure comm. link
    auth_codes = "#SCL00"
    au = return_recv_msg_send("CNF")
    PUBLIC_KEYS = return_recv_msg_send("RECV")

    print("\nPublic Key Received: ", PUBLIC_KEYS, "\n")

    while True:
        recv_msg_send(RSA, PUBLIC_KEYS)
