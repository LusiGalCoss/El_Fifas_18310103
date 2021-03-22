# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 18:49:40 2021

@author: USUARIO PC
"""

import random
#funciones
import funciones
import ventanas

#VARIABLES NECESARIAS
intento = 0
ventana = 0
seed = [0,1,2,3,4]
#AREGLOS INICIALES
P = ["messi","CR7","el joker","el potro","el chicharito"]
A = ["el balon de oro","la bandera","el tambor","el trofeo","los zapatos"]
L = ["los baños","la cabina","la cancha","las gradas","el palco"]

#ARREGLOS PREGUNTADOS
PP = ["messi","CR7","el joker","el potro","el chicharito"]
AP = ["el balon de oro","la bandera","el tambor","el trofeo","los zapatos"]
LP = ["los baños","la cabina","la cancha","las gradas","el palco"]

#RANDOMIZAR LISTAS
random.shuffle(P)
random.shuffle(A)
random.shuffle(L)
random.shuffle(seed)
#OBTENER CULPABLES
PC = P.pop(0)
AC = A.pop(0)
LC = L.pop(0)
print(PC)
print(AC)
print(LC)

#MENSAJES ENCABEZADOS
ME = ["Ahora que recuerdo...","Ya recordé...","Lo que pasó fue que...","si, de hecho...","deja pienso mmmm oh si..."]

MC = ["FIRMALA GIO, FIRMALA, FIRMALA",
      "TUYA, MÍA, TENLA, TE LA PRESTO","- ¡ZAMBOMBAZO!",
      "¡UF, UF Y RECONTRA UF!","¡DONDE LAS ARAÑAS TEJEN SU NIDO!",
      "QUISO HACERLA DE SEXTO AÑO...y la terminó de Kinder garden"]
random.shuffle(ME)
random.shuffle(MC)


def cosa(nombre,cosa):
    # aumentar intento


    global intento 
    intento +=1
    #checar si es culpable
    if intento <=5:
        if nombre == PC or nombre == AC or nombre == LC:
            #caso culpable
            encabezado = MC[0]
            MC.pop(0)
            mensajec(nombre,cosa,encabezado,intento)
        if nombre != PC and nombre != AC and nombre != LC: 
            #caso inocente
            inocente(nombre,cosa)
    
    if intento >5:  
        ventanas.vfinal()

    

def inocente (nombre,cosa):
    print(PP)
    #checar si ya se preguntó antes
    #eliminarlo de preguntados
    preguntado=0
    if cosa == "persona":
        if nombre in PP: #aun no se pregunta
            PP.remove(nombre)
        else: #ya se preguntó
            preguntado = 1
    if cosa == "arma":
        if nombre in AP: #aun no se pregunta
            AP.remove(nombre)
        else: #ya se preguntó
            preguntado = 1
    if cosa == "lugar":
        if nombre in LP: #aun no se pregunta
            LP.remove(nombre)
        else: #ya se preguntó
            preguntado = 1
    if preguntado == 0:
        encabezado = ME[0]
        ME.pop(0)
    if preguntado == 1:
        encabezado = "Ya te lo había dicho"
    print (str(preguntado)  +" preguntado")
    mensajei(nombre,encabezado,intento)
    
def mensajei(nombre,encabezado,intento):
    
    #poner los 4 mensajes que conforman la historia
    #***********historia 1*****************
    if seed[0] == 0:
        #1
        if nombre == P[0] or nombre == A[0] or nombre == L[0]:
            mensaje = "cuando entré a "+L[0]+"," +P[0] +" estaba muy tranquilo sujetando " +A[0]
            if P[0] in PP:
                PP.remove(P[0])
            if A[0] in AP:
                AP.remove(A[0])
            if L[0] in LP:
                LP.remove(L[0])
            
            
        #2
        if nombre == P[1] or nombre == A[1] or nombre == L[1]:
            mensaje = "justo iba saliendo de " + L[1] + " cuando me topé con " + P[1] + ", lo saludé, tenía " + A[1] + " en la mano, pero se veía tranquilo" 
            
            if P[1] in PP:
                PP.remove(P[1])
            if A[1] in AP:
                AP.remove(A[1])
            if L[1] in LP:
                LP.remove(L[1])
            
        #3
        if nombre == P[2] or nombre == A[2] or nombre == L[2]:
            mensaje = "yo fui a " + L[2] + " para buscar " + A[2] + " pero no lo encontraba y " + P[2] + " me ayudó a busacrlo, lo encontramos y fuimos a comer"
            
            if P[2] in PP:
                PP.remove(P[2])
            if A[2] in AP:
                AP.remove(A[0])
            if L[2] in LP:
                LP.remove(L[2])
            
        #4
        if nombre == P[3] or nombre == A[3] or nombre == L[3]:
            mensaje = "saludé a mi compita  " + P[3] + " fuimos " + L[3] + " para recoger " + A[3] +", pero no vimos nada sospechoso"
            
            if P[3] in PP:
                PP.remove(P[3])
            if A[3] in AP:
                AP.remove(A[3])
            if L[3] in LP:
                LP.remove(L[3])

    #***********historia 2*****************
    if seed[0] == 1:
        #1
        if nombre == P[0] or nombre == P[1] or nombre == A[0]:
            mensaje = "de hecho "+P[0]+" y " +P[1] +" registrando " +A[0]+" en el inventario, estuvieron ocupados todo el dia"
            if P[0] in PP:
                PP.remove(P[0])
            if P[1] in PP:
                PP.remove(P[1])
            if A[0] in AP:
                AP.remove(A[0])
            
            
        #2
        if nombre == L[1] or nombre == A[1] or nombre == L[0]:
            mensaje =  "yo entré a "+L[1]+ " buscando " +A[1] +" vi todo en orden peró no lo encontré, así que fui a "+ L[0]+ "y lo encontré, estaba justo en su lugar"
            
            if L[1] in LP:
                LP.remove(L[1])
            if A[1] in AP:
                AP.remove(A[1])
            if L[0] in LP:
                LP.remove(L[0])
            
        #3
        if nombre == P[2] or nombre == A[2] or nombre == P[3]:
            mensaje = "no te preocupes, yo le di "+A[2]+" a " +P[2]+" para que se lo diera a "+P[3]
            
            if P[2] in PP:
                PP.remove(P[2])
            if A[2] in AP:
                AP.remove(A[0])
            if P[3] in PP:
                PP.remove(P[3])
            
        #4
        if nombre == L[2] or nombre == A[3] or nombre == L[3]:
            mensaje = "yo mismo moví"+A[3]+ " de "+L[2]+" a "+L[3]
            
            if P[3] in PP:
                PP.remove(P[3])
            if A[3] in AP:
                AP.remove(A[3])
            if L[3] in LP:
                LP.remove(L[3])
    
    #***********historia 3*****************
    if seed[0] == 2:
        #1
        if nombre == P[0] or nombre == P[1] or nombre == A[0]:
            mensaje = P[0]+" estaba reparando " +A[0] +" mientras " +P[1]+" le chalaneaba, no pudieron ser ellos"
            if P[0] in PP:
                PP.remove(P[0])
            if P[1] in PP:
                PP.remove(P[1])
            if A[0] in AP:
                AP.remove(A[0])
            
            
        #2
        if nombre == L[1] or nombre == A[1] or nombre == L[0]:
            mensaje =  +L[1]+ " estaba en orden y " +L[0] +"también, "+ A[1] + " estaba reluciente "
            
            if L[1] in LP:
                LP.remove(L[1])
            if A[1] in AP:
                AP.remove(A[1])
            if L[0] in LP:
                LP.remove(L[0])
            
        #3
        if nombre == P[2] or nombre == A[2] or nombre == P[3]:
            mensaje = "no encontraba "+A[2]+" así que fui con " +P[2]+" y me dijo que "+P[3]+" lo tenía, todo en orden con eso"
            
            if P[2] in PP:
                PP.remove(P[2])
            if A[2] in AP:
                AP.remove(A[0])
            if P[3] in PP:
                PP.remove(P[3])
            
        #4
        if nombre == L[2] or nombre == A[3] or nombre == L[3]:
            mensaje = A[3]+ " no pudo ser el arma, fui a "+L[2]+" y  "+L[3] +"y vi todo normal, de hecho recordé que me lo había llevado a mi casa haha"
            
            if P[3] in PP:
                PP.remove(P[3])
            if A[3] in AP:
                AP.remove(A[3])
            if L[3] in LP:
                LP.remove(L[3])
        
    #***********historia 4*****************
    if seed[0] == 3:
        #1
        if nombre == P[0] or nombre == P[1] or nombre == A[0]:
            mensaje = "de hecho "+P[0]+" y " +P[1] +" registrando " +A[0]+" en el inventario, estuvieron ocupados todo el dia"
            if P[0] in PP:
                PP.remove(P[0])
            if P[1] in PP:
                PP.remove(P[1])
            if A[0] in AP:
                AP.remove(A[0])
            
            
        #2
        if nombre == L[1] or nombre == A[1] or nombre == L[0]:
            mensaje =  "yo entré a "+L[1]+ " buscando " +A[1] +" vi todo en orden peró no lo encontré, así que fui a "+ L[0]+ "y lo encontré, estaba justo en su lugar"
            
            if L[1] in LP:
                LP.remove(L[1])
            if A[1] in AP:
                AP.remove(A[1])
            if L[0] in LP:
                LP.remove(L[0])
            
        #3
        if nombre == P[2] or nombre == A[2] or nombre == P[3]:
            mensaje = "no te preocupes, yo le di "+A[2]+" a " +P[2]+" para que se lo diera a "+P[3]
            
            if P[2] in PP:
                PP.remove(P[2])
            if A[2] in AP:
                AP.remove(A[0])
            if P[3] in PP:
                PP.remove(P[3])
            
        #4
        if nombre == L[2] or nombre == A[3] or nombre == L[3]:
            mensaje = "yo mismo moví"+A[3]+ " de "+L[2]+" a "+L[3]
            
            if P[3] in PP:
                PP.remove(P[3])
            if A[3] in AP:
                AP.remove(A[3])
            if L[3] in LP:
                LP.remove(L[3])
    
    #***********historia 5*****************
    if seed[0] == 4:
        #1
        if nombre == P[0] or nombre == P[1] or nombre == A[0]:
            mensaje = "de hecho "+P[0]+" y " +P[1] +" registrando " +A[0]+" en el inventario, estuvieron ocupados todo el dia"
            if P[0] in PP:
                PP.remove(P[0])
            if P[1] in PP:
                PP.remove(P[1])
            if A[0] in AP:
                AP.remove(A[0])
            
            
        #2
        if nombre == L[1] or nombre == A[1] or nombre == L[0]:
            mensaje =  "yo entré a "+L[1]+ " buscando " +A[1] +" vi todo en orden peró no lo encontré, así que fui a "+ L[0]+ "y lo encontré, estaba justo en su lugar"
            
            if L[1] in LP:
                LP.remove(L[1])
            if A[1] in AP:
                AP.remove(A[1])
            if L[0] in LP:
                LP.remove(L[0])
            
        #3
        if nombre == P[2] or nombre == A[2] or nombre == P[3]:
            mensaje = "no te preocupes, yo le di "+A[2]+" a " +P[2]+" para que se lo diera a "+P[3]
            
            if P[2] in PP:
                PP.remove(P[2])
            if A[2] in AP:
                AP.remove(A[0])
            if P[3] in PP:
                PP.remove(P[3])
            
        #4
        if nombre == L[2] or nombre == A[3] or nombre == L[3]:
            mensaje = "yo mismo moví"+A[3]+ " de "+L[2]+" a "+L[3]
            
            if P[3] in PP:
                PP.remove(P[3])
            if A[3] in AP:
                AP.remove(A[3])
            if L[3] in LP:
                LP.remove(L[3])
    
    ventanas.vmensaje(intento,encabezado,mensaje)

    
def mensajec (nombre,cosa,encabezado,intento):
    
    #personaje culpable:
    if cosa == "persona":
        mensaje = "claro!, de hecho " + nombre + " estaba bieeeeen nervioso, lo enconté a un lado de " + AP[0] + " no creo que esa haya sido el arma "
        if nombre in PP:
            PP.remove(nombre)
        AP.pop(0) 
    
    if cosa == "arma":
        mensaje = "claro! " + nombre + " estaba ensangrentado, lo vi en " + LP[0] + " aunque no haya sido ahí, ya encontramos el arma "
        if nombre in AP:
            AP.remove(nombre)
        AP.pop(0)
        
    if cosa == "lugar":
        mensaje = "claro! " + nombre + " ese sitio me parecio sospechoso desde un inicio " + PP[0] + " y yo vimos ese lugar todo desordenado y en todo el dia no nos separamos"
        if nombre in LP:
            LP.remove(nombre)
        LP.pop(0)
   
    ventanas.vmensaje(intento,encabezado,mensaje)
    

def resultado(PCR,ACR,LCR):
    mensaje3 = "Respuesta: fue "+PC+" con "+AC+" en "+LC
    print(PC)
    print(AC)
    print(LC)
    if  PCR == PC and ACR == AC and LCR == LC:
        mensaje = "¡AFICIONADOS QUE VIVEN LA INTENSIDAD DEL FUTBOL!"
        mensaje2 = "Has resuelto el caso correctamente"
    else:
        mensaje = "LA TENÍA, ERA SUYA... Y LA DEJÓ IR"
        mensaje2 = "No has logrado resolver el caso correctamente"
    ventanas.vresultado(mensaje,mensaje2,mensaje3)
        
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
    
    
    
    
    