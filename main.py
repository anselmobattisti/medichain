import hashlib
import binascii
import json
from Savoir import Savoir

def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()

rpcuser = 'foo'
rpcpasswd = 'bar'
rpchost = 'localhost' #probably you don't need to connect to the server
rpcport = '7410'
chainname = 'chain1'

api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

# generate the hash from a file
file_hash = md5sum('sample.png')

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

j = json.loads(data)
a = api.publish('stream1',file_hash, binascii.hexlify(bytes(j, "utf-8")))

print(a)
print("a")

# print(file_hash)

# data_to_store = binascii.hexlify(b'hello')
# print(data_to_store)

# cria um novo item no stream
# print(api.publish('stream1','hash_battisti',''))

# verifica se existe um item no stream
# print(api.liststreamkeyitems('stream1','hash_battisti'))

# print(api.liststreamitems('stream1'))

# print(api.getinfo())


