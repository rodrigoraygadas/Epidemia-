import random
import pov
import matplotlib.pyplot as plt

'''
estado:
  0 Sano   verde
  1 enfermo rojo
  2 recuperado  azul
  3 vacunado  (color segun vacuna)
  4 muerto  negro
  5 inmune amarillo 
'''
'''
vacunas:
  1 Pfizer blanco
  2 Sputnik gris
  3 Astrazeneca Rosa
  4 Moderna Azul claro
'''
class Persona:
    estado = 0
    contactos =[]
    diaContagio = 0
    diaVacuna = 0
    tipoVacuna = 0
    def __init__(self, e, c, dc):
        self.estado = e        
        self.contactos = c
        self.diaContagio = dc
              
def creaPobInicial(n):
    poblacion = []
    for c1 in range(n):
        a=[]
        for c2 in range(n):
            contactos = []
            for cc in range(10): #contador de contactos
                alex=random.randint(-3,3)
                aley=random.randint(-3,3)
                if (alex!=0) and (aley!=0): 
                    contactos.append([(c1+alex)%n, (c2+aley)%n])
            alex=random.randint(0,n-1)
            aley=random.randint(0,n-1)
            if (alex!=c1) and (aley!=c2): 
                    contactos.append([alex, aley])
            a.append(Persona(0,contactos, 0))
        poblacion.append(a)
    return poblacion

def pob2pov(pob):
    cad = pov.povBasico()
    cad += pov.povLuz (1000, 1000, 1000, 1,1,1)
    cad += pov.povCamara (50, 50, 100, 50,50,50)
    for c1 in range(n):
        for c2 in range(n):
            x = c2
            y = c1
            z = 0
            perso=pob[c1][c2]
            if (perso.estado==0):
                textura = "texture{pigment{color rgb <0,1,0>}}"
            elif (perso.estado==1):
                textura = "texture{pigment{color rgb <1,0,0>}}"
            elif (perso.estado==2):
                textura = "texture{pigment{color rgb <0,0,1>}}"
            elif (perso.estado==3):
                if(perso.tipoVacuna==1):
                    textura = "texture{pigment{color rgb <1,1,1>}}"
                elif(perso.tipoVacuna==2):
                    textura = "texture{pigment{color rgb <0.5,0.5,0.5>}}"
                elif(perso.tipoVacuna==3):
                    textura = "texture{pigment{color rgb <1,0,1>}}"
                elif(perso.tipoVacuna==4):
                    textura = "texture{pigment{color rgb <0,1,1>}}"                    
            elif (perso.estado==4):
                textura = "texture{pigment{color rgb <0,0,0>}}"
            elif (perso.estado==5):
                textura = "texture{pigment{color rgb <1,1,0>}}"                
            cad = cad + pov.povEsfera(x,y,z,"0.5", textura)
    return cad

