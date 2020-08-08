import base64
from pyDes import *

key = "Ab5d1Q32"
code = "xKXOhHDvfcEinVUmuoO1OIiHJf8ReYbq"

keyE = key.encode("UTF-8")
codeE = code.encode("UTF-16")

keyde = base64.b64decode(key)
codede = base64.b64decode(code)

keydeD = keyde.decode("utf-16")
codedeD = codede.decode("utf-16")

k = des(key, CBC, key, pad=None, padmode=PAD_PKCS5)

d = k.decrypt(codede)
f = d.decode("utf-8")
print("d : %r" % f)
