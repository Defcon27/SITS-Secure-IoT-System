import datetime as dt
import time
import sys
import subprocess
import math
import hmac
import hashlib


machine_IMEI = subprocess.check_output(
    'wmic csproduct get uuid').decode().split('\n')[1].strip()


def get_UnixEpox_time():
    sec = int(dt.datetime.now().strftime("%S"), 10)
    minte = int(dt.datetime.now().strftime("%M"), 10)
    hr = int(dt.datetime.now().strftime("%H"), 10)
    day = int(dt.date.today().strftime("%d"), 10)
    month = int(dt.date.today().strftime("%m"), 10)
    year = int(dt.date.today().strftime("%Y"), 10)

    today_sec = sec + minte*60 + hr*3600
    this_year_sec = (day-1)*86400 + (month-1) * \
        2629743 + ((year-1)-1970)*31556926
    tot_sec = today_sec+this_year_sec
    # print(tot_sec)
    unix_time = time.time()

    return unix_time


def TOTP_generator():
    time_step = 30
    unix_time = get_UnixEpox_time()
    N = math.floor(unix_time/time_step)
    N_hex = hex(N)
    N_hex = N_hex[2:]
    if len(N_hex[2:]) < 16:
        bl = 16-len(N_hex)
        for i in range(bl):
            N_hex = '0'+N_hex

    # print(N_hex)

    message = bytes((int(N_hex, 16)))
    key = bytes(12345)

    hmac_sha1 = hmac.new(key, message, digestmod=hashlib.sha1)
    hmac_digest_unix = hmac_sha1.hexdigest()

    message = bytes(int(machine_IMEI[:8], 16))
    hmac_sha1 = hmac.new(key, message, digestmod=hashlib.sha1)
    hmac_digest_imei = hmac_sha1.hexdigest()

    offset_hex = hmac_digest_unix[39:]
    offset_hex_imei = hmac_digest_imei[-1:]

    offset_num = int(offset_hex, 16)
    offset_num += int(offset_hex_imei, 16)
    # print(offset_num)

    hmac_offset = (hmac_digest_unix[offset_num:(offset_num+8)])
    # print(hmac_offset)
    hmac_offset_int = int(hmac_offset, 16)
    # print(hmac_offset_int)
    token_n = 6
    token = (hmac_offset_int) % (10**token_n)
    return token


time_start = time.time()
seconds = 30

print("\nGenerating T-OTP for MachineID ", machine_IMEI, "\n\n")
while True:
    try:
        totp = TOTP_generator()
        while (seconds != 0):
            sys.stdout.write(
                "\rT-OTP is {otp} valid for {seconds} Seconds".format(otp=totp, seconds=seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = seconds-1  # int(time.time() - time_start) - minutes * 60
            if seconds == 0:
                print("\nT-OTP expired\n")
                break
        seconds = 30
    except KeyboardInterrupt:
        break
