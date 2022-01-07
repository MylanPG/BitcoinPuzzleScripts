import ecdsa
import codecs
import hashlib
import random
from random import randint
import time


line = 1

line2 = 1

kn = 23771900000

print(time.strftime('%H:%M:%S'))


a = 2 ** 64 - 100000000000000
b = 2**64

while True:

 pk = random.randint((a), (b))

 pkh = hex(pk)

 pkh2 = ((pkh)[2:]).zfill(64)

 private_key_bytes = codecs.decode(pkh2, 'hex')
 # Get ECDSA public key
 key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
 key_bytes = key.to_string()
 key_hex = codecs.encode(key_bytes, 'hex')
 pub = (codecs.decode(key_hex))[:64]

 p2 = "02" + pub
 p3 = "03" + pub

 pk3 = (codecs.encode((hashlib.new('ripemd160', (hashlib.new('sha256', (codecs.decode((p2), 'hex'))).digest())).digest()), 'hex').decode("utf-8")).upper()
 pk4 = (codecs.encode((hashlib.new('ripemd160', (hashlib.new('sha256', (codecs.decode((p3), 'hex'))).digest())).digest()), 'hex').decode("utf-8")).upper()

# print(p2, p3, line)
# print(pk3, pk4, pk, line, line2)
# pk = pk - 1
 line = line + 1
 line2 = line2 + 1

 if line2 == int("100000"):
  kn = kn + 100000
  print(kn, time.strftime('%H:%M:%S'))
  line2 = 1
#   break

 if line == int("100"):
  a = a - 100000000000000
  b = b - 100000000000000
  pk = random.randint((a), (b))
  line = 1

 if pk3 == "3EE4133D991F52FDF6A25C9834E0745AC74248A4":
  print(pk, pk3, p2)
  print(pk, pk3, p2, file=open("found.txt", "a"))
  break

 if pk4 == "3EE4133D991F52FDF6A25C9834E0745AC74248A4":
  print(pk, pk4, p3)
  print(pk, pk4, p3, file=open("found.txt", "a"))
  break


 if a < int("16140901064495857663"):
  a = 2 ** 64 - 100000000000000
  b = 2**64