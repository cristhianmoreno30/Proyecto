# -*- coding: utf-8 -*-
#Importamos Las librerias
from tkinter import *
import time
import random




#######VENTANAS DEL MENU###########################

#(1)Se crea la ventana del tk
ventana = Tk()
#(2)Nombre de la ventana
ventana.title("Road Figther")
#(3)Tamaño y posicion de la ventana ( ancho x alto + posX + posY )
ventana.geometry ("900x623+0+0")
ventana.resizable(width=False,height=False)

##Fondos
img_fondo_niveles=PhotoImage(file="fondo_menu_niveles.png")
img_fondo_menu=PhotoImage(file="fondo_menu.png")
img_fondo_1jugador=PhotoImage(file="fondo_menu_player1.png")
img_fondo_2jugadores=PhotoImage(file="fondo_menu_player2.png")
lbl_fondo_menu=Label(image=img_fondo_menu).place(x=0,y=0)




##################FUNCIONES DEL JUEGO#####################

##mapa 1##
def inicio1 ():
    ##ventana de juego
    ventana2 = Toplevel(ventana)
    ventana2.geometry("900x623+0+0")
    ventana2.resizable(width=False, height=False)
    ##Canvas##ventana2
    lienzo = Canvas(ventana2, width=900, height=2900, bg="light blue")
    #########################
    global mapa__1
    mapa__1 = PhotoImage(file="mapa_1.png")
    global carro_main
    carro_main = PhotoImage(file="car_main.png")
    global explosion
    explosion = PhotoImage(file="explosion.png")
    mapa_1= lienzo.create_image(0,-28380,image = mapa__1, anchor = NW)
    rojo=lienzo.create_image(368, 500, image = carro_main, anchor = NW)
    datos= lienzo.create_text(780,100,fill="white",font="Times 18 bold",text=player1.get())
    Cgasolina= StringVar()
    Cgasolina.set("Gasolina")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730,y=200)
    lienzo.pack()
    ventana.withdraw()
    ###########################
    def enemigo_aleatorio():
        aleatorio1= random.randrange(254,494,10)
        global mancha
        mancha = PhotoImage(file="mancha.png")
        lienzo.create_image(aleatorio1,0,image= mancha)

    ###########################
    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 70
            enemigo_aleatorio()
            while (lienzo.coords(mapa_1)[1])< -10:
                lienzo.after(15, lienzo.move(mapa_1, 0, 10))
                if (lienzo.coords(rojo)[0]) < 254:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 368, 500)
                elif (lienzo.coords(rojo)[0]) > 494:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 368, 500)
                elif cgasolina < 1:
                    break
                cgasolina -= 0.01
                Cgasolina.set("Gasolina " + str(int(cgasolina)))
                ventana2.update()
        if tecla.char == "a":
            lienzo.move(rojo, -3, 0)
            lienzo.after(1, lienzo.move(rojo, -3, 0))
        elif tecla.char == "d":
            lienzo.move(rojo, 3, 0)
            lienzo.after(1, lienzo.move(rojo, 3, 0))
    lienzo.bind("<KeyPress>", car_main_move)
    lienzo.focus_set()
    return
###########################################################################################################

##mapa2

def inicio2 ():
    ##ventana de juego
    ventana2 = Toplevel(ventana)
    ventana2.geometry("900x623+0+0")
    ventana2.resizable(width=False, height=False)
    ##Canvas##ventana2
    lienzo = Canvas(ventana2, width=900, height=2900, bg="light blue")
    #########################
    global mapa__2
    mapa__2 = PhotoImage(file="mapa_2.png")
    global carro_main
    carro_main = PhotoImage(file="car_main.png")
    global explosion
    explosion = PhotoImage(file="explosion.png")
    mapa_2= lienzo.create_image(0,-28380,image = mapa__2, anchor = NW)
    rojo=lienzo.create_image(386, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(790, 100, fill="white", font="Times 22 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina 70")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730,y=200)
    lienzo.pack()
    ventana.withdraw()
    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 70
            while (lienzo.coords(mapa_2)[1]) < -10 and cgasolina >= 1:
                lienzo.after(15, lienzo.move(mapa_2, 0, 10))
                if (lienzo.coords(rojo)[0]) < 284:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 386, 500)
                if (lienzo.coords(rojo)[0]) > 500:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 386, 500)
                cgasolina -= 0.01
                Cgasolina.set("Gasolina " + str(int(cgasolina)))
                ventana2.update()
        if tecla.char == "a":
            lienzo.move(rojo, -3, 0)
            lienzo.after(1, lienzo.move(rojo, -3, 0))
        elif tecla.char == "d":
            lienzo.move(rojo, 3, 0)
            lienzo.after(1, lienzo.move(rojo, 3, 0))
        return
    lienzo.bind("<KeyPress>", car_main_move)
    lienzo.focus_set()
    return
