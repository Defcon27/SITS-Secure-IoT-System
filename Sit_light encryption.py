
key = str(input('Enter the 64-bit key'))    #0101001000010101010101000100100101001010111110110001000100100101
chunks = []

for i in range(0,len(key),4):
    chunks.append(key[i:i+4])

for i, value in enumerate(chunks):
     exec("Kc"+str(i)+" = value")

Kb1f = Kc0 + Kc4 + Kc8 + Kc12
Kb2f = Kc1 + Kc5 + Kc9 + Kc13
Kb3f = Kc2 + Kc6 + Kc10 + Kc14
Kb4f = Kc3 + Kc7 + Kc11 + Kc15

P = {0: 3, 1: 15, 2: 14, 3: 0, 4: 5, 5: 4, 6: 11, 7: 12, 8: 13, 9: 10, 10: 9, 11: 6, 12: 7, 13: 8, 14: 2, 15: 1}

Q = {0: 9, 1: 14, 2: 5, 3: 6, 4: 10, 5: 2, 6: 3, 7: 12, 8: 15, 9: 0, 10: 4, 11: 13, 12: 7, 13: 11, 14: 1, 15: 8}
      
def Xnor(m,n):                                          # created new function for xnor 
    xnr=[]
    for i in range(0,16):
        if(m[i]=='0' and n[i]=='0'):
            xnr.append('1')
        if(m[i]=='1' and n[i]=='1'):
            xnr.append('1')
        if(m[i]=='0' and n[i]=='1'):
            xnr.append('0')
        if(m[i]=='1' and n[i]=='0'):
            xnr.append('0')
    return(''.join(xnr))

def binaryToDecimal(n): 
    return int(n,2) 

def decimalToBinary(n): 
	return bin(n).replace("0b","")

def functionP(u):                                   # funtion for P
    k = binaryToDecimal(u)
    f = P[k]
    m=decimalToBinary(f)
    if(len(m)<4):
        length = 4-len(m)
        for j in range(0,length):
            m='0'+m
    return m


def functionQ(r):                                   # funtion for Q
    k1=binaryToDecimal(r)
    f1=Q[k1]
    m1=decimalToBinary(f1)
    if(len(m1)<4):
        length1 = 4-len(m1)
        for j in range(0,length1):
            m1='0'+m1
    return m1

def shuffling(elem):                                # function for shuffling in function F
    elem1 = elem[0]+elem[1]+elem[4]+elem[5]
    elem2 = elem[2]+elem[3]+elem[8]+elem[9]
    elem3 = elem[6]+elem[7]+elem[12]+elem[13]
    elem4 = elem[10]+elem[11]+elem[14]+elem[15]
    return(elem1,elem2,elem3,elem4)

def repeatedPQ(arr):                                # PQ function used in F
    P1=functionP(arr[0])
    Q1=functionQ(arr[1])
    P2=functionP(arr[2])
    Q2=functionQ(arr[3])
    s=list(shuffling(P1+Q1+P2+Q2))
    return s

def repeated(arr):                                  # this is the change in key expansion in the last round of f-function we must not shuffle the bits so created 
    P1=functionP(arr[0])                            # new function without shuffling
    Q1=functionQ(arr[1])
    P2=functionP(arr[2])
    Q2=functionQ(arr[3])
    s=list(P1+Q1+P2+Q2)
    return s


def repeatedQP(arr1):                               # QP function used in F
    Q11=functionQ(arr1[0])
    P11=functionP(arr1[1])
    Q22=functionQ(arr1[2])
    P22=functionP(arr1[3])
    s1=list(shuffling(Q11+P11+Q22+P22))
    return s1

def functionF(ele):                                 # F function
    divide = [ele[i:i+4] for i in range(0, len(ele), 4)]
    list1=repeatedPQ(divide)
    list2=repeatedQP(list1)
    final_list=repeated(list2)
    return(''.join(final_list))
    

def matrixgenerator(t):                             # function for generating matrix
    l1=[]
    counter=0
    for i in range(0,4):
        l2=[]
        for j in range(0,4):
            l2.append(t[counter])
            counter=counter+1
        l1.append(l2)
    return(l1)


def Key1(mat):                                       # function for making key1
    sum=[]
    for i in range(0,4):
        x=''
        if(i==0 or i==2):
            for j in reversed(range(4)):
                x=x+mat[i][j]
        elif(i==1 or i==3):
            for j in range(0,4):
                x=x+mat[i][j]
        sum.append(x)
    return(''.join(sum))

