import matplotlib.pyplot as plt
import numpy as np

files = [10,100,500,1000]
types = ['consult', 'insert']
#files = [10]

linhas = ''

mean_cosult = []
mean_insert = []

for n in files:
  for t in types:
    f_csv = open('results/'+t+'_'+str(n)+".csv", "r")
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


fig, ax = plt.subplots()

bar_width = 0.3

index = np.arange(4)

rects1 = ax.bar(index, mean_cosult, bar_width,
                color='b',
                label='Consulta')

rects2 = ax.bar(index+bar_width, mean_insert, bar_width,
                color='r',
                label='Inserção')

ax.set_xlabel('Número de mídias na blockchain')
ax.set_ylabel('Tempo em milesegundos')
#ax.set_title('Relação entre o número de mídias e o tempo de execução')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels([10,100,500,1000])
ax.legend()
plt.grid(linestyle='dotted')

fig.tight_layout()
plt.savefig('result.png')

#print(mean_insert)
#print(mean_cosult)
#plt.show()


"""
plt.plot(files,mean_insert, 'g^-', label='Inserção')
plt.plot(files,mean_cosult, 'bs-', label='Consulta')
plt.ylabel('Tempo em milesegundos')
plt.xlabel('Quantidade de méidias médicas')
# plt.title('Relação entre o tamanho do arquivo e ')
plt.legend()

# plt.show()
plt.savefig('result.png')

print(mean_insert)
print(mean_cosult)
"""