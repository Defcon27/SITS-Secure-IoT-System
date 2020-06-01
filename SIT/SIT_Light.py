import random
import string


def binaryToDecimal(n):
    return int(n, 2)


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def XNOR(m, n):                                          # created new function for XNOR
    xnr = []
    for i in range(0, 16):
        if(m[i] == '0' and n[i] == '0'):
            xnr.append('1')
        if(m[i] == '1' and n[i] == '1'):
            xnr.append('1')
        if(m[i] == '0' and n[i] == '1'):
            xnr.append('0')
        if(m[i] == '1' and n[i] == '0'):
            xnr.append('0')
    return(''.join(xnr))


def XOR(m1, m2):
    q = ((binaryToDecimal(m1)) ^ (binaryToDecimal(m2)))
    q1 = decimalToBinary(q)
    if(len(q1) < 16):
        for i in range(0, (16-len(q1))):
            q1 = '0'+q1
    return(q1)


def functionP(u):                                   # funtion for P
    k = binaryToDecimal(u)
    f = P[k]
    m = decimalToBinary(f)
    if(len(m) < 4):
        length = 4-len(m)
        for j in range(0, length):
            m = '0'+m
    return m


def functionQ(r):                                   # funtion for Q
    k1 = binaryToDecimal(r)
    f1 = Q[k1]
    m1 = decimalToBinary(f1)
    if(len(m1) < 4):
        length1 = 4-len(m1)
        for j in range(0, length1):
            m1 = '0'+m1
    return m1


def shuffling(elem):                                # function for shuffling in function F
    elem1 = elem[0]+elem[1]+elem[4]+elem[5]
    elem2 = elem[2]+elem[3]+elem[8]+elem[9]
    elem3 = elem[6]+elem[7]+elem[12]+elem[13]
    elem4 = elem[10]+elem[11]+elem[14]+elem[15]
    return(elem1, elem2, elem3, elem4)


def repeatedPQ(arr):                                # PQ function used in F
    P1 = functionP(arr[0])
    Q1 = functionQ(arr[1])
    P2 = functionP(arr[2])
    Q2 = functionQ(arr[3])
    s = list(shuffling(P1+Q1+P2+Q2))
    return s


# this is the change in key expansion in the last round of f-function we must not shuffle the bits so created
def repeated(arr):
    # new function without shuffling
    P1 = functionP(arr[0])
    Q1 = functionQ(arr[1])
    P2 = functionP(arr[2])
    Q2 = functionQ(arr[3])
    s = list(P1+Q1+P2+Q2)
    return s


def repeatedQP(arr1):                               # QP function used in F
    Q11 = functionQ(arr1[0])
    P11 = functionP(arr1[1])
    Q22 = functionQ(arr1[2])
    P22 = functionP(arr1[3])
    s1 = list(shuffling(Q11+P11+Q22+P22))
    return s1


def functionF(ele):                                 # F function
    divide = [ele[i:i+4] for i in range(0, len(ele), 4)]
    list1 = repeatedPQ(divide)
    list2 = repeatedQP(list1)
    final_list = repeated(list2)
    return(''.join(final_list))


def matrixgenerator(t):                             # function for generating matrix
    l1 = []
    counter = 0
    for i in range(0, 4):
        l2 = []
        for j in range(0, 4):
            l2.append(t[counter])
            counter = counter+1
        l1.append(l2)
    return(l1)


def Key1(mat):                                       # function for making key1
    sum = []
    for i in range(0, 4):
        x = ''
        if(i == 0 or i == 2):
            for j in reversed(range(4)):
                x = x+mat[i][j]
        elif(i == 1 or i == 3):
            for j in range(0, 4):
                x = x+mat[i][j]
        sum.append(x)
    return(''.join(sum))


