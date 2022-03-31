from Crypto.Cipher import AES
import os

def ejercicio1():
    m = "hola soy lucia !"
    master_key = os.urandom(16)
    vectoriv1 = os.urandom(16)
    vectoriv2 = os.urandom(16)
    aes1 = AES.new(master_key, AES.MODE_CBC, vectoriv1)
    aes2 = AES.new(master_key, AES.MODE_CBC, vectoriv2)
    e1 = aes1.encrypt(m)
    e2 = aes2.encrypt(m)
    print("aes1: " + e1)
    print("aes2: " + e2)
    pass

def ejercicio2():
    m = "hola soy lucia !"
    master_key = os.urandom(16)
    vectoriv = os.urandom(0)
    aes1 = AES.new(master_key, AES.MODE_CBC, vectoriv)
    aes2 = AES.new(master_key, AES.MODE_CBC, vectoriv)
    e1 = aes1.encrypt(m)
    e2 = aes2.encrypt(m)
    print("aes1: " + e1)
    print("aes2: " + e2)
    pass

if __name__ == "__main__":
    print("------------------------Ejercicio 1---------------------\n")
    ejercicio1()
    print("\n------------------------Ejercicio 2---------------------\n")
    ejercicio2()
    pass