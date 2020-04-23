#CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERÍAS NECESARIAS.
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os
import pandas as pd

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x200")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("ENTRAR AL PROGRAMA")#TITULO DE LA VENTANA
    Label(text="Escoja su opción".upper(), bg="#F9A409",fg='white', width="300", height="2", font=13).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg='#34B5E6',fg='white', command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg='#67C81E',fg='white', command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"11
 
    Label(ventana_registro, text="Introduzca datos").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, command = registro_usuario).pack() #BOTÓN "Registrarse"

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    global us
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        us=usuario1
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".

#------------------------------------------------------root (ventana principal del programa...)
def vent():
    borrar_exito_login()
    ventana_principal.destroy()
    vent=Tk()
    vent.title('Medidor de calidad del suelo')
    vent.geometry("500x350")
    bg_image1=PhotoImage(file="resources/BG.png")
    Label(vent, image=bg_image1).place(x=0, y=0, relwidth=1, relheight=1)
    vent.resizable(False, False)#-----------------Bloquear redimencion de la ventana

    
    
    #choices = ['GB', 'MB', 'KB']
    #variable = StringVar(vent)
    #variable.set('Fertilizante')
    #w = OptionMenu(vent, variable, *choices)
    #w.place(x=100,y=300)
    
    ph=StringVar()#ph xd
    ph.set(0)
    sal=StringVar()#salinidad
    sal.set(0)
    urea=StringVar()#urea
    urea.set(0)
    fosf=StringVar()#Fósforo
    fosf.set(0)
    pot=StringVar()#potacio
    pot.set(0)
       

    uss=str(us)
    texto="HOLA "+uss.upper()#------------------------Muestra el nombre de usuario en la ventana...
    Label(vent,text=texto,bg='#39b200',fg='white').place(x=430,y=10)
    Label(vent,text=uss[0].upper(),bg='#39b200',fg='white', font =('arial', 11, 'bold')).place(x=395,y=9)
    Label(vent,text="ESTADO NUTRICIONAL DEL SUELO",bg='#39b200', fg='white', font = 'bold').place(x=20,y=9)
    n=80

    Label(vent, text='Ingresar los datos actuales',bg='white').place(x=20+30-10,y=65)

    Label(vent,text="PH (Valor)",bg='white').place(x=20+30-10 , y=20+n-10 )
    Entry(vent,textvariable=ph).place(x=20+30-10 , y=20*2+n-10 )
    
    Label(vent,text="Etapa actual del arroz",bg='white').place(x=20+30-10 , y=20*3+n-3 )
    #Entry(vent,textvariable=sal).place(x=20 , y=20*4+n )
    comboExample = ttk.Combobox(vent, 
                            values=[
                                    "Vegetativa", 
                                    "Reproductiva",
                                    "Maduracion"])
    #print(dict(comboExample))

    comboExample.place(x=20+30-10 , y=20*4+n-3)
    comboExample.current(1)

    #print(comboExample.current(), comboExample.get())
    

    Label(vent,text="Urea (%)",bg='white').place(x=20+30-10 , y=20*5+n+3 )
    Entry(vent,textvariable=urea).place(x=20+30-10 , y=20*6+n+3 )
    

    Label(vent,text="Súper Fosfato Triple (%)",bg='white').place(x=20+30-10 , y=20*7+n+6 )
    Entry(vent,textvariable=fosf).place(x=20+30-10 , y=20*8+n+6 )
    +30

    Label(vent,text="Muriato de Potasio (Valor)",bg='white').place(x=20+30-10 , y=20*9+n+9 )
    Entry(vent,textvariable=pot).place(x=20+30-10 , y=20*10+n+9 )

    def save():
        vph=ph.get() 
        vsall=comboExample.get()
        if vsall == 'Vegetativa':
            vsall='Alta'
        elif vsall == 'Reproductiva':
            vsall='Maxima'
        elif vsall == 'Maduracion':
            vsall='Baja'
        else:
            vsall='--'

        vurea=urea.get()
        vfosf=fosf.get()
        vpot=pot.get()

        lista=['PH', float(vph), 'Sensibilidad', vsall, 'Urea', float(vurea), 'S. Fosfato', float(vfosf), 'M. de Potasio', float(vpot) ]

        df= pd.DataFrame()
        #--------------------------crea columnas  ---------- py -m pip install xlwt
        df['Variables']=lista[0::2]
        df['Info']=lista[1::2]
        
        #------------------------- convertir  EXCEL
        df.to_excel('datos.xls', index=False)

        #os.system('datos.xls')
        messagebox.showinfo("listo","Archivo excel Guardado")


    
    def comp():

        vph=ph.get()
        '''vsal=sal.get()
                                print("--",vsal)'''
        vsall=comboExample.get()
 
        vurea=urea.get()
        vurea=float(vurea)
        vfosf=fosf.get()
        vfosf=float(vfosf)
        vpot=pot.get()
        vpot=float(vpot)

        bph=0
        bur=0

        #---------------------------------------------------- logica para el ph
        if float(vph)==6.6 :
            optph="✔ El nivel de Ph es optimo."
            bph=True

        elif float(vph)< 5.5 :
            optph="✖ La acidez del suelo es muy alta."
            bph=False

        elif float(vph)>=5.5 and float(vph)<=5.9 :
            optph="✔ El suelo es moderadamente acido."
            bph=True

        elif float(vph)>=6 and float(vph)<6.6 :
            optph="✔ El suelo tiene un nivel aceptable de Ph."
            bph=True

        elif float(vph)>6.6 and float(vph)<=7.3:
            optph="✖ El suelo tiene un nivel neutro."
            bph=True

        elif float(vph)>7.4:
            optph="✖ La alcalinidad del suelo es muy alta."
            bph=False

        #---------------------------------------------------- logica para la salinidad
        if vsall == 'Vegetativa':
        	optsal="✖ La planta es altamente sensible a la salinidad"
        elif vsall == 'Reproductiva':
        	optsal="✖ La planta es totalmente sensible a la salinidad"
        elif vsall == 'Maduracion':
        	optsal="✔ La planta no es muy sensible a la salinidad"

        #---------------------------------------------------- logica para la urea
        if vurea >= 20:
            optur="✖ El suelo tiene mucha Urea, se perderá volatilizacion"
            bur=False

        elif vurea>0:
            optur="✔ El suelo cumple con el porcentaje aceptado de Urea"
            bur=True

        else:
        	optur="✖ El suelo no contiene Urea"

            
        #---------------------------------------------------- logica para fosforo
        if vfosf > 100:
            optf="✖ El suelo contiene mucho súper fosfato triple"
            

        elif vfosf>0:
            optf="✔ EL suelo cumple con el porcentaje aceptado de súper fosfato triple"
            

        else:
        	optf="✖ EL suelo no contiene súper fosfato triple"


        #---------------------------------------------------- logica para fosforo
        if vpot > 100:
            optpo="✖ EL suelo exede de los 100 kilos de muriato de potacio"
            

        elif vpot>0:
            optpo="✔ El suelo contiene una cantidad permitida de muriato de potacio"


        else:
        	optpo="✖ El suelo no contiene muriato de potacio"

        

        if bph==True:
        	if bur==True:
        		valid='El suelo es apto'.upper()
        	else:
        		valid='El suelo no es apto'.upper()
        else:
        	valid='El suelo no es apto'.upper()

        ntxt=optph+'\n'+optsal+'\n'+optur+'\n'+optf+'\n'+optpo+'\n'+'\n'+'<< '+valid+'>>'



        
        messagebox.showinfo("informacion", ntxt)#------------------------------------------- message box

    btnimage=PhotoImage(file='resources/btn.png')
    Button(vent, image=btnimage, command=comp).place(x=300, y=100)

    btnimage2=PhotoImage(file='resources/btnxls.png')
    Button(vent, image=btnimage2, command=save).place(x=400, y=100)



    vent.mainloop()

# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=vent).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario = nombre_usuario.get()
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario,"w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
 
ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.
 