def Key2(mat1):                                       # function for making key2
    sum1=[]
    for j in range(0,4):
        x1=''
        if(j==0 or j==2):
            for i in range(0,4):
                x1=x1+mat1[i][j]
        elif(j==1 or j==3):
            for i in reversed(range(4)):
                x1=x1+mat1[i][j]
        sum1.append(x1)
    return(''.join(sum1))

def Key3(mat2):                                        # function for making key3
    sum2=[]
    for i in range(0,4):
        x2=''
        if(i==0 or i==2):
            for j in range(0,4):
                x2=x2+mat2[i][j]
        elif(i==1 or i==3):
            for j in reversed(range(4)):
                x2=x2+mat2[i][j]
        sum2.append(x2)
    return(''.join(sum2))
    
def Key4(mat3):                                         # function for making key4
    sum3=[]
    for j in range(0,4):
        x3=''
        if(j==0 or j==2):
            for i in reversed(range(4)):
                x3=x3+mat3[i][j]
        elif(j==1 or j==3):
            for i in range(0,4):
                x3=x3+mat3[i][j]
        sum3.append(x3)
    return(''.join(sum3))

def Key5(K1,K2,K3,K4):                                  # function for making key5
    u0=binaryToDecimal(K1)
    u1=binaryToDecimal(K2)
    u2=binaryToDecimal(K3)
    u3=binaryToDecimal(K4)
    u4=decimalToBinary((u0^u1^u2^u3))
    if(len(u4)<16):
        for i in range(0,(16-len(u4))):
            u4='0'+u4
    return(u4)

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
K5 = Key5(K1,K2,K3,K4)


 

print('Key1:',K1)
print('Key2:',K2)
print('Key3:',K3)
print('Key4:',K4)
print('Key5:',K5)

def XOR(m1,m2):
    q=((binaryToDecimal(m1))^(binaryToDecimal(m2)))
    q1=decimalToBinary(q)
    if(len(q1)<16):
        for i in range(0,(16-len(q1))):
            q1='0'+q1
    return(q1)

chunks1 = []
													#Key: 0101001000010101010101000100100101001010111110110001000100100101	
input = str(input('Enter the input text: '))         #Input: 0101001000010101010101000100100101001010111110110001000101101100
													#Cipher: 0010001011100110111000001111011110101001001101101011001010000101

for i in range(0,len(input),16):
    chunks1.append(input[i:i+16])

for i, value in enumerate(chunks1):
     exec("Px"+str(i)+" = value")

inplist=[Px0,Px1,Px2,Px3]
def Round1(elem1,key):
    thrlist=[]
    k3=Xnor(elem1[0],key)
    if(len(k3)<16):
        for i in range(0,(16-len(k3))):
            k3='0'+k3
    Efl1=functionF(k3)
    k4=XOR(Efl1,elem1[2])
    op1=Xnor(elem1[3],key)
    if(len(op1)<16):
        for i in range(0,(16-len(op1))):
            op1='0'+op1
    Efr1=functionF(op1)
    k8=XOR(Efr1,elem1[1])
    thrlist.append(k4)
    thrlist.append(k3)
    thrlist.append(op1)
    thrlist.append(k8)
    return(thrlist)

y5=[]

y=Round1(inplist,K1)

y1=Round1(y,K2)

y2=Round1(y1,K3)

y3=Round1(y2,K4)

y4=Round1(y3,K5)

y5.append(y4[1])
y5.append(y4[0])
y5.append(y4[3])
y5.append(y4[2])
F= ''.join(y5)
print('The cipher text:',F)


#decryption
Py0=y4[1]
Py1=y4[0]
Py2=y4[3]
Py3=y4[2]
     
inplist1=[Py0,Py1,Py2,Py3]

#print(inplist1)

def Round2(elem2,key1):
    thrlist2=[]
    o3=Xnor(elem2[0],key1)
    if(len(o3)<16):
        for i in range(0,(16-len(o3))):
            o3='0'+o3
    EFl1=functionF(elem2[0])
    o4=XOR(EFl1,elem2[1])
    op11=Xnor(elem2[3],key1)
    if(len(op11)<16):
        for i in range(0,(16-len(op1))):
            op11='0'+op11
    EFr1=functionF(elem2[3])
    o8=XOR(EFr1,elem2[2])
    thrlist2.append(o8)
    thrlist2.append(o3)
    thrlist2.append(op11)
    thrlist2.append(o4)
    return(thrlist2)

q5=[]

q=Round2(inplist1,K5)

q1=Round2(q,K4)

q2=Round2(q1,K3)

q3=Round2(q2,K2)

q4=Round2(q3,K1)

q5.append(q4[1])
q5.append(q4[0])
q5.append(q4[3])
q5.append(q4[2])
print('The decrypted input text:',''.join(q5))







