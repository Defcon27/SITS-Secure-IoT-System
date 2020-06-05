import random


class RSA_LightWeight:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.s = 0

    # Generating public and private keys using two arbitary prime numbers
    def rsalight_keygen(self):
        # Euclid's algorithm for finding GCD
        def gcd(a, b):
            while (b != 0):
                c = a % b
                a = b
                b = c

            return a

        # Euclid's Extended algorithm for Modular Inverse
        def mod_inv(a, b):
            phi = b
            x0, x1, y0, y1 = 0, 1, 1, 0
            while a != 0:
                (q, a), b = divmod(b, a), a
                y0, y1 = y1, y0 - q * y1
                x0, x1 = x1, x0 - q * x1

            if (x0 < 0):
                return x0+phi

            return x0

        # Primality Test
        def is_prime(num):
            if num == 2:
                return True
            if num < 2 or num % 2 == 0:
                return False
            for n in range(3, int(num**0.5)+2, 2):
                if num % n == 0:
                    return False
            return True

        # Generating Prime Numbers
        def generate_prime_number(length):
            p = 0
            while not is_prime(p):
                p = random.getrandbits(length)
                # print(p)

            return p

        # Generating public and private keys
        def key_gen():
            prime_len = 15

            p = generate_prime_number(prime_len)
            q = generate_prime_number(prime_len)
            s = generate_prime_number(prime_len)
            while q == p:
                q = generate_prime_number(prime_len)

            while s == q and s == p:
                s = generate_prime_number(prime_len)

            if is_prime(p) != 1 or is_prime(q) != 1 or is_prime(s) != 1:
                raise ValueError("Numbers are not prime")
            elif p == q or q == s or p == s:
                raise ValueError("Some numbers are equal")

            N = p*q*s
            # Euler Totient of N
            phi_N = (p-1)*(q-1)*(s-1)
            # Choosing integer e such that gcd (e,phi_N) is 1
            e = random.randrange(2, phi_N)
            g = gcd(e, phi_N)
            while (g != 1):
                e = random.randrange(2, phi_N)
                g = gcd(e, phi_N)

            d = mod_inv(e, phi_N)
            d_p = mod_inv(e, p-1)
            d_q = mod_inv(e, q-1)

            if (p > q):
                q_in = mod_inv(q, p)
            else:
                q_in = mod_inv(p, q)

            return [e, N], [q_in, d_p, d_q, p, q]

        public_keys, private_keys = key_gen()
        return public_keys, private_keys

    # RSA Light Weight Encryption
    def rsalight_encrypt(self, message, public_keys):
        e = public_keys[0]
        N = public_keys[1]

        cipher = pow(message, e, N)
        return cipher

    # RSA Light Weight Decryption
    def rsalight_decrypt(self, cipher, private_keys):
        q_in = private_keys[0]
        d_p = private_keys[1]
        d_q = private_keys[2]
        p = private_keys[3]
        q = private_keys[4]

        M_a = pow(cipher, d_p, p)
        M_b = pow(cipher, d_q, q)
        h = (q_in*(M_a - M_b)) % p
        message = M_b + (h*q)
        return message


# rsa = RSA_LightWeight()
# k_pub, k_prv = rsa.rsalight_keygen()
# print(k_pub, k_prv)
# cipher = rsa.rsalight_encrypt(100000, k_pub)
# print(cipher)
# message = rsa.rsalight_decrypt(cipher, k_prv)
# print(message)
