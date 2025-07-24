import matplotlib as mpl
import matplotlib.pyplot as plt

#plt.plot([1,3,5], [2,4,7])
#plt.show()

#x = [2,3,5]
#y = [3,5,7]

#plt.plot(x,y)
#plt.xlabel('Variavel 1')
#plt.ylabel('Variavel 2')
#plt.title('Teste Plot')
#plt.show()

#x2 = [1,2,3,]
#y2 = [11,12,15 ]

#plt.plot(x2, y2, label = 'Grafico com Matplotlib')
#plt.legend()
#plt.show()

#Grafico de barras
#x = [2,4,6,8,10]
#y = [6,7,8,2,4]

#plt.bar(x, y, label= 'Barras', color= 'green')
#plt.legend()
#plt.show()

#x1 = [1,3,5,7,9]
#y2 = [7,8,2,4,2]

#plt.bar(x, y, label= 'Lista 1', color= 'green')
#plt.bar(x1, y2, label= 'Lista 2', color= 'red')
#plt.legend()
#plt.show()

#idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,74,54,44,64,13,18,48]
#ids = [x for x in range(len(idades))]
#print(ids)

#plt.bar(ids, idades)
#plt.show()

#Estograma

#bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

#plt.hist(idades, bins, histtype= 'bar', rwidth= 0.8)
#plt.hist(idades, bins, histtype= 'stepfilled', rwidth= 0.8)
#plt.show()

# Grafico de Dispersão

#x = [1,2,3,4,5,6,7,8]
#y = [5,2,4,5,6,8,4,8]

#plt.scatter(x, y, label= 'Pontos', color= 'black', marker= '*')
#plt.legend()
#plt.show()

#Grafico de area empilhada

#dias = [1,2,3,4,5]
#dormir = [7,8,6,7,7]
#comer = [2,3,4,5,3]
#trabalhar = [7,8,7,2,2]
#passear = [8,5,7,8,13]

#plt.stackplot(dias, dormir, comer, trabalhar, passear,  colors= ['m', 'c', 'r', 'k', 'b'])

#plt.show()

#Grafico de pizza

#fatias = [7,2,2,13]
#atividades = ['dormir', 'comer', 'passear', 'trabalhar']
#cores = ['olive', 'lime', 'violet', 'royalblue']

#plt.pie(fatias, labels= atividades, colors= cores, startangle= 90, shadow= True, explode=(0,0.2,0,0))
#plt.show()


