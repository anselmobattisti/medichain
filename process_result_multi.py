import matplotlib.pyplot as plt
import numpy as np

# files = [10,100,500,1000]
# types = ['consult', 'insert']

files = [100]
types = ['consult']

linhas = ''

mean_cosult = []
mean_insert = []
n_t = range(1,10)

for n in files:
  for k in range(0,9):
    for t in types:
      # f_csv = open('results/'+t+'_'+str(n)+"-"+str(k)+".csv", "r")
      f_csv = open(t+'_'+str(n)+"-"+str(k)+".csv", "r")
      lines = f_csv.readlines()

      mean = 0
      for l in lines:
        aux = l.split(';')
        mean += float(aux[1])
      mean = (mean / n)*1000
      if t == 'consult':
        mean_cosult.append(round(mean,2))
      else:
        mean_insert.append(round(mean,2))

#plt.plot(files,mean_insert, 'g^-', label='Inserção')
plt.plot(n_t, mean_cosult, 'bs-', label='Consulta')

plt.ylabel('Tempo em milesegundos')
plt.xlabel('Quantidade de méidias médicas')
# plt.title('Relação entre o tamanho do arquivo e ')
plt.legend()

# plt.show()
plt.savefig('result.png')

print(mean_insert)
print(mean_cosult)