#############################################################################################

##mapa3

def inicio3 ():
    ##ventana de juego
    ventana2 = Toplevel(ventana)
    ventana2.geometry("900x623+0+0")
    ventana2.resizable(width=False, height=False)
    ##Canvas##ventana2
    lienzo = Canvas(ventana2, width=900, height=2900, bg="light blue")
    #########################
    global mapa__3
    mapa__3 = PhotoImage(file="mapa_3.png")
    global carro_main
    carro_main = PhotoImage(file="car_main.png")
    global explosion
    explosion = PhotoImage(file="explosion.png")
    mapa_3= lienzo.create_image(0,-28380,image = mapa__3, anchor = NW)
    rojo=lienzo.create_image(446, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(780, 100, fill="white", font="Times 18 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina 70")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730, y=200)
    lienzo.pack()
    ventana.withdraw()
    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 70
            while (lienzo.coords(mapa_3)[1]) < -10 and cgasolina >= 1:
                lienzo.after(15, lienzo.move(mapa_3, 0, 10))
                if (lienzo.coords(rojo)[0]) < 338:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 446, 500)
                if (lienzo.coords(rojo)[0]) > 554:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 446, 500)
                cgasolina -= 0.01
                Cgasolina.set("Gasolina " + str(int(cgasolina)))
                ventana2.update()
        if tecla.char == "a":
            lienzo.move(rojo, -3, 0)
            lienzo.after(1, lienzo.move(rojo, -3, 0))
        elif tecla.char == "d":
            lienzo.move(rojo, 3, 0)
            lienzo.after(1, lienzo.move(rojo, 3, 0))
        return
    lienzo.bind("<KeyPress>", car_main_move)
    lienzo.focus_set()
    return

#################################################################################

##mapa4

def inicio4 ():
    ##ventana de juego
    ventana2 = Toplevel(ventana)
    ventana2.geometry("900x623+0+0")
    ventana2.resizable(width=False, height=False)
    ##Canvas##ventana2
    lienzo = Canvas(ventana2, width=900, height=2900, bg="light blue")
    #########################
    global mapa__4
    mapa__4 = PhotoImage(file="mapa_4.png")
    global carro_main
    carro_main = PhotoImage(file="car_main.png")
    global explosion
    explosion= PhotoImage(file="explosion.png")
    mapa_4 = lienzo.create_image(0,-28380,image = mapa__4, anchor = NW)
    rojo =lienzo.create_image(428, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(780, 100, fill="white", font="Times 18 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina 70")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730, y=200)
    lienzo.pack()
    ventana.withdraw()
    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 70
            while (lienzo.coords(mapa_4)[1]) < -10 and cgasolina >= 1:
                lienzo.after(15, lienzo.move(mapa_4, 0, 10))
                if (lienzo.coords(rojo)[0]) < 326:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,anchor=NW)
                    lienzo.itemconfig(rojo,state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo,state="disabled")
                    lienzo.coords(rojo,428,500)
                if (lienzo.coords(rojo)[0]) > 554:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 428, 500)
                cgasolina -= 0.01
                Cgasolina.set("Gasolina " + str(int(cgasolina)))
                ventana2.update()
        if tecla.char == "a":
            lienzo.move(rojo, -3, 0)
            lienzo.after(1, lienzo.move(rojo, -3, 0))
        elif tecla.char == "d":
            lienzo.move(rojo, 3, 0)
            lienzo.after(1, lienzo.move(rojo, 3, 0))
        return
    lienzo.bind("<KeyPress>", car_main_move)
    lienzo.focus_set()
    return
#############################################################################################

##mapa5

def inicio5 ():
    ##ventana de juego
    ventana2 = Toplevel(ventana)
    ventana2.geometry("900x623+0+0")
    ventana2.resizable(width=False, height=False)
    ##Canvas##ventana2
    lienzo = Canvas(ventana2, width=900, height=2900, bg="light blue")
    #########################
    global mapa__5
    mapa__5 = PhotoImage(file="mapa_5.png")
    global carro_main
    carro_main = PhotoImage(file="car_main.png")
    global explosion
    explosion = PhotoImage(file="explosion.png")
    mapa_5= lienzo.create_image(0,-28380,image = mapa__5, anchor = NW)
    rojo=lienzo.create_image(434, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(780, 100, fill="white", font="Times 18 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina 70")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730, y=200)
    lienzo.pack()
    ventana.withdraw()
    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 70
            while (lienzo.coords(mapa_5)[1]) < -10 and cgasolina >= 1:
                lienzo.after(15, lienzo.move(mapa_5, 0, 10))
                if (lienzo.coords(rojo)[0]) < 308:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 434, 500)
                if (lienzo.coords(rojo)[0]) > 554:
                    cgasolina -= 10
                    explo = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.3)
                    lienzo.delete(explo)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.coords(rojo, 434, 500)
                cgasolina -= 0.01
                Cgasolina.set("Gasolina " + str(int(cgasolina)))
                ventana2.update()
        if tecla.char == "a":
            lienzo.move(rojo, -3, 0)
            lienzo.after(1, lienzo.move(rojo, -3, 0))
        elif tecla.char == "d":
            lienzo.move(rojo, 3, 0)
            lienzo.after(1, lienzo.move(rojo, 3, 0))
        return
    lienzo.bind("<KeyPress>", car_main_move)
    lienzo.focus_set()
    return
