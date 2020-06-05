from RSA.RSA_Light import RSA_LightWeight
from cryptography.fernet import Fernet

# Establishing secure comm. channel using RSA for Key-exchange


def key_exg():
    key = Fernet.generate_key()
    key = key.decode()
    print("Let the key to be exchanged is ", key)

    rsa = RSA_LightWeight()
    k_pub, k_prv = rsa.rsalight_keygen()
    print("\nGenerating Public and Private keys.............")
    print("\nThe Public keys are ", k_pub)
    print("The Private keys are ", k_prv)

    cip = []
    cip_str = []
    for k in key:
        asc = ord(k)
        cipher = rsa.rsalight_encrypt(asc, k_pub)
        cip.append(cipher)
        cip_str.append(str(cipher))

    cipher = ''.join(cip_str)
    print("\nThe Encrypted key using Public key\n", cipher)

    message = []
    for c in cip:
        msg = rsa.rsalight_decrypt(c, k_prv)
        message.append(chr(msg))

    message = ''.join(message)
    print("\nThe Decrypted key using Private key\n", message)


key_exg()
