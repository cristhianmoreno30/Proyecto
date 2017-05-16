#Importamos Las librerias
from tkinter import *
import time


#####FUNCIONES###########
###############################################


## niveles ##
global Nivel
Nivel= 1


def menu_niveles():
    btn_niveles=Button(ventana,text="Dificultad",font=("Century",15),command=menu_niveles,width=9,bg="black",fg="peru").place_forget()
    btn_jugadores=Button(ventana,text="Jugadores",font=("Century",15),width=9,bg="black",fg="peru").place_forget()
    btn_salir=Button(ventana,text="Salir",font=("Century",15),command=ventana.destroy,width=9,bg="black",fg="peru").place_forget()
    lbl_fondo_niveles=Label(image=img_fondo_niveles).place(x=0,y=0)
    btn_nvl1=Button(ventana,text="1",font=("Century",15),command=inicio1,width=2,bg="black",fg="peru").place(x=600,y=680)
    btn_nvl2=Button(ventana,text="2",font=("Century",15),command=Nivel2,width=2,bg="black",fg="peru").place(x=660,y=680)
    btn_nvl3=Button(ventana,text="3",font=("Century",15),width=2,bg="black",fg="peru").place(x=720,y=680)
    btn_nvl4=Button(ventana,text="4",font=("Century",15),width=2,bg="black",fg="peru").place(x=780,y=680)
    btn_nvl5=Button(ventana,text="5",font=("Century",15),width=2,bg="black",fg="peru").place(x=840,y=680)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=1179,y=859)
    return 

##comandos para botones de nivel###
def Nivel2 ():
    Nivel= 2


##funcion de regreso ##
def regreso():
    lbl_fondo_menu=Label(image=img_fondo_menu).place(x=0,y=0)
    lbl_fondo_niveles=Label(image=img_fondo_niveles).place_forget
    btn_jugadores=Button(ventana,text="Jugadores",font=("Century",15),command=menu_jugadores,width=9,bg="black",fg="peru").place(x=900,y=570)
    btn_salir=Button(ventana,text="Salir",font=("Century",15),command=ventana.destroy,width=9,bg="black",fg="peru").place(x=900,y=640)
    btn_nvl1=Button(ventana,text="1",font=("Century",15),width=2,bg="black",fg="peru").place_forget()
    btn_nvl2=Button(ventana,text="2",font=("Century",15),width=2,bg="black",fg="peru").place_forget()
    btn_nvl3=Button(ventana,text="3",font=("Century",15),width=2,bg="black",fg="peru").place_forget()
    btn_nvl4=Button(ventana,text="4",font=("Century",15),width=2,bg="black",fg="peru").place_forget()
    btn_nvl5=Button(ventana,text="5",font=("Century",15),width=2,bg="black",fg="peru").place_forget()
    btn_player1=Button(ventana,text="1 Jugador",font=("Century",15),width=9,bg="black",fg="peru").place_forget()
    btn_player2=Button(ventana,text="2 Jugadores",font=("Century",15),width=9,bg="black",fg="peru").place_forget()
    return

##funciones jugadores##
def menu_jugadores ():
    lbl_fondo_menu=Label(image=img_fondo_menu).place(x=0,y=0)
    btn_niveles=Button(ventana,text="Dificultad",font=("Century",15),command=menu_niveles,width=9,bg="black",fg="peru").place_forget()
    btn_jugadores=Button(ventana,text="Jugadores",font=("Century",15),width=9,bg="black",fg="peru").place_forget()
    btn_salir=Button(ventana,text="Salir",font=("Century",15),command=ventana.destroy,width=9,bg="black",fg="peru").place_forget()
    btn_player1=Button(ventana,text="1 Jugador",font=("Century",15),command=jugador1,width=9,bg="black",fg="peru").place(x=610,y=500)
    btn_player2=Button(ventana,text="2 Jugadores",font=("Century",15),command=jugador2,width=9,bg="black",fg="peru").place(x=1150,y=500)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=1179,y=859)
    return

##jugador1:
def jugador1():
    global player1
    lbl_fondo_1jugador=Label(image=img_fondo_1jugador).place(x=0,y=0)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=1179,y=859)
    player1=StringVar ()
    text_player1=Entry(ventana,textvariable=player1,bg="peru",width=25).place(x=770,y=505)
    btn_inicio=Button(ventana,text="Iniciar",font=("Century",20),command=menu_niveles,width=20,bg="black",fg="orange").place(x=800,y=815)
    return

##duo jugadores:
def jugador2():
    global player1
    global player2
    lbl_fondo_2jugador=Label(image=img_fondo_2jugadores).place(x=0,y=0)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=1179,y=859)
    player1=StringVar ()
    text_player1=Entry(ventana,textvariable=player1,bg="peru",width=25).place(x=770,y=505)
    player2=StringVar ()
    text_player2=Entry(ventana,textvariable=player2,bg="peru",width=25).place(x=770,y=615)
    btn_inicio=Button(ventana,text="Iniciar",font=("Century",20),command=inicio_2,width=20,bg="black",fg="orange").place(x=800,y=815)
    return
###INICIO #####
##solo##
def inicio1 ():
    ventana.withdraw()
    ventana2.deiconify()
    lbl_player1=Label(ventana2,text=player1.get(),bg="black",fg="peru",font=("Century",20,'bold' )).place(x=1000,y=150)
    lienzo.pack()
    return