###################################################################################

##mapa_duo##
def inicio_duo ():
    ##ventanas dobles ## duo jugadores
    ventana3 = Toplevel(ventana)
    ventana3.geometry("900x623+0+0")
    ventana3.resizable(width=False, height=False)
    # Canvas_duo#
    lienzo_duo = Canvas(ventana3, width=900, height=29000, bg="light blue")
    ##imagines###
    global mapa_duo1
    mapa_duo1 = PhotoImage(file="mapa_duo_1.png")
    global carro_main
    carro_main = PhotoImage(file="car_main.png")
    global carro_main_2
    carro_main_2 = PhotoImage(file="car_main_2.png")
    global explosion
    explosion = PhotoImage(file="explosion.png")
    ##lienzos
    mapa_duo= lienzo_duo.create_image(0, -28380, image=mapa_duo1, anchor=NW)
    rojo = lienzo_duo.create_image(200, 500, image=carro_main, anchor=NW)
    morado = lienzo_duo.create_image(660, 500, image=carro_main_2, anchor=NW)
    ## Nombres
    datos1 = lienzo_duo.create_text(390, 100, fill="white", font="Times 16 bold", text=player1.get())
    datos2 = lienzo_duo.create_text(500, 100, fill="white", font="Times 16 bold", text=player2.get())
    lienzo_duo.pack()
    ventana.withdraw()
    ######################### eventos
    def car_main_move_1(tecla):
        if tecla.char == "q":
            while (lienzo_duo.coords(mapa_duo)[1]) < -10:
                lienzo_duo.after(15, lienzo_duo.move(mapa_duo, 0, 10))
                if (lienzo_duo.coords(rojo)[0]) < 116:
                    explo = lienzo_duo.create_image(lienzo_duo.coords(rojo)[0], lienzo_duo.coords(rojo)[1], image=explosion,
                                                anchor=NW)
                    lienzo_duo.itemconfig(rojo, state="hidden")
                    lienzo_duo.update()
                    time.sleep(0.1)
                    lienzo_duo.delete(explo)
                    lienzo_duo.itemconfig(rojo, state="disabled")
                    lienzo_duo.coords(rojo, 200, 500)
                if (lienzo_duo.coords(rojo)[0]) > 302:
                    explo = lienzo_duo.create_image(lienzo_duo.coords(rojo)[0], lienzo_duo.coords(rojo)[1],
                                                    image=explosion,
                                                    anchor=NW)
                    lienzo_duo.itemconfig(rojo, state="hidden")
                    lienzo_duo.update()
                    time.sleep(0.1)
                    lienzo_duo.delete(explo)
                    lienzo_duo.itemconfig(rojo, state="disabled")
                    lienzo_duo.coords(rojo, 200, 500)
                if (lienzo_duo.coords(morado)[0]) < 564:
                    explo = lienzo_duo.create_image(lienzo_duo.coords(morado)[0], lienzo_duo.coords(morado)[1],
                                                    image=explosion,
                                                    anchor=NW)
                    lienzo_duo.itemconfig(morado, state="hidden")
                    lienzo_duo.update()
                    time.sleep(0.1)
                    lienzo_duo.delete(explo)
                    lienzo_duo.itemconfig(morado, state="disabled")
                    lienzo_duo.coords(morado, 660, 500)
                if (lienzo_duo.coords(morado)[0]) > 744:
                    explo = lienzo_duo.create_image(lienzo_duo.coords(morado)[0], lienzo_duo.coords(morado)[1],
                                                    image=explosion,
                                                    anchor=NW)
                    lienzo_duo.itemconfig(morado, state="hidden")
                    lienzo_duo.update()
                    time.sleep(0.1)
                    lienzo_duo.delete(explo)
                    lienzo_duo.itemconfig(morado, state="disabled")
                    lienzo_duo.coords(morado, 660, 500)
                ventana3.update()
        if tecla.char == "a":
            lienzo_duo.move(rojo, -3, 0)
            lienzo_duo.after(0, lienzo_duo.move(rojo, -3, 0))
        if tecla.char == "d":
            lienzo_duo.move(rojo, 3, 0)
            lienzo_duo.after(0, lienzo_duo.move(rojo, 3, 0))
            ###########TECLAS DEL DUO##########
    def car_main_move_2 (tecla):
        if tecla.char == "j":
            lienzo_duo.move(morado, -3, 0)
            lienzo_duo.after(0, lienzo_duo.move(morado, -3, 0))
        if tecla.char == "l":
            lienzo_duo.move(morado, 3, 0)
            lienzo_duo.after(0, lienzo_duo.move(morado, 3, 0))
        return
    lienzo_duo.bind("<KeyPress>", car_main_move_1)
    lienzo_duo.bind("<KeyRelease>",car_main_move_2)
    lienzo_duo.focus_set()
    return