def evoluciona(p, t):
    p2 = []
    
    for r in p:
        p2.append(r)
    R0 = 6
    inicio = 7    
    for i in range(n):
        for j in range(n):
            a = t - p[i][j].diaContagio
            if (p[i][j].estado==1):
                if (a>=inicio) and (a<inicio+R0):
                    malaSuerte = random.choice(p[i][j].contactos)
                    x =malaSuerte[0]
                    y = malaSuerte[1]
                    if (p2[x][y].estado==0):
                        p2[x][y].estado = 1
                        p2[x][y].diaContagio = t
                elif (a>14):
                    ale = random.random()
                    if (ale<0.98):
                        p2[i][j].estado=2
                    else:
                        p2[i][j].estado=4

    ##Vacuna empieza aquí
    if (t>40):  #empieza a vacunar en el dia 40
        for c in range (1000):  #Numero de personas que se vacunan
            alex = random.randint(0,n-1)    
            aley =  random.randint(0,n-1)
            if (p2[alex][aley].estado == 3):
                p2[alex][aley].estado = 5
            #Si la persona no está muerta, vacunada o inmune entonces se elige el tipo de vacuna que tendrá
            elif(p2[alex][aley].estado != 4 and p2[alex][aley].estado != 3 and p2[alex][aley].estado != 5):
                vac = random.choice(list(vacuna.keys()))
                if (vac =='Pfizer' ):
                    diasInmunidad=40
                    p2[alex][aley].tipoVacuna = 1
                    p2[alex][aley].diaVacuna +=1
                    diasInmunidad = t - p2[alex][aley].diaVacuna
                    #print(diasInmunidad)                    
                    if (diasInmunidad>40 ):
                        p2[alex][aley].estado = 0
                        diasInmunidad= diasInmunidad-t
                    diasInmunidad-=1    
                if (vac =='Sputnik' ):
                    diasInmunidad=30
                    p2[alex][aley].tipoVacuna = 2
                    p2[alex][aley].diaVacuna +=1
                    diasInmunidad = t - p2[alex][aley].diaVacuna
                    if (diasInmunidad>30):
                        p2[alex][aley].estado = 0
                        diasInmunidad= diasInmunidad-t
                    diasInmunidad-=1    
                if (vac =='Astrazeneca' ):
                    diasInmunidad=20
                    p2[alex][aley].tipoVacuna = 3
                    p2[alex][aley].diaVacuna +=1
                    diasInmunidad = t - p2[alex][aley].diaVacuna
                    if (diasInmunidad>20):
                        p2[alex][aley].estado = 0                          
                    diasInmunidad-=1
                if (vac =='Moderna' ):
                    diasInmunidad=10
                    p2[alex][aley].tipoVacuna = 4
                    p2[alex][aley].diaVacuna +=1
                    diasInmunidad = t - p2[alex][aley].diaVacuna
                    if (diasInmunidad>10):
                        p2[alex][aley].estado = 0 
                    diasInmunidad-=1    
                p2[alex][aley].estado = 3


     
    return (p2)




def cuenta(p, valor):
    cont = 0
    for i in range(n):
        for j in range(n):
            if (p[i][j].estado==valor):
                cont = cont + 1
    return cont

def cuentaVacuna(p, valor):
    cont = 0
    for i in range(n):
        for j in range(n):
            if (p[i][j].tipoVacuna==valor):
                cont = cont + 1
    return cont


'''
Efectividad de vacuna

100% 40 días
75%  30 días
50%  20 días
25%  10 días
'''

 
n = 100
vacuna = {'Pfizer': 100, 'Sputnik':100, 'Astrazeneca':100, 'Moderna': 100} #porcentaje de eficacia
datos = []
datosEnfermos = []
datosPfizer = []
datosSputnik = []
datosAstrazeneca = []
datosModerna = []
p = creaPobInicial(n)
p[n//2][n//2].estado=1
for t in range(200):
    p = evoluciona(p, t)
    enfermos = cuenta(p, 1)   
    sanos = cuenta(p, 0)
    recuperados = cuenta(p, 2)
    vacunados = cuenta(p, 3)
    muertos = cuenta(p, 4)
    pfizer = cuentaVacuna(p, 1)
    sputnik = cuentaVacuna(p, 2)
    astrazeneca = cuentaVacuna(p, 3)
    moderna = cuentaVacuna(p, 4)
    cad = pob2pov(p)
    num = str(t)
    archivo = open("salida" + num + ".pov", "w")
    archivo.write(cad)
    archivo.close()
    datos.append(enfermos+recuperados+muertos)  ##Grafica de contagios
    datosEnfermos.append(enfermos)        ##Grafica enfermos
    datosPfizer.append(pfizer)
    datosSputnik.append(sputnik)
    datosAstrazeneca.append(astrazeneca)
    datosModerna.append(moderna)
    print("dia: ",t, " ",enfermos, ":enfermos", " ",sanos, ":sanos"
          ,recuperados, ":recuperados", vacunados, ":vacunados" ,muertos, ":muertos")

plt.plot(datos)
plt.title('Contagios')
plt.show()
plt.plot(datosEnfermos)
plt.title('Enfermos')
plt.show()
plt.plot(datosPfizer, label='Pfizer')
plt.plot(datosSputnik, label = 'Sputnik')
plt.plot(datosAstrazeneca, label='Astrazeneca')
plt.plot(datosModerna, label = 'Moderna')
plt.title('Vacunas')
plt.legend()
plt.show()
   
