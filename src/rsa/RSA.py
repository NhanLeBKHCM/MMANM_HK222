import random
from Crypto.Util import number

class publickey:
    def __init__(self,n,e) -> None:
        self.n=n
        self.e=e
class privatekey:
    def __init__(self,n,d) -> None:
        self.n=n
        self.d=d
    
def Prime(numberOfBits):
    # Pre generated primes
    first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                        73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                        127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                        179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                        233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                        283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                        353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
                        419, 421, 431, 433,	439, 443, 449, 457,	461, 463,
                        467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
     
    def getLowLevelPrime(n):
        '''Generate a prime candidate divisible by first primes'''
        while True:
            # Tạo ngẫu nhiên một số nguyên
            # Để đảm bảo N của RSA đúng kích thước ta chọn các số có 2 bit đầu là '1'
            pc = random.randrange(2**(n-1)+2**(n-2)+1, 2**n-1)
    
            # Kiểm tra nó với các số nguyên tố nhỏ
            for divisor in first_primes_list:
                if pc % divisor == 0 and divisor**2 <= pc:
                    break
            else:
                return pc
    
    #Kiểm tra Miller-Rabin xem 1 số phải là số nguyên tố hay không
    #Xác suất: Pr(n,t)=1-4^(-t), qua 40 lần kiểm tra Pr(n,40)~1
    def isMillerRabinPassed(n):
        k = 0
        q = n - 1
        while q % 2 == 0:
            q = q >> 1
            k += 1
    
        def testComposite(round_tester):
            if powermod(round_tester, q, n) == 1: #dung ham power o day
                return False
            for j in range(k):
                if powermod(round_tester, (2**j) * q, n) == n-1: #dung ham power o day
                    return False
            return True
    
        # Đặt số lần kiểm tra Miller Rabin
        iteration_num = 40
        for i in range(iteration_num):
            a = random.randrange(2, n - 1)
            if testComposite(a): return False
        return True
    
    while True:
        prime_candidate = getLowLevelPrime(numberOfBits)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            # print(prime_candidate)
            return prime_candidate



def powermod(a, b, n):
    #Hàm tìm x,y,gcd với a*x+b*y=gcd(a,b)
    def extended_gcd(a,b):
        x,y,x1,y1=1,0,0,1
        a1,b1=a,b
        while(b1!=0):
            q=a1//b1
            x,x1=x1,x-q*x1
            y,y1=y1,y-q*y1
            a1,b1=b1,a1-q*b1
        return a1,x,y

    r = 1
    flag=False
    if(b<0):
        flag=True
        b=-b
    while b > 0:
        if b % 2==1:
            r = r * a % n
        b =b//2
        a = a * a % n
    if(flag):
        r=extended_gcd(r,n)[1]
        if r<0: 
            r=r%n
    return r

def gcd(a,b):
    while(a!=0):
        c=a
        a=b%a
        b=c
    return b

def RsaKey(n):
    """
    Tạo bộ khóa RSA với số N có độ dài n bits
    """
    p = Prime(n//2+n%2)
    q = Prime(n//2)

    # tính N và phi(N)
    N = p * q
    phi_N = (p-1) * (q-1)

    # chọn e là số nguyên tố cùng nhau với phi(N)
    e = random.randrange(1, phi_N)
    g = gcd(e, phi_N)
    while g != 1:
        e = random.randrange(1, phi_N)
        g = gcd(e, phi_N)

    # tính d là nghịch đảo modular của e và phi(N)
    d = powermod(e, -1, phi_N)

    # trả về bộ khóa
    return (publickey(N,e), privatekey(N, d))

def encrypt(pt,pub):
    pt=pt.encode('utf8')
    pt=number.bytes_to_long(pt)
    return powermod(pt,pub.e,pub.n)

#Giai ma
def decrypt(ct,priv):
    pt=powermod(ct,priv.d,priv.n)
    pt=number.long_to_bytes(pt)
    return pt.decode('utf8')

# from Crypto.PublicKey import RSA
# p=number.getPrime(1024)
# a=8
# # print(len(bin(RsaKey(2048)[1][0])[2:]))
# # print(len(bin(RSA.generate(2048).p)[2:]))