def Key2(mat1):                                       # function for making key2
    sum1 = []
    for j in range(0, 4):
        x1 = ''
        if(j == 0 or j == 2):
            for i in range(0, 4):
                x1 = x1+mat1[i][j]
        elif(j == 1 or j == 3):
            for i in reversed(range(4)):
                x1 = x1+mat1[i][j]
        sum1.append(x1)
    return(''.join(sum1))


def Key3(mat2):                                        # function for making key3
    sum2 = []
    for i in range(0, 4):
        x2 = ''
        if(i == 0 or i == 2):
            for j in range(0, 4):
                x2 = x2+mat2[i][j]
        elif(i == 1 or i == 3):
            for j in reversed(range(4)):
                x2 = x2+mat2[i][j]
        sum2.append(x2)
    return(''.join(sum2))


def Key4(mat3):                                         # function for making key4
    sum3 = []
    for j in range(0, 4):
        x3 = ''
        if(j == 0 or j == 2):
            for i in reversed(range(4)):
                x3 = x3+mat3[i][j]
        elif(j == 1 or j == 3):
            for i in range(0, 4):
                x3 = x3+mat3[i][j]
        sum3.append(x3)
    return(''.join(sum3))


def Key5(K1, K2, K3, K4):                                  # function for making key5
    u0 = binaryToDecimal(K1)
    u1 = binaryToDecimal(K2)
    u2 = binaryToDecimal(K3)
    u3 = binaryToDecimal(K4)
    u4 = decimalToBinary((u0 ^ u1 ^ u2 ^ u3))
    if(len(u4) < 16):
        for i in range(0, (16-len(u4))):
            u4 = '0'+u4
    return(u4)


def charToBits(chars):
    SIZE = 8
    chunks = []
    for c in chars:
        asc = ord(c)
        asc_bits = decimalToBinary(asc)
        rem = (SIZE - len(asc_bits)) % SIZE
        for z in range(rem):
            asc_bits = "0"+asc_bits

        chunks.append(asc_bits)

    bits = ''.join(chunks)
    return bits


def bitsToChar(bits):
    char = []
    for b in range(0, len(bits)-8, 8):
        asc_bits = bits[b:b+8]
        asc = ((binaryToDecimal(asc_bits)+33) % 126)+33
        print("ch is ", chr(asc))
        char.append(chr(asc))

    chars = ""
    for i in char:
        chars = chars+i

    return chars


P = {0: 3, 1: 15, 2: 14, 3: 0, 4: 5, 5: 4, 6: 11, 7: 12,
     8: 13, 9: 10, 10: 9, 11: 6, 12: 7, 13: 8, 14: 2, 15: 1}

Q = {0: 9, 1: 14, 2: 5, 3: 6, 4: 10, 5: 2, 6: 3, 7: 12,
     8: 15, 9: 0, 10: 4, 11: 13, 12: 7, 13: 11, 14: 1, 15: 8}


def sit_keygen(password):
    key = charToBits(password)
    chunks = []

    for i in range(0, len(key), 4):
        chunks.append(key[i:i+4])

    # Kc0 + Kc4 + Kc8 + Kc12
    Kb1f = chunks[0] + chunks[4] + chunks[8] + chunks[12]
    Kb2f = chunks[1] + chunks[5] + chunks[9] + chunks[13]
    Kb3f = chunks[2] + chunks[6] + chunks[10] + chunks[14]
    Kb4f = chunks[3] + chunks[7] + chunks[11] + chunks[15]

    Ka1f = functionF(Kb1f)
    Ka2f = functionF(Kb2f)
    Ka3f = functionF(Kb3f)
    Ka4f = functionF(Kb4f)

    Km1 = matrixgenerator(Ka1f)
    Km2 = matrixgenerator(Ka2f)
    Km3 = matrixgenerator(Ka3f)
    Km4 = matrixgenerator(Ka4f)

    K1 = Key1(Km1)
    K2 = Key2(Km2)
    K3 = Key3(Km3)
    K4 = Key4(Km4)
    K5 = Key5(K1, K2, K3, K4)

    print('Key1:', K1)
    print('Key2:', K2)
    print('Key3:', K3)
    print('Key4:', K4)
    print('Key5:', K5)

    return [K1, K2, K3, K4, K5]


