from SIT.SIT_Light import sit_keygen
from SIT.SIT_Light import sit_encrypt
from SIT.SIT_Light import sit_decrypt
from Hashing.hash import hashmsg

print("\nSIT Algorithm for Data Encryption \n")

password = input("Enter a secret key : ")
pass_h = hashmsg(password)
pass_h = pass_h[:8]

print("\nKey Generation\n")
keys = sit_keygen(pass_h)
for k in range(len(keys)):
    print("Round ", k+1, "key is ", keys[k])


print("\nData Encryption")
cipher_txt = []
SIZE = 8
with open('db/data.txt', 'r') as f:
    data = f.read(SIZE)
    while len(data) > 0:
        data = f.read(SIZE)
        if (len(data) < 8) and (len(data) > 0):
            rem = (SIZE-len(data)) % SIZE
            for i in range(rem):
                data = data+" "

        elif len(data) == 0:
            break

        cipher = sit_encrypt(data, keys)
        # print(cipher)
        cipher_txt.append(cipher)


print("The cipher text of the data is\n")
cipher_str = ''.join(cipher_txt)
print(cipher_str)


print("\nData Decryption")
message = []
for c in cipher_txt:
    msg = sit_decrypt(c, keys)
    message.append(msg)

message_str = ''.join(message)
print("The plain text of data is \n")
print(message_str)
