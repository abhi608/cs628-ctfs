#!/usr/bin/python

from pwn import *

host = "cseproj91.cse.iitk.ac.in"
port = 8040

conn = remote(host, port)
print conn.recvuntil("retransmit.\n")

def check_validity(data, parity):
    if (data.count('1') % 2 != 0 and parity == '1') or (data.count('1') % 2 == 0 and parity == '0'):
    	return False
    return True

flag = ""
while True:
	bits = conn.recv()
	data = bits[1:-3]
	parity = bits[-3:-2]

	if check_validity(data, parity):
		flag = flag + chr(int(data,2))
		if chr(int(data,2)) == "}":
			print flag
			conn.close()
			break
		conn.send("1\n")
	else:
		conn.send("0\n")