##duo##
def inicio_2 ():
    ventana.withdraw()
    ventana3.deiconify()
    lbl_player1=Label(ventana3,text=player1.get(),bg="black",fg="peru",font=("Century",18 )).place(x=1415,y=150)
    lbl_player2=Label(ventana3,text=player2.get(),bg="black",fg="peru",font=("Century",18 )).place(x=15,y=150)
    lienzo_duo.pack()
    return

    
###########FUNCIONES CON EL TECLADO########
##modo solo ###

def car_main_move(tecla):
    if tecla.char == "q":
        while True:
            print(lienzo.coords(mapa_1)[1])
            lienzo.move(mapa_1,0,10)  ###limite 100####
            ventana2.update()  
            time.sleep(0.018)   
    if tecla.char == "a":
        lienzo.move(rojo,-3,0)
        lienzo.after(1,lienzo.move(rojo,-3,0))
    elif tecla.char=="d":
        lienzo.move(rojo,3,0)
        lienzo.after(1,lienzo.move(rojo,3,0))
    return

## modo duo ##

def car_main_move_1(tecla):
    if tecla.char == "a":
        lienzo_duo.move(rojo,-3,0)
        lienzo_duo.after(0,lienzo_duo.move(rojo,-3,0))
    if tecla.char=="d":
        lienzo_duo.move(rojo,3,0)
        lienzo_duo.after(0,lienzo_duo.move(rojo,3,0))
    if tecla.char == "j":
        lienzo_duo.move(morado,-3,0)
        lienzo_duo.after(0,lienzo_duo.move(morado,-3,0))
    if tecla.char=="l":
        lienzo_duo.move(morado,3,0)
        lienzo_duo.after(0,lienzo_duo.move(morado,3,0))
    return

    
    
############################################################

    
    



    
    
    
############################################################


#######CREANDO LA VENTANA###########################

#(1)Se crea la ventana del tk
ventana = Tk()
#(2)Nombre de la ventana
ventana.title("Road Figther")
#(3)Tamaño y posicion de la ventana ( ancho x alto + posX + posY )
ventana.geometry ("1300x900+300+50")

##Fondos
img_fondo_niveles=PhotoImage(file="fondo_menu_niveles.png")
img_fondo_menu=PhotoImage(file="fondo_menu.png")
img_fondo_1jugador=PhotoImage(file="fondo_menu_player1.png")
img_fondo_2jugadores=PhotoImage(file="fondo_menu_player2.png")
lbl_fondo_menu=Label(image=img_fondo_menu).place(x=0,y=0)

##botenes de jugadores
btn_jugadores=Button(ventana,text="Jugadores",font=("Century",15),command=menu_jugadores,width=9,bg="black",fg="peru").place(x=900,y=570)


##botone niveles
#btn_niveles=Button(ventana,text="Dificultad",font=("Century",15),command=menu_niveles,width=9,bg="black",fg="peru").place(x=900,y=500)


##boton  salir
btn_salir=Button(ventana,text="Salir",font=("Century",15),command=ventana.destroy,width=9,bg="black",fg="peru").place(x=900,y=640)

##boton inicio ## 
# btn_inicio=Button(ventana,text="Iniciar",font=("Century",20),command=inicio,width=20,bg="black",fg="orange").place(x=800,y=815)


#######################################




#######################################

#########VENTANAS##########

##ventana de juego##player1
ventana2=Toplevel(ventana)
ventana2.geometry ("1300x900+300+50")
ventana2.resizable(width=False,height=False)
ventana2.iconify()

##Canvas##player1
lienzo=Canvas(ventana2,width=1300,height=2900,bg="light blue")
lienzo.pack_forget()


##mapa1###player1
mapa__1=PhotoImage(file="mapa_1.png")
mapa_1= lienzo.create_image(0,-28100,image = mapa__1, anchor = NW)

##mapa2##player2
#mapa__2=PhotoImage(file="mapa_2.png")
#mapa_2= lienzo.create_image(0,-28100,image = mapa__2, anchor = NW)

##carro##
carro_main_2=PhotoImage(file="car_main_2.png")
carro_main=PhotoImage(file="car_main.png")
rojo=lienzo.create_image(550, 780, image = carro_main, anchor = NW)


##teclas solo
lienzo.bind("<KeyPress>",car_main_move)
lienzo.focus_set()




###############################################


#############################################


##ventanas dobles ## duo jugadores
ventana3=Toplevel(ventana)
ventana3.geometry ("1600x950+200+20")
ventana3.resizable(width=False,height=False)
ventana3.iconify()

#Canvas_duo#
lienzo_duo=Canvas(ventana3,width=1600,height=950,bg="light blue")
lienzo_duo.pack_forget()


##mapa###player1
mapa_duo_1=PhotoImage(file="mapa_duo_1.png")
lienzo_duo.create_image(0,0,image = mapa_duo_1, anchor = NW)

##carros para duo
rojo=lienzo_duo.create_image(430, 820, image = carro_main, anchor = NW)
morado=lienzo_duo.create_image(1130, 820, image = carro_main_2, anchor = NW)

## teclas duo
lienzo_duo.bind("<KeyPress>",car_main_move_1)
lienzo_duo.focus_set()



###########################################












##Cargar los componentes##
ventana.mainloop ()


