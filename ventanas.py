# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 18:52:17 2021

@author: USUARIO PC
"""

#librerias
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

import funciones

nintento = 0
################ VENTANA PRINCIPAL  #################
def vprincipal ():
    # NOMBRE DE LA RAIZ (VENTANA)
    rprincipal = Tk() 
    #ICONO Y NOMBRE DE LA VENTANA
    
    rprincipal.iconbitmap("Recursos/perro.ico")
    rprincipal.title("El_Fifas.exe")
    
    
    #CONFIGURACION DE LA VENTANA
    
    #rprincipal.geometry("1000x1000")
    #rprincipal.config(bg="red")  
    rprincipal.config(cursor="pirate")
    rprincipal.config(relief="sunken")
    #rprincipal.config(bd=25)
    
    
    #CREACION DE FRAME DE JUEGO
    
    fjuego = Frame(rprincipal) #Creacion del Frame
    fjuego.pack(side=LEFT)
    
    
    #CONFIGURACION DE FRAME
    #fjuego.config(bg="lightblue") #cambiar color de fondo 
    #fjuego.config(width="1000", height="1000") #cambiar tamaño
    #fjuego.config(bd=24) #cambiar el grosor del borde
    fjuego.config(relief="sunken")   #cambiar el tipo de borde
    fjuego.config(cursor="arrow")    #cambiar el tipo de cursor 
    
    """
    #LABEL
    Label(fjuego, text="Messi").grid(           row=1,column=0,sticky="e")
    Label(fjuego, text="CR7").grid(             row=1,column=1,sticky="e")
    Label(fjuego, text="Rafa Marquez").grid(    row=1,column=2,sticky="e")
    Label(fjuego, text="Aitor Cardone").grid(   row=1,column=3,sticky="e")
    Label(fjuego, text="Chicharito").grid(      row=1,column=4,sticky="e")
    
    """
    
    #########################################PERSONAS#########################################
    Label(fjuego,text="________________________________________________________Sospechosos________________________________________________________").grid(
                                                                                row = 0, column = 0, columnspan = 15, rowspan = 1, pady=5)
    #IMAGENES
    imgmessi = PhotoImage(file = r"Recursos/messi.png") 
    img1messi = imgmessi.subsample(4, 4) 
    Label(fjuego, image = img1messi).grid(                                      row = 1, column = 0, columnspan = 2, rowspan = 1, padx=5)
    
    imgcristiano = PhotoImage(file = r"Recursos/cristiano.png") 
    img1cristiano = imgcristiano.subsample(2, 2) 
    Label(fjuego, image = img1cristiano).grid(                                  row = 1, column = 2, columnspan = 2, rowspan = 1, padx=5)
    
    imgjoker = PhotoImage(file = r"Recursos/joker.png") 
    img1joker = imgjoker.subsample(5, 5) 
    Label(fjuego, image = img1joker).grid(                                      row = 1, column = 4, columnspan = 2, rowspan = 1, padx=5)
    
    imgpotro = PhotoImage(file = r"Recursos/potro.png") 
    img1potro = imgpotro.subsample(4, 4) 
    Label(fjuego, image = img1potro).grid(                                      row = 1, column = 6, columnspan = 2, rowspan = 1, padx=5)
    
    imgchicharito = PhotoImage(file = r"Recursos/chicharito.png") 
    img1chicharito = imgchicharito.subsample(3, 3) 
    Label(fjuego, image = img1chicharito).grid(                                 row = 1, column = 8, columnspan = 2, rowspan = 1, padx=5)
    
    #BOTONES
    bmessi = Button(fjuego, text="Messi",
                        command = lambda: [incremento(),funciones.cosa("messi","persona")]).grid(       row = 2, column = 0, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bcristiano = Button(fjuego, text="CR7",
                        command = lambda: [incremento(),funciones.cosa("CR7","persona")]).grid(         row = 2, column = 2, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bjoker = Button(fjuego, text="joker",
                        command = lambda: [incremento(),funciones.cosa("el joker","persona")]).grid(       row = 2, column = 4, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bpotro = Button(fjuego, text="potro",
                        command = lambda: [incremento(),funciones.cosa("el potro","persona")]).grid(       row = 2, column = 6, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bchicharito = Button(fjuego, text="chicharito",
                        command = lambda: [incremento(),funciones.cosa("el chicharito","persona")]).grid(  row = 2, column = 8, columnspan = 2, rowspan = 1, padx=5,pady=5)
    
    
        
        #########################################ARMAS#########################################
    Label(fjuego,text="________________________________________________________Armas________________________________________________________").grid(
                                                                                row = 4, column = 0, columnspan = 15, rowspan = 1, pady=20)
    #IMAGENES
    imgbalon = PhotoImage(file = r"Recursos/balon.png") 
    img1balon = imgbalon.subsample(3, 3) 
    Label(fjuego, image = img1balon).grid(                                      row = 5, column = 0, columnspan = 2, rowspan = 1, padx=5)
    
    imgbandera = PhotoImage(file = r"Recursos/bandera.png") 
    img1bandera = imgbandera.subsample(4, 4) 
    Label(fjuego, image = img1bandera).grid(                                    row = 5, column = 2, columnspan = 2, rowspan = 1, padx=5)
    
    imgtambor = PhotoImage(file = r"Recursos/tambor.png") 
    img1tambor = imgtambor.subsample(4, 4) 
    Label(fjuego, image = img1tambor).grid(                                     row = 5, column = 4, columnspan = 2, rowspan = 1, padx=5)
    
    imgtrofeo = PhotoImage(file = r"Recursos/trofeo.png") 
    img1trofeo = imgtrofeo.subsample(3, 3) 
    Label(fjuego, image = img1trofeo).grid(                                     row = 5, column = 6, columnspan = 2, rowspan = 1, padx=5)
    
    imgzapatos= PhotoImage(file = r"Recursos/zapatos.png") 
    img1zapatos = imgzapatos.subsample(4, 4) 
    Label(fjuego, image = img1zapatos).grid(                                    row = 5, column = 8, columnspan = 2, rowspan = 1, padx=5)
    
    #BOTONES
    bbalon = Button(fjuego, text="balon de oro",
                        command = lambda: [incremento(),funciones.cosa("el balon de oro","arma")]).grid(                          row = 6, column = 0, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bbandera = Button(fjuego, text="bandera",
                        command = lambda: [incremento(),funciones.cosa("la bandera","arma")]).grid(                             row = 6, column = 2, columnspan = 2, rowspan = 1, padx=5,pady=5)
    btambor = Button(fjuego, text="tambor",
                        command = lambda: [incremento(),funciones.cosa("el tambor","arma")]).grid(                               row = 6, column = 4, columnspan = 2, rowspan = 1, padx=5,pady=5)
    btrofeo= Button(fjuego, text="trofeo",
                        command = lambda: [incremento(),funciones.cosa("el trofeo","arma")]).grid(                                row = 6, column = 6, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bzapatos = Button(fjuego, text="zapatos",
                        command = lambda: [incremento(),funciones.cosa("los zapatos","arma")]).grid(                             row = 6, column = 8, columnspan = 2, rowspan = 1, padx=5,pady=5)
    
        #########################################LUGARES#########################################
    Label(fjuego,text="________________________________________________________Lugares________________________________________________________").grid( 
                                                                                row = 8, column = 0, columnspan = 15, rowspan = 1, pady=20)
    #IMAGENES
    imgbanos = PhotoImage(file = r"Recursos/banos.png") 
    img1banos = imgbanos.subsample(4, 4) 
    Label(fjuego, image = img1banos).grid(                                      row = 9, column = 0, columnspan = 2, rowspan = 1, padx=5)
    
    imgcabina = PhotoImage(file = r"Recursos/cabina.png") 
    img1cabina = imgcabina.subsample(4, 4) 
    Label(fjuego, image = img1cabina).grid(                                     row = 9, column = 2, columnspan = 2, rowspan = 1, padx=5)
    
    imgcancha = PhotoImage(file = r"Recursos/cancha.png") 
    img1cancha = imgcancha.subsample(4, 4) 
    Label(fjuego, image = img1cancha).grid(                                     row = 9, column = 4, columnspan = 2, rowspan = 1, padx=5)
    
    imggradas= PhotoImage(file = r"Recursos/gradas.png") 
    img1gradas = imggradas.subsample(3, 3) 
    Label(fjuego, image = img1gradas).grid(                                     row = 9, column = 6, columnspan = 2, rowspan = 1, padx=5)
    
    imgpalco= PhotoImage(file = r"Recursos/palco.png") 
    img1palco = imgpalco.subsample(4, 4) 
    Label(fjuego, image = img1palco).grid(                                      row = 9, column = 8, columnspan = 2, rowspan = 1, padx=5)
    
    #BOTONES
    bbanos = Button(fjuego, text="baños",
                        command = lambda: [incremento(),funciones.cosa("los baños","lugar")]).grid(                                 row = 10, column = 0, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bcabina = Button(fjuego, text="cabina",
                        command = lambda: [incremento(),funciones.cosa("la cabina","lugar")]).grid(                               row = 10, column = 2, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bcancha = Button(fjuego, text="cancha",
                        command = lambda: [incremento(),funciones.cosa("la cancha","lugar")]).grid(                               row = 10, column = 4, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bgradas= Button(fjuego, text="gradas",
                        command = lambda: [incremento(),funciones.cosa("las gradas","lugar")]).grid(                                row = 10, column = 6, columnspan = 2, rowspan = 1, padx=5,pady=5)
    bpalco = Button(fjuego, text="palco",
                        command = lambda: [incremento(),funciones.cosa("el palco","lugar")]).grid(                                 row = 10, column = 8, columnspan = 2, rowspan = 1, padx=5,pady=5)
    #CREACION DE FRAME DE PERRO************************************************************************************
    
    fperro = Frame(rprincipal) #Creacion del Frame
    fperro.pack(side=LEFT)
    
    
    #CONFIGURACION DE FRAME
    #fperro.config(bg="blue") #cambiar color de fondo 
    #finstucciones.config(width="300", height="500") #cambiar tamaño
    #fperro.config(bd=24) #cambiar el grosor del borde
    fperro.config(relief="sunken")   #cambiar el tipo de borde
    fperro.config(cursor="arrow")    #cambiar el tipo de cursor 
    
    #PREGUNTAR
    label1 = Label(fperro,text="preguntas permitidas: 5", font=("arial",20)).grid(             row = 4, column = 0, columnspan = 3, rowspan = 1, pady=5)
    
    #intentos permitido
    labelintento = Label(fperro,text="_____________", font=("arial",20)).grid(                            row = 0, column = 0, columnspan = 3, rowspan = 1, pady=5)
    labelintento = Label(fperro,text="_____________", font=("arial",20)).grid(                            row = 3, column = 0, columnspan = 3, rowspan = 1, pady=5)
    labelencabezado = Label(fperro,text="Pregunta al perro bermudez", font=("arial",20)).grid(    row = 1, column = 0, columnspan = 3, rowspan = 1)
    labelmensaje = Label(fperro,text="y resuelve el caso ", font=("arial",20)).grid(           row = 2, column = 0, columnspan = 3, rowspan = 1)
    
    imgperro = PhotoImage(file = r"Recursos/perro.png") 
    img1perro = imgperro.subsample(2, 2) 
    Label(fperro, image = img1perro).grid(                                      row = 5, column = 0, columnspan = 3, rowspan = 1, padx=5)
    
    Label(fperro,text="___________________________", font=("arial",20)).grid(
                                                                                 row = 6, column = 0, columnspan = 3, rowspan = 1, pady=5)
    Label(fperro,text="una vez descubierto el caso, envia el informe ", font=("arial",14)).grid(
                                                                                 row = 7, column = 0, columnspan = 3, rowspan = 1, pady=5)
    
    #INFORME
    #ASESINO
    PCR=StringVar()
    PCR.set("Asesino")
    opcionesasesino=["Asesino","messi","CR7","el joker","el potro","el chicharito"]
    opcionclase=OptionMenu(fperro, PCR,*opcionesasesino).grid(           row=8,column=0,padx=5,pady=5)
    
    #ARMA
    ACR=StringVar()
    ACR.set("Arma")
    opcionesarma=["Arma","el balon de oro","la bandera","el tambor","el trofeo","los zapatos"]
    opcionclase=OptionMenu(fperro, ACR,*opcionesarma).grid(                 row=8,column=1,padx=5,pady=5)
    
    #Lugar
    LCR=StringVar()
    LCR.set("Lugar")
    opcioneslugar=["Lugar","los baños","la cabina","la cancha","las gradas","el palco"]
    opcionclase=OptionMenu(fperro, LCR,*opcioneslugar).grid(               row=8,column=2,padx=5,pady=5)
    
    binforme = Button(fperro, text="enviar informe",command = lambda: funciones.resultado(PCR.get(),ACR.get(),LCR.get())).grid(                      row = 9, column = 1, columnspan = 1, rowspan = 1, padx=5,pady=5)
    
    bpro = Button(fperro, text="MODO PRO",
                        command = lambda: pro()).grid(                                 row = 10, column = 0, columnspan = 1, rowspan = 1, padx=5,pady=5)
    bnopro = Button(fperro, text="MODO FACIL",
                        command = lambda: nopro()).grid(                                 row = 10, column = 2, columnspan = 1, rowspan = 1, padx=5,pady=5)
    for i in range(5):
            for k in range(3,12,4):
                Label(fjuego,text="______",).grid(row=k,column=i*2)
                Label(fjuego,text="______",).grid(row=k,column=(i*2)+1)
                
    
    def pro():
        for i in range(5):
            for k in range(3,12,4):
                Label(fjuego,text="______",).grid(row=k,column=i*2)
                Label(fjuego,text="______",).grid(row=k,column=(i*2)+1)
    #CHECKBOX
    def nopro():
        valorcheck=0
        for i in range(5):
            for k in range(3,12,4):
                valorcheck += 1
                Radiobutton(fjuego, text="X",variable=valorcheck, value=0).grid(           row=k,column=i*2)
                Radiobutton(fjuego, text="O",variable=valorcheck, value=1).grid(           row=k,column=(i*2)+1)
    
    def incremento():
        global nintento
        nintento +=1
        if nintento == 1:
            label1 = Label(fperro,text="preguntas permitidas: 4", font=("arial",20)).grid(             row = 4, column = 0, columnspan = 3, rowspan = 1, pady=5)
        if nintento == 2:
            label1 = Label(fperro,text="preguntas permitidas: 3", font=("arial",20)).grid(             row = 4, column = 0, columnspan = 3, rowspan = 1, pady=5)
        if nintento == 3:
            label1 = Label(fperro,text="preguntas permitidas: 2", font=("arial",20)).grid(             row = 4, column = 0, columnspan = 3, rowspan = 1, pady=5)
        if nintento == 4:
            label1 = Label(fperro,text="preguntas permitidas: 1", font=("arial",20)).grid(             row = 4, column = 0, columnspan = 3, rowspan = 1, pady=5)
        if nintento == 5:
            label1 = Label(fperro,text="No quedan más intentos", font=("arial",20)).grid(             row = 4, column = 0, columnspan = 3, rowspan = 1, pady=5)
            label2= Label(fjuego,text="Por favor ingresa tus resultados", font=("arial",20)).grid(              row = 0, column = 0, columnspan = 15, rowspan = 15, pady=5)
           

    # Start the GUI 
    rprincipal.mainloop()


    
def vmensaje (intento,encabezado,mensaje):
    #CREACION DE FRAME DE RESPUESTAS
     # NOMBRE DE LA RAIZ (VENTANA)
    rmensaje = Tk() 
    #ICONO Y NOMBRE DE LA VENTANA
    
    rmensaje.iconbitmap("Recursos/perro.ico")
    rmensaje.title("Mensaje_El_Fifas.exe")
    
    #CONFIGURACION DE LA VENTANA
    
    rmensaje.config(cursor="pirate")
    rmensaje.config(relief="sunken")

    fmensaje = Frame(rmensaje) #Creacion del Frame
    fmensaje.pack()
    
    #CONFIGURACION DE FRAME
    fmensaje.config(relief="sunken")   #cambiar el tipo de borde
    fmensaje.config(cursor="arrow")    #cambiar el tipo de cursor
    global nintento 
    nintento =intento
    
    Label(fmensaje,text="intento numero", font=("arial",20)).grid(              row = 0, pady=5)

    intento = str(intento) + " de 5"
    
    labelintento = Label(fmensaje,text=intento, font=("arial",20)).grid(              row = 1, pady=5)
    Label(fmensaje,text=encabezado, font=("arial",20)).grid(                            row = 2, pady=10)
    Label(fmensaje,text=mensaje, font=("arial",20)).grid(                            row = 3, pady=10)
    
    
    rmensaje.mainloop()

def vfinal ():
    #CREACION DE FRAME DE RESPUESTAS
     # NOMBRE DE LA RAIZ (VENTANA)
    rfinal = Tk() 
    #ICONO Y NOMBRE DE LA VENTANA
    
    rfinal.iconbitmap("Recursos/perro.ico")
    rfinal.title("No_intentos_El_Fifas.exe")
    
    #CONFIGURACION DE LA VENTANA
    
    rfinal.config(cursor="pirate")
    rfinal.config(relief="sunken")

    ffinal = Frame(rfinal) #Creacion del Frame
    ffinal.pack()
    
    #CONFIGURACION DE FRAME
    ffinal.config(relief="sunken")   #cambiar el tipo de borde
    ffinal.config(cursor="pirate")    #cambiar el tipo de cursor
    
    label1 = Label(ffinal,text="No quedan más intentos", font=("arial",20)).grid(             row = 0, column = 0, pady=5)
    label2= Label(ffinal,text="Por favor ingresa tus resultados", font=("arial",20)).grid(              row = 1, column = 0,   pady=5)
    
    
    rfinal.mainloop()
      
def vresultado(mensaje,mensaje2,mensaje3):
    #CREACION DE FRAME DE RESPUESTAS
     # NOMBRE DE LA RAIZ (VENTANA)
    rresultado = Tk() 
    #ICONO Y NOMBRE DE LA VENTANA
    
    rresultado.iconbitmap("Recursos/perro.ico")
    rresultado.title("No_intentos_El_Fifas.exe")
    
    #CONFIGURACION DE LA VENTANA
    
    rresultado.config(cursor="pirate")
    rresultado.config(relief="sunken")

    fresultado = Frame(rresultado) #Creacion del Frame
    fresultado.pack()
    
    #CONFIGURACION DE FRAME
    fresultado.config(relief="sunken")   #cambiar el tipo de borde
    fresultado.config(cursor="arrow")    #cambiar el tipo de cursor
    
    Label(fresultado,text=mensaje, font=("arial",20)).grid(             row = 0, column = 0, pady=5)
    Label(fresultado,text=mensaje2, font=("arial",20)).grid(              row = 1, column = 0,   pady=5)
    Label(fresultado,text=mensaje3, font=("arial",20)).grid(             row = 2, column = 0, pady=5)
    
    
    rresultado.mainloop()    

    
def vbotarga ():
    #CREACION DE FRAME DE RESPUESTAS
     # NOMBRE DE LA RAIZ (VENTANA)
    rbotarga = Tk() 
    #ICONO Y NOMBRE DE LA VENTANA
    
    rbotarga.iconbitmap("Recursos/perro.ico")
    rbotarga.title("No_intentos_El_Fifas.exe")
    
    #CONFIGURACION DE LA VENTANA
    
    rbotarga.config(cursor="pirate")
    rbotarga.config(relief="sunken")

    fbotarga = Frame(rbotarga) #Creacion del Frame
    fbotarga.pack()
    
    #CONFIGURACION DE FRAME
    fbotarga.config(relief="sunken")   #cambiar el tipo de borde
    fbotarga.config(cursor="pirate")    #cambiar el tipo de cursor
    
    label1 = Label(fbotarga,text="con ayuda del Perro Bermudez, investiga quién asesinó la botarga de los zorros", font=("arial",20)).grid(             row = 0, column = 0, pady=5)
    
    
    rbotarga.mainloop()






















