import time
import hashlib
from Savoir import Savoir
from threading import Thread

rpcuser = 'foo'
rpcpasswd = 'bar'
rpchost = 'localhost'
rpcport = '7410'
chainname = 'chain1'

api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)

def md5sum(filename, blocksize=65536):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    return hash.hexdigest()


def insertFile(f):
  # Insere o hash da mídia na blockchain
  dados = api.publish('stream1',md5sum(f),'')
  return dados

def consultFile():
    # Consulta o hash da mídia na blockchain
  dados = api.liststreamkeyitems('stream1',md5sum('sample.png'))
  return dados

def insertTest():
  a = []
  d = []
  for i in range(0,n):
    a.append(time.time())
    insertFile('img/'+str(i)+'.png')
    d.append(time.time())

  linha = ""
  for i in range(0,n):
    linha = linha + str(i) + ";"+str(d[i]-a[i]) + "\n"

  f_csv = open('insert_'+str(n)+".csv", "w")
  f_csv.write(linha)
  f_csv.close()

def consultTest(ID):
  a = []
  d = []
  for i in range(0,n):
    a.append(time.time())
    consultFile()
    d.append(time.time())

  linha = ""
  for i in range(0,n):
    linha = linha + str(i) + ";"+str(d[i]-a[i]) + "\n"

  f_csv = open('consult_'+str(n)+"-"+str(ID)+".csv", "w")
  f_csv.write(linha)
  f_csv.close()

n = 100
# insertTest()
c = []
for i in range(0,10):
  Thread(target=consultTest,args=[i]).start()

# consultTest()
print('fim')

"""
REPOSITÓRIO DE EXEMPLOS
# data_to_store = binascii.hexlify(b'hello')
# print(data_to_store)

# cria um novo item no stream
# print(api.publish('stream1','hash_battisti',''))

# verifica se existe um item no stream
# print(api.liststreamkeyitems('stream1','hash_battisti'))

# print(api.liststreamitems('stream1'))

# print(api.getinfo())
"""