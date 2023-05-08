# MMANM_HK222

Repo được tạo cho khóa _"Mật mã và An ninh mạng"_ học kì 222

## Cấu trúc

Thư mục `src` lưu tất cả mã bao gồm:  
\-`rsa`: Chứa mã hiện thực RSA: `RSA.py` và demo các hàm `demoRSA.py`  
\-`vulnerability`: Chứa mã hiện thực các cuộc tấn công vào RSA như: Fermat, Pollard p-1, Weiner

## Cài đặt

Để chạy được các file trên yêu cầu chạy các lệnh cài đặt sau:  
\-`pip install pycryptodome`  
\-`pip install gmpy2`  
\-`pip install rsa`

## Các module

`RSA.py` cung cấp các module:  
\-`Prime(numberOfBits)`: Trả về số nguyên tố có `numberOfBits` bit  
\-`powermod(a, b, n)`: Trả về kết quả cho phép tính a^b mod(n)  
\-`gcd(a,b)`: Trả về ước chung lớn nhất của a,b
\-`RsaKey(n)`: Trả về kết quả dưới dạng: (publickey, privatekey). Trong đó các class có dạng:

```python
class publickey:
    def __init__(self,n,e) -> None:
        self.n=n
        self.e=e
class privatekey:
    def __init__(self,n,d) -> None:
        self.n=n
        self.d=d
```

\-`encrypt(pt,pub)`: pt là 1 `string`, pub là 1 object của class `publickey`. Trả về kết quả mã hóa `ct` dưới dạng `long int`  
\-`decrypt(ct,priv)`: ct là 1 `long int`, priv là 1 object của class `privatekey`. Trả về kết quả giải mã `pt` dưới dạng `string`