def sit_encrypt(message, keys):
    K1 = keys[0]
    K2 = keys[1]
    K3 = keys[2]
    K4 = keys[3]
    K5 = keys[4]

    chunks1 = []  # Key: 0101001000010101010101000100100101001010111110110001000100100101
    # Input: 0101001000010101010101000100100101001010111110110001000101101100
    message = charToBits(message)
    # Cipher: 0010001011100110111000001111011110101001001101101011001010000101
    for i in range(0, len(message), 16):
        chunks1.append(message[i:i+16])

    Px0 = chunks1[0]
    Px1 = chunks1[1]
    Px2 = chunks1[2]
    Px3 = chunks1[3]

    inplist = [Px0, Px1, Px2, Px3]

    def Round1(elem1, key):
        thrlist = []
        k3 = XNOR(elem1[0], key)
        if(len(k3) < 16):
            for i in range(0, (16-len(k3))):
                k3 = '0'+k3
        Efl1 = functionF(k3)
        k4 = XOR(Efl1, elem1[2])
        op1 = XNOR(elem1[3], key)
        if(len(op1) < 16):
            for i in range(0, (16-len(op1))):
                op1 = '0'+op1
        Efr1 = functionF(op1)
        k8 = XOR(Efr1, elem1[1])
        thrlist.append(k4)
        thrlist.append(k3)
        thrlist.append(op1)
        thrlist.append(k8)
        return(thrlist)

    y5 = []
    y = Round1(inplist, K1)
    y1 = Round1(y, K2)
    y2 = Round1(y1, K3)
    y3 = Round1(y2, K4)
    y4 = Round1(y3, K5)

    y5.append(y4[1])
    y5.append(y4[0])
    y5.append(y4[3])
    y5.append(y4[2])
    F = ''.join(y5)
    cipher = F
    print('The cipher text:', cipher)

    return cipher


def sit_decrypt(y4, keys):
    K1 = keys[0]
    K2 = keys[1]
    K3 = keys[2]
    K4 = keys[3]
    K5 = keys[4]

    # Py0 = y4[1]
    # Py1 = y4[0]
    # Py2 = y4[3]
    # Py3 = y4[2]

    Py0 = y4[:16]
    Py1 = y4[16:32]
    Py2 = y4[32:48]
    Py3 = y4[48:]

    inplist1 = [Py0, Py1, Py2, Py3]

    # print(inplist1)
    def Round2(elem2, key1):
        thrlist2 = []
        o3 = XNOR(elem2[0], key1)
        if(len(o3) < 16):
            for i in range(0, (16-len(o3))):
                o3 = '0'+o3
        EFl1 = functionF(elem2[0])
        o4 = XOR(EFl1, elem2[1])
        op11 = XNOR(elem2[3], key1)
        if(len(op11) < 16):
            for i in range(0, (16-len(op1))):
                op11 = '0'+op11
        EFr1 = functionF(elem2[3])
        o8 = XOR(EFr1, elem2[2])
        thrlist2.append(o8)
        thrlist2.append(o3)
        thrlist2.append(op11)
        thrlist2.append(o4)
        return(thrlist2)

    q5 = []
    q = Round2(inplist1, K5)
    q1 = Round2(q, K4)
    q2 = Round2(q1, K3)
    q3 = Round2(q2, K2)
    q4 = Round2(q3, K1)

    q5.append(q4[1])
    q5.append(q4[0])
    q5.append(q4[3])
    q5.append(q4[2])
    F = ''.join(q5)
    message = bitsToChar(F)

    return message
    print('The decrypted input text:', message)


# keys = sit_keygen("aaaabbbb")
# cipher = sit_encrypt("aaaabbbb", keys)
# print(bitsToChar(cipher))
print(b'a')
