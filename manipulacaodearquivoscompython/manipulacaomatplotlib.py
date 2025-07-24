import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d.axes3d import axis3d

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

#Graficos customizados

#x = linspace(0,5,10)
#y = x ** 2

#fig = plt.figure()

#axess = fig.add_axes([0,0,0.8,0.8])

#axess.plot(x, y, 'r')

#plt.show()
#axess.set_xlabel('x')
#axess.set_ylabel('y')
#axess.set_title('Gráfico de Linha')

#Grafico de linha com 2 figuras

#x = linspace(0,5,10)
#y = x ** 2

#fig = plt.figure()

##Eixos

#axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
#axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

##figura principal

#axes1.plot(x,y,'r')
#axes1.set_xlabel('x')
#axes1.set_ylabel('y')
#axes1.set_title('Figura Principal')

##figura secundaria

#axes2.plot(x,y,'g')
#axes2.set_xlabel('x')
#axes2.set_ylabel('y')
#axes2.set_title('Figura Secundaria')

#plt.show()

##Grafico de linha parelelo
#x = linspace(0,5,10)
#y = x ** 2
#
##Divide a area de plotagem em dois subplots
#fig, axess = plt.subplots(nrows= 1, ncols= 2)
#
##Loop pelo eixos para criar cada plot
#for ax in axess:
#    ax.plot(x, y, 'r')
#    ax.set_xlabel('x')
#    ax.set_ylabel('y')
#    ax.set_title('Titulo')
#
##ajuste de layout
#fig.tight_layout()
#
#plt.show()

#Grafico de linhas com diferentes escalas

#x = linspace(0,5,10)
#y = x ** 2
#
##cria os subplots
#fig, axess = plt.subplots(1,2, figsize=(10,4))
#
##cria o plot
#axess[0].plot(x, x**2, x, exp(x))
#axess[0].set_title("Escala padrão")
#
##cria plot2
#axess[1].plot(x, x**2, x, exp(x))
#axess[1].set_yscale("log")
#axess[1].set_title("Escala logaritma (y)")
#
#plt.show()

#x = linspace(0,5,10)
#y = x ** 2
#
##cria os subplots
#fig, axess = plt.subplots(1,2, figsize=(10,3))
#
##cria o plot
#axess[0].plot(x, x**2, x, x**3, lw= 2)
#axess[0].grid(True)
#
##cria plot2
#axess[1].plot(x, x**2, x, x**3, lw= 2)
#axess[1].grid(color= 'b', alpha= 0.7, linestyle= 'dashed', linewidth= 0.8)
#
#plt.show()

#Diferentes estilos de plots

#xx = np.linspace(-0.75, 1., 100)
#n = np.array([0,1,2,3,4,5])
#
#fig, axess = plt.subplots(1,4, figsize= (12,3))
#
##plot 1
#axess[0].scatter(xx, xx + 0.25 * randn(len(xx)), color= 'black')
#axess[0].set_title('scatter')
#
##plot 2
#axess[1].step(n, n**2, lw= 2, color= 'blue')
#axess[1].set_title('step')
#
##plot 3
#axess[2].bar(n, n**2, align= 'center', width= 0.5, alpha= 0.5, color= 'magenta')
#axess[2].set_title('bar')
#
##plot 4
#axess[3].fill_between(x, x ** 2, x ** 3, alpha=0.5, color= 'green')
#axess[3].set_title('fill_between')
#
#plt.show()
#
##Histogramas
#n = np.random.randn(100000)
#
#fig, axess = plt.subplots(1,2, figsize= (12,4))
#
#axess[0].hist(n)
#axess[0].set_title('Histograma Padrão')
#axess[0].set_xlim(min(n), max(n))
#
#axess[1].hist(n, cumulative= True, bins= 50)
#axess[1].set_title('Histograma acumulativo')
#axess[1].set_xlim(min(n), max(n))
#

#plt.show()

#Grafico 3d

#alpha = 0.7
#phi_ext = 2 * np.pi * 0.5
#
#def ColorMap(phi_m, phi_p):
#    return ( + alpha - 2 * np.cos(phi_p)*cos(phi_m) - alpha * np.cos(phi_ext - 2 * phi_p))
#
#phi_m = np.linspace(0,2*np.pi, 100)
#phi_p = np.linspace(0,2*np.pi, 100)
#x, y = np.meshgrid(phi_p, phi_m)
#z = ColorMap(x, y).T
#
#fig = plt.figure(figsize=(14,6))
#
#ax = fig.add_subplot(1,2,1,projection= '3d')
#p = ax.plot_surface(x, y, z, rstride=4, cstride=4, linewidth=0)
#
#ax = fig.add_subplot(1,2,2,projection= '3d')
#p = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
#
#cb = fig.colorbar(p, shrink=0.5)
#
#plt.show()