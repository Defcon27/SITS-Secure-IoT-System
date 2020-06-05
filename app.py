from Sockets.server import send_msg_recv
from Auth0.totp import TOTP_generator
from Hashing.hash import hashmsg
from RSA.RSA_Light import RSA_LightWeight


# Authentication
def auth():
    wel = "***Welcome to SITS-Secure IoT System Server***\n\nEnter Username"
    resp = send_msg_recv(wel)
    user = resp

    try:
        file_hdl = open("C://Users/subha/Desktop/Cyber/db/pass/"+user+".txt")
    except IOError:
        reauth()

    pas = "\nEnter Password"
    resp = send_msg_recv(pas)
    user_pass = resp
    user_pass_h = hashmsg(user_pass)

    file_hdl = open("C://Users/subha/Desktop/Cyber/db/pass/"+user+".txt")
    file_pass_h = file_hdl.readline()
    if user_pass_h == file_pass_h:
        print("User Authentication Successful")
        succ = "\nTwo-Factor Authentication\nEnter the Generated T-OTP"
        resp = send_msg_recv(succ)
        topt_cl = resp
        totp_svr = TOTP_generator()
        print("T-OTP generated on the server-side", totp_svr)

        if int(topt_cl) == int(totp_svr):
            msg = "\nTwo-Factor Authentication Successful\nUser has been successfully Authenticated"
            resp = send_msg_recv(msg)
        else:
            msg = "Two-Factor Authentication Failed\nAccess is Denied"
            resp = send_msg_recv(msg)
            reauth()

    else:
        fail = "Wrong Username or Password Couldn't log in"
        resp = send_msg_recv(fail)
        reauth()


def reauth():
    # Authentication
    wel = "Credentials incorrect\n\nEnter Username"
    resp = send_msg_recv(wel)
    user = resp

    try:
        file_hdl = open("C://Users/subha/Desktop/Cyber/db/pass/"+user+".txt")
    except IOError:
        reauth()

    pas = "\nEnter Password"
    resp = send_msg_recv(pas)
    user_pass = resp
    user_pass_h = hashmsg(user_pass)

    file_hdl = open("C://Users/subha/Desktop/Cyber/db/pass/"+user+".txt")
    file_pass_h = file_hdl.readline()
    if user_pass_h == file_pass_h:
        print("User Authentication Successful")
        succ = "\nTwo-Factor Authentication\nEnter the Generated T-OTP"
        resp = send_msg_recv(succ)
        topt_cl = resp
        totp_svr = TOTP_generator()
        print("T-OTP generated on the server-side", totp_svr)

        if int(topt_cl) == int(totp_svr):
            msg = "\nTwo-Factor Authentication Successful\nUser has been successfully Authenticated"
            resp = send_msg_recv(msg)
        else:
            msg = "Two-Factor Authentication Failed\nAccess is Denied"
            resp = send_msg_recv(msg)
            reauth()

    else:
        fail = "Wrong Username or Password Couldn't log in"
        resp = send_msg_recv(fail)
        reauth()


auth()