#####FUNCIONES DEL MENU###########
###############################################



####niveles #####
def menu_niveles():
    btn_niveles=Button(ventana,text="Dificultad",font=("Century",15),command=menu_niveles,width=9,bg="black",fg="peru").place_forget()
    btn_jugadores=Button(ventana,text="Jugadores",font=("Century",15),width=9,bg="black",fg="peru").place_forget()
    btn_salir=Button(ventana,text="Salir",font=("Century",15),command=ventana.destroy,width=9,bg="black",fg="peru").place_forget()
    lbl_fondo_niveles=Label(image=img_fondo_niveles).place(x=0,y=0)
    btn_nvl1=Button(ventana,text="1",font=("Century",15),command=inicio1,width=2,bg="black",fg="peru").place(x=410,y=480)
    btn_nvl2=Button(ventana,text="2",font=("Century",15),command=inicio2,width=2,bg="black",fg="peru").place(x=470,y=480)
    btn_nvl3=Button(ventana,text="3",font=("Century",15),command=inicio3,width=2,bg="black",fg="peru").place(x=530,y=480)
    btn_nvl4=Button(ventana,text="4",font=("Century",15),command=inicio4,width=2,bg="black",fg="peru").place(x=590,y=480)
    btn_nvl5=Button(ventana,text="5",font=("Century",15),command=inicio5,width=2,bg="black",fg="peru").place(x=650,y=480)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=750,y=580)
    return 



##funcion de regreso ##
def regreso():
    lbl_fondo_menu=Label(image=img_fondo_menu).place(x=0,y=0)
    lbl_fondo_niveles=Label(image=img_fondo_niveles).place_forget
    btn_jugadores=Button(ventana,text="Jugadores",font=("Century",15),command=menu_jugadores,width=9,bg="black",fg="peru").place(x=600,y=393)
    btn_salir=Button(ventana,text="Salir",font=("Century",15),command=ventana.destroy,width=9,bg="black",fg="peru").place(x=600,y=463)
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
    btn_player1=Button(ventana,text="1 Jugador",font=("Century",15),command=jugador1,width=9,bg="black",fg="peru").place(x=410,y=393)
    btn_player2=Button(ventana,text="2 Jugadores",font=("Century",15),command=jugador2,width=9,bg="black",fg="peru").place(x=750,y=393)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=750,y=580)
    return

##jugador:
def jugador1():
    global player1
    lbl_fondo_1jugador=Label(image=img_fondo_1jugador).place(x=0,y=0)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=750,y=580)
    player1=StringVar ()
    text_player1=Entry(ventana,textvariable=player1,bg="peru",width=25).place(x=410,y=393)
    btn_inicio=Button(ventana,text="Iniciar",font=("Century",20),command=menu_niveles,width=15,bg="black",fg="orange").place(x=550,y=493)
    return

##dos jugadores:
def jugador2():
    global player1
    global player2
    lbl_fondo_2jugador=Label(image=img_fondo_2jugadores).place(x=0,y=0)
    btn_regreso=Button(ventana,text="Regresar",font=("Century",15),command=regreso,width=9,bg="black",fg="peru").place(x=750,y=580)
    player1=StringVar ()
    text_player1=Entry(ventana,textvariable=player1,bg="peru",width=25).place(x=410,y=380)
    player2=StringVar ()
    text_player2=Entry(ventana,textvariable=player2,bg="peru",width=25).place(x=410,y=450)
    btn_inicio=Button(ventana,text="Iniciar",font=("Century",20),command=inicio_duo,width=15,bg="black",fg="orange").place(x=550,y=513)
    return

##########################################################################################


##########################BOTONES DEL MENU##################################

##botenes de jugadores
btn_jugadores=Button(ventana,text="Jugadores",font=("Century",15),command=menu_jugadores,width=9,bg="black",fg="peru").place(x=600,y=393)

##boton  salir
btn_salir=Button(ventana,text="Salir",font=("Century",15),command=ventana.destroy,width=9,bg="black",fg="peru").place(x=600,y=463)

##Cargar los componentes##
ventana.mainloop ()


