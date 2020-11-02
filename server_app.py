from Sockets.server import send_msg_recv
from Auth0.totp_client import TOTP_generator
from Hashing.hash import hashmsg
from RSA.RSA_Light import RSA_LightWeight


# Securing comm. channel using RSA
def secureChannel(PUBLIC_KEYS):

    au = "#SCL00"
    cnf = send_msg_recv(au)
    if cnf == "CNF":
        cnf = send_msg_recv(PUBLIC_KEYS)
    if cnf == "RECV":
        print("\nPublic Keys successfully published\n")
    return


# RSA Light Decryption
def decrypt(cipher_h, RSA, PRIVATE_KEYS):

    cipher = int(cipher_h, 16)
    plain = RSA.rsalight_decrypt(cipher, PRIVATE_KEYS)
    return plain


# Authentication
def auth(RSA, PRIVATE_KEYS):
    wel = "***Welcome to SITS-Secure IoT System Server***\n\nEnter Username"
    resp = send_msg_recv(wel)
    user = resp

    try:
        file_hdl = open("db/pass/"+user+".txt")
    except IOError:
        reauth()

    pas = "\nEnter Password"
    resp = send_msg_recv(pas)
    user_pass = resp
    user_pass_h = hashmsg(user_pass)

    file_hdl = open("db/pass/"+user+".txt")
    file_pass_h = file_hdl.readline()
    if user_pass_h == file_pass_h:
        print("User Authentication Successful")
        succ = "\nTwo-Factor Authentication\nEnter the Generated T-OTP"
        resp = send_msg_recv(succ)
        cipher_h = resp
        print("\nT-OTP Encrypted ", cipher_h)
        totp_cl = decrypt(cipher_h, RSA, PRIVATE_KEYS)
        print("\nT-OTP Decrypted on the server-side", totp_cl, "\n")
        totp_svr = TOTP_generator()
        print("T-OTP generated on the server-side", totp_svr, "\n")

        if int(totp_cl) == int(totp_svr):
            msg = "\nTwo-Factor Authentication Successful\nUser has been successfully Authenticated"
            resp = send_msg_recv(msg)
        else:
            msg = "Two-Factor Authentication Failed\nAccess is Denied"
            resp = send_msg_recv(msg)
            reauth(RSA, PRIVATE_KEYS)

    else:
        fail = "Wrong Username or Password Couldn't log in"
        resp = send_msg_recv(fail)
        reauth(RSA, PRIVATE_KEYS)


# Re-Authentication
def reauth(RSA, PRIVATE_KEYS):
    wel = "Credentials incorrect\n\nEnter Username"
    resp = send_msg_recv(wel)
    user = resp

    try:
        file_hdl = open("db/pass/"+user+".txt")
    except IOError:
        reauth(RSA, PRIVATE_KEYS)

    pas = "\nEnter Password"
    resp = send_msg_recv(pas)
    user_pass = resp
    user_pass_h = hashmsg(user_pass)

    file_hdl = open("db/pass/"+user+".txt")
    file_pass_h = file_hdl.readline()
    if user_pass_h == file_pass_h:
        print("User Authentication Successful")
        succ = "\nTwo-Factor Authentication\nEnter the Generated T-OTP"
        resp = send_msg_recv(succ)
        cipher_h = resp
        print("\nT-OTP Encrypted ", cipher_h)
        totp_cl = decrypt(cipher_h, RSA, PRIVATE_KEYS)
        print("\nT-OTP Decrypted on the server-side", totp_cl, "\n")
        totp_svr = TOTP_generator()
        print("T-OTP generated on the server-side", totp_svr)

        if int(totp_cl) == int(totp_svr):
            msg = "\nTwo-Factor Authentication Successful\nUser has been successfully Authenticated"
            resp = send_msg_recv(msg)
        else:
            msg = "Two-Factor Authentication Failed\nAccess is Denied"
            resp = send_msg_recv(msg)
            reauth(RSA, PRIVATE_KEYS)

    else:
        fail = "Wrong Username or Password Couldn't log in"
        resp = send_msg_recv(fail)
        reauth(RSA, PRIVATE_KEYS)


if __name__ == "__main__":

    RSA = RSA_LightWeight()
    PUBLIC_KEYS, PRIVATE_KEYS = RSA.rsalight_keygen()
    print("\nPublic Key Generated: ", PUBLIC_KEYS, "\n")

    secureChannel(PUBLIC_KEYS)

    auth(RSA, PRIVATE_KEYS)
