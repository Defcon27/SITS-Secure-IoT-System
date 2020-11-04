import socket
import pickle


HEADER_SIZE = 10


# RSA Light Encryption
def encrypt(otp, RSA, PUBLIC_KEYS):

    plain = otp
    cipher = RSA.rsalight_encrypt(plain, PUBLIC_KEYS)
    cipher_h = hex(cipher)[2:]
    return cipher_h


def recv_msg_send(RSA=None, PUBLIC_KEYS=None):
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
                print(decoded_full_msg)
                break
        send_msg = input()
        if send_msg[-4:] == "#ENC":
            send_msg = encrypt(int(send_msg[:4]), RSA, PUBLIC_KEYS)
            print("\nEncrypted OTP ", send_msg, "\n")

        s.send(bytes(send_msg, "utf-8"))
        s.close()
        break


# while True:
#     recv_msg_send(send_msg)
