import RSA
import gmpy2
import random
import rsa

#Kiểm tra hàm RSA.Prime()
def testPrime(n=1024):
    print("@@---Kiểm tra hàm RSA.Prime()---@@")
    pr=RSA.Prime(n)
    print("Số nguyên tố: ", pr)
    print("Kiểm tra với gmpy2.is_prime(): ",gmpy2.is_prime(pr))
    print("@@---Kết thúc---@@\n")

#Kiểm tra hàm RSA.gcd()
def testGcd(a=random.randrange(2**(1024-1), 2**1024-1),b=random.randrange(2**(1024-1), 2**1024-1)):
    print("@@---Kiểm tra hàm RSA.gcd()---@@")
    print("Kết quả RSA.gcd(): ", RSA.gcd(a,b))
    print("Kiểm tra với gmpy2.gcd(): ", gmpy2.gcd(a,b))
    print("@@---Kết thúc---@@\n")

#Kiểm tra hàm RSA.powermod()
def testPowermod(a=random.randrange(2**(1024-1), 2**1024-1),b=random.randrange(2**(1024-1), 2**1024-1),n=random.randrange(2**(1024-1), 2**1024-1)):
    print("@@---Kiểm tra hàm RSA.powermod()---@@")
    print("Kết quả RSA.powermod(): ", RSA.powermod(a,b,n))
    print("Kiểm tra với built-in pow(): ", pow(a,b,n))
    print("@@---Kết thúc---@@\n")

def testEncript(pt,publickey):
    print("@@---Kiểm tra hàm RSA.encript()()---@@")
    x1=RSA.encrypt(pt,publickey)
    print("plaintext: ",pt)
    print("Kết quả RSA.encript(): ", x1)
    print("@@---Kết thúc---@@\n")
    return x1

def testDecript(ct,privatekey):
    print("@@---Kiểm tra hàm RSA.decript()()---@@")
    x1=RSA.decrypt(ct,privatekey)
    print("cirphertext: ",ct)
    print("Kết quả RSA.decript(): ", x1)
    print("@@---Kết thúc---@@\n")
    return x1

testPrime()
testGcd()
testPowermod()
testPowermod(52,-1,3)
(pub, priv) = RSA.RsaKey(1024)
ct=testEncript('Xin chào đây là bài kiểm tra RSA!',pub)
testDecript(ct,priv)
