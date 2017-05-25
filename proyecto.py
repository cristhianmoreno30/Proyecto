# -*- coding: utf-8 -*-
#Importamos Las librerias
from tkinter import *
import time
import random




#######VENTANAS DEL MENU###########################

#(1)Se crea la ventana del tk
ventana = Tk()
#(2)Nombre de la ventana
ventana.title("Road fighter")
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
    ###########CARGA DE IMAGENES##############
    global mapa__1
    mapa__1 = PhotoImage(file="mapa_1.png")
    global carro_main
    carro_main = PhotoImage(file="car_main.png")
    global explosion
    explosion = PhotoImage(file="explosion.png")
    global mancha1
    mancha1 = PhotoImage(file="mancha.png")
    global car_main_choque
    car_main_choque = PhotoImage(file="car_main_choque.png")
    #############IMAGENES EN CANVAS###################
    mapa_1= lienzo.create_image(0,-28380,image = mapa__1, anchor = NW)
    rojo=lienzo.create_image(368, 500, image = carro_main, anchor = NW)
    datos= lienzo.create_text(780,100,fill="white",font="Times 18 bold",text=player1.get())
    ###############GASOLINA####################
    Cgasolina= StringVar()
    Cgasolina.set("Gasolina")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730,y=200)
    #######cargar widgets########
    lienzo.pack()
    ventana.withdraw() #ocultar ventana principal
    ###########################
    ###########################
    def aleatorio():
        global mancha,mancha_coord1,mancha_coord2,mancha_coord3,mancha_coord4
        mancha = lienzo.create_image(0, 0, image=mancha1, anchor=NW)
        mancha_coord1 = random.randrange(254,494)
        mancha_coord2 = random.randrange(254,494)
        mancha_coord3 = random.randrange(254,494)
        mancha_coord4 = random.randrange(254,494)


    def coords():
        if (lienzo.coords(mapa_1)[1]) == -28000:
            lienzo.coords(mancha, mancha_coord1, -50)
        elif (lienzo.coords(mapa_1)[1]) == -20000:
            lienzo.coords(mancha, mancha_coord2, -50)
        elif (lienzo.coords(mapa_1)[1]) == -15000:
            lienzo.coords(mancha, mancha_coord3, -50)
        elif (lienzo.coords(mapa_1)[1]) == -10000:
            lienzo.coords(mancha, mancha_coord4, -50)


    ###########################
    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 45
            aleatorio()
            while (lienzo.coords(mapa_1)[1])< -10:
                box_rojo= lienzo.bbox(rojo)
                lap_rojo= lienzo.find_overlapping(box_rojo[0],box_rojo[1],box_rojo[2],box_rojo[3])
                coords()
                lienzo.after(15,lienzo.move(mancha,0,10))
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
                elif len(lap_rojo) > 2:
                    cgasolina -= 5
                    lienzo.coords(mancha, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -15, 0))
                elif cgasolina < 1:
                    break
                cgasolina -= 0.01
                Cgasolina.set("Gasolina " + str(int(cgasolina)))
                ventana2.update()
        if tecla.char == "a":
            lienzo.move(rojo, -3, 0)
            lienzo.after(3, lienzo.move(rojo, -3, 0))
        elif tecla.char == "d":
            lienzo.move(rojo, 3, 0)
            lienzo.after(3, lienzo.move(rojo, 3, 0))
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
    global car_minivan
    car_minivan = PhotoImage(file="car_minivan.png")
    global car_main_choque
    car_main_choque = PhotoImage(file="car_main_choque.png")
    global mancha1
    mancha1 = PhotoImage(file="mancha.png")
    ###############################
    car_main_choque = PhotoImage(file="car_main_choque.png")
    mapa_2= lienzo.create_image(0,-28380,image = mapa__2, anchor = NW)
    rojo=lienzo.create_image(386, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(790, 100, fill="white", font="Times 22 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730,y=200)
    lienzo.pack()
    ventana.withdraw()

    ###########################
    def aleatorio():
        global minivan,mancha
        global mancha_coord1,mancha_coord2,mancha_coord3
        global minivan_coord1,minivan_coord2,minivan_coord3,minivan_coord4
        minivan = lienzo.create_image(-200, 0, image=car_minivan, anchor=NW)
        mancha = lienzo.create_image(-200, 0, image=mancha1, anchor=NW)
        #############
        mancha_coord1 = random.randrange(290, 490)
        mancha_coord2 = random.randrange(290, 490)
        mancha_coord3 = random.randrange(290, 490)
        ####
        minivan_coord1 = random.randrange(290, 490)
        minivan_coord2 = random.randrange(290, 490)
        minivan_coord3 = random.randrange(290, 490)
        minivan_coord4 = random.randrange(290, 490)

    def coords():
        if (lienzo.coords(mapa_2)[1]) == -28000:
            lienzo.coords(minivan, minivan_coord1, -50)
        elif (lienzo.coords(mapa_2)[1]) == -25000:
            lienzo.coords(mancha, mancha_coord1, -50)
        elif (lienzo.coords(mapa_2)[1]) == -15000:
            lienzo.coords(minivan, minivan_coord2, -50)
        elif (lienzo.coords(mapa_2)[1]) == -10000:
            lienzo.coords(minivan, mancha_coord2, -50)
        elif (lienzo.coords(mapa_2)[1]) == -5000:
            lienzo.coords(minivan, minivan_coord3, -50)
        elif (lienzo.coords(mapa_2)[1]) == -19000:
            lienzo.coords(mancha, mancha_coord3, -50)
        elif (lienzo.coords(mapa_2)[1]) == -9000:
            lienzo.coords(mancha, minivan_coord4 , -50)

    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 50
            aleatorio()
            while (lienzo.coords(mapa_2)[1]) < -10:
                box_rojo = lienzo.bbox(rojo)
                lap_rojo = lienzo.find_overlapping(box_rojo[0], box_rojo[1], box_rojo[2], box_rojo[3])
                coords()
                lienzo.after(13, lienzo.move(mancha, 0, 10))
                lienzo.after(13, lienzo.move(minivan, 0, 12))
                lienzo.after(13, lienzo.move(mapa_2, 0, 10))
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
                elif lap_rojo == (1,2,4):
                    cgasolina -= 8
                    lienzo.coords(minivan, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -20, 0))
                elif lap_rojo == (1,2,5):
                    cgasolina -= 5
                    lienzo.coords(mancha, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -15, 0))
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
    global car_minivan
    car_minivan = PhotoImage(file="car_minivan.png")
    global car_main_choque
    car_main_choque = PhotoImage(file="car_main_choque.png")
    global mancha1
    mancha1 = PhotoImage(file="mancha.png")
    global car_runner
    car_runner = PhotoImage(file="car_runner.png")
    ##########################################
    mapa_3= lienzo.create_image(0,-28380,image = mapa__3, anchor = NW)
    rojo=lienzo.create_image(446, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(780, 100, fill="white", font="Times 18 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730, y=200)
    lienzo.pack()
    ventana.withdraw()
    ############################################
    def aleatorio():
        global minivan,mancha,runner
        global mancha_coord1,mancha_coord2,mancha_coord3
        global minivan_coord1,minivan_coord2,minivan_coord3,minivan_coord4
        global runner_coord1,runner_coord2,runner_coord3,runner_coord4
        ##
        minivan = lienzo.create_image(-200, 0, image=car_minivan, anchor=NW)
        mancha = lienzo.create_image(-200, 0, image=mancha1, anchor=NW)
        runner = lienzo.create_image(-200, 0, image=car_runner, anchor=NW)
        ##
        mancha_coord1 = random.randrange(340, 550)
        mancha_coord2 = random.randrange(340, 550)
        mancha_coord3 = random.randrange(340, 550)
        ####
        minivan_coord1 = random.randrange(340, 550)
        minivan_coord2 = random.randrange(340, 550)
        minivan_coord3 = random.randrange(340, 550)
        minivan_coord4 = random.randrange(340, 550)
        ####
        runner_coord1 = random.randrange(340, 550)
        runner_coord2 = random.randrange(340, 550)
        runner_coord3 = random.randrange(340, 550)
        runner_coord4 = random.randrange(340, 550)

    def coords():
        ##########
        if (lienzo.coords(mapa_3)[1]) == -28200:
            lienzo.coords(minivan, minivan_coord1, -50)
        elif (lienzo.coords(mapa_3)[1]) == -16000:
            lienzo.coords(minivan, minivan_coord2, -50)
        elif (lienzo.coords(mapa_3)[1]) == -7000:
            lienzo.coords(minivan, minivan_coord3, -50)
        elif (lienzo.coords(mapa_3)[1]) == -9000:
            lienzo.coords(minivan, minivan_coord4, -50)
        ###########
        elif (lienzo.coords(mapa_3)[1]) == -26000:
            lienzo.coords(mancha, mancha_coord1, -50)
        elif (lienzo.coords(mapa_3)[1]) == -12000:
            lienzo.coords(mancha, mancha_coord2, -50)
        elif (lienzo.coords(mapa_3)[1]) == -19000:
            lienzo.coords(mancha, mancha_coord3, -50)
        ###########
        elif (lienzo.coords(mapa_3)[1]) == -25000:
            lienzo.coords(runner, runner_coord1, -50)
        elif (lienzo.coords(mapa_3)[1]) == -13000:
            lienzo.coords(runner, runner_coord2, -50)
        elif (lienzo.coords(mapa_3)[1]) == -8000:
            lienzo.coords(runner, runner_coord3, -50)
        elif (lienzo.coords(mapa_3)[1]) == -11000:
            lienzo.coords(runner, runner_coord4, -50)

###################################
    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 55
            aleatorio()
            while (lienzo.coords(mapa_3)[1]) < -10:
                box_rojo = lienzo.bbox(rojo)
                lap_rojo = lienzo.find_overlapping(box_rojo[0], box_rojo[1], box_rojo[2], box_rojo[3])
                coords()
                lienzo.after(12, lienzo.move(mancha, 0, 10))
                lienzo.after(12, lienzo.move(minivan, 0, 13))
                lienzo.after(12, lienzo.move(runner, 0, 13))
                lienzo.after(12, lienzo.move(mapa_3, 0, 10))
                if (lienzo.coords(runner)[0]) > 338 and (lienzo.coords(runner)[0]) < 446:
                    for i in range(1):
                        lienzo.after(12, lienzo.move(runner, 11, 13))
                        lienzo.update()
                if (lienzo.coords(runner)[0]) > 500:
                    for i in range(1):
                        lienzo.after(12, lienzo.move(runner, -11, 13))
                        lienzo.update()
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
                elif lap_rojo == (1,2,4):
                    cgasolina -= 8
                    lienzo.coords(minivan, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -20, 0))
                elif lap_rojo == (1,2,5):
                    cgasolina -= 5
                    lienzo.coords(mancha, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -15, 0))
                elif lap_rojo == (1,2,6):
                    cgasolina -= 9
                    lienzo.coords(runner, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -20, 0))
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
    global car_minivan
    car_minivan = PhotoImage(file="car_minivan.png")
    global car_main_choque
    car_main_choque = PhotoImage(file="car_main_choque.png")
    global mancha1
    mancha1 = PhotoImage(file="mancha.png")
    global car_runner
    car_runner = PhotoImage(file="car_runner.png")
    global car_gasolina
    car_gasolina = PhotoImage(file="car_gasolina.png")
    #######################
    mapa_4 = lienzo.create_image(0,-28380,image = mapa__4, anchor = NW)
    rojo =lienzo.create_image(428, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(780, 100, fill="white", font="Times 18 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730, y=200)
    lienzo.pack()
    ventana.withdraw()
    ##########################
    def aleatorio():
        global minivan,mancha,runner,fuel
        global mancha_coord1,mancha_coord2,mancha_coord3
        global minivan_coord1,minivan_coord2,minivan_coord3,minivan_coord4,minivan_coord5
        global runner_coord1,runner_coord2,runner_coord3,runner_coord4,runner_coord5
        global fuel_coord1,fuel_coord2
        ##
        minivan = lienzo.create_image(-200, 0, image=car_minivan, anchor=NW)
        mancha = lienzo.create_image(-200, 0, image=mancha1, anchor=NW)
        runner = lienzo.create_image(-200, 0, image=car_runner, anchor=NW)
        fuel = lienzo.create_image(-200, 0, image=car_gasolina, anchor=NW)
        ##
        mancha_coord1 = random.randrange(330, 550)
        mancha_coord2 = random.randrange(330, 550)
        mancha_coord3 = random.randrange(330, 550)
        ####
        minivan_coord1 = random.randrange(330, 550)
        minivan_coord2 = random.randrange(330, 550)
        minivan_coord3 = random.randrange(330, 550)
        minivan_coord4 = random.randrange(330, 550)
        minivan_coord5 = random.randrange(330, 550)
        ####
        runner_coord1 = random.randrange(330, 550)
        runner_coord2 = random.randrange(330, 550)
        runner_coord3 = random.randrange(330, 550)
        runner_coord4 = random.randrange(330, 550)
        runner_coord5 = random.randrange(330, 550)
        ####
        fuel_coord1 = random.randrange(330, 550)
        fuel_coord2 = random.randrange(330, 550)

    def coords():
        ##########
        if (lienzo.coords(mapa_4)[1]) == -28200:
            lienzo.coords(minivan, minivan_coord1, -50)
        elif (lienzo.coords(mapa_4)[1]) == -17000:
            lienzo.coords(minivan, minivan_coord2, -50)
        elif (lienzo.coords(mapa_4)[1]) == -5000:
            lienzo.coords(minivan, minivan_coord3, -50)
        elif (lienzo.coords(mapa_4)[1]) == -9000:
            lienzo.coords(minivan, minivan_coord4, -50)
        elif (lienzo.coords(mapa_4)[1]) == -3000:
            lienzo.coords(minivan, minivan_coord5, -50)
        ###########
        elif (lienzo.coords(mapa_4)[1]) == -27300:
            lienzo.coords(mancha, mancha_coord1, -50)
        elif (lienzo.coords(mapa_4)[1]) == -13000:
            lienzo.coords(mancha, mancha_coord2, -50)
        elif (lienzo.coords(mapa_4)[1]) == -19000:
            lienzo.coords(mancha, mancha_coord3, -50)
        ###########
        elif (lienzo.coords(mapa_4)[1]) == -25500:
            lienzo.coords(runner, runner_coord1, -50)
        elif (lienzo.coords(mapa_4)[1]) == -15000:
            lienzo.coords(runner, runner_coord2, -50)
        elif (lienzo.coords(mapa_4)[1]) == -8500:
            lienzo.coords(runner, runner_coord3, -50)
        elif (lienzo.coords(mapa_4)[1]) == -11500:
            lienzo.coords(runner, runner_coord4, -50)
        elif (lienzo.coords(mapa_4)[1]) == -24500:
            lienzo.coords(runner, runner_coord5, -50)
        ############
        elif (lienzo.coords(mapa_4)[1]) == -23500:
            lienzo.coords(fuel, fuel_coord1, -50)
        elif (lienzo.coords(mapa_4)[1]) == -4500:
            lienzo.coords(fuel, fuel_coord2, -50)


    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 60
            aleatorio()
            while (lienzo.coords(mapa_4)[1]) < -10:
                box_rojo = lienzo.bbox(rojo)
                lap_rojo = lienzo.find_overlapping(box_rojo[0], box_rojo[1], box_rojo[2], box_rojo[3])
                coords()
                lienzo.after(8, lienzo.move(mancha, 0, 10))
                lienzo.after(8, lienzo.move(minivan, 0, 14))
                lienzo.after(8, lienzo.move(runner, 0, 16))
                lienzo.after(8, lienzo.move(fuel, 0, 18))
                lienzo.after(8, lienzo.move(mapa_4, 0, 10))
                if (lienzo.coords(runner)[0]) > 338 and (lienzo.coords(runner)[0]) < 446:
                    for i in range(1):
                        lienzo.after(15, lienzo.move(runner, 11, 16))
                        lienzo.update()
                if (lienzo.coords(runner)[0]) > 500:
                    for i in range(1):
                        lienzo.after(15, lienzo.move(runner, -11, 16))
                        lienzo.update()
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
                elif lap_rojo == (1, 2, 4):
                    cgasolina -= 8
                    lienzo.coords(minivan, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                 anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -20, 0))
                elif lap_rojo == (1, 2, 5):
                    cgasolina -= 5
                    lienzo.coords(mancha, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                 anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -15, 0))
                elif lap_rojo == (1, 2, 6):
                    cgasolina -= 9
                    lienzo.coords(runner, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                 anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -20, 0))
                elif lap_rojo == (1, 2, 7):
                    cgasolina += 10
                    lienzo.coords(fuel, -200, 0)
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
    global car_minivan
    car_minivan = PhotoImage(file="car_minivan.png")
    global car_main_choque
    car_main_choque = PhotoImage(file="car_main_choque.png")
    global mancha1
    mancha1 = PhotoImage(file="mancha.png")
    global car_runner
    car_runner = PhotoImage(file="car_runner.png")
    global car_gasolina
    car_gasolina = PhotoImage(file="car_gasolina.png")
    global car_fighter
    car_fighter= PhotoImage(file="car_fighter.png")
    mapa_5= lienzo.create_image(0,-28380,image = mapa__5, anchor = NW)
    rojo=lienzo.create_image(434, 500, image = carro_main, anchor = NW)
    datos = lienzo.create_text(780, 100, fill="white", font="Times 18 bold", text=player1.get())
    Cgasolina = StringVar()
    Cgasolina.set("Gasolina")
    gasolina = Label(lienzo, textvariable=Cgasolina, fg="white", bg="black", font="Times 18 bold").place(x=730, y=200)
    lienzo.pack()
    ventana.withdraw()

    def aleatorio():
        global minivan,mancha,runner,fuel,fighter
        global mancha_coord1,mancha_coord2,mancha_coord3,mancha_coord4,mancha_coord5
        global minivan_coord1,minivan_coord2,minivan_coord3,minivan_coord4,minivan_coord5,minivan_coord6
        global runner_coord1,runner_coord2,runner_coord3,runner_coord4,runner_coord5,runner_coord6
        global fuel_coord1,fuel_coord2,fuel_coords3
        global fighter_coord1,fighter_coord2,fighter_coord3,fighter_coord4,fighter_coord5
        ##
        minivan = lienzo.create_image(-200, 0, image=car_minivan, anchor=NW)
        mancha = lienzo.create_image(-200, 0, image=mancha1, anchor=NW)
        runner = lienzo.create_image(-200, 0, image=car_runner, anchor=NW)
        fuel = lienzo.create_image(-200, 0, image=car_gasolina, anchor=NW)
        fighter= lienzo.create_image(-200, 0, image=car_fighter, anchor=NW)
        ##
        mancha_coord1 = random.randrange(310, 550)
        mancha_coord2 = random.randrange(310, 550)
        mancha_coord3 = random.randrange(310, 550)
        mancha_coord4 = random.randrange(310, 550)
        mancha_coord5 = random.randrange(310, 550)
        ####
        minivan_coord1 = random.randrange(310, 550)
        minivan_coord2 = random.randrange(310, 550)
        minivan_coord3 = random.randrange(310, 550)
        minivan_coord4 = random.randrange(310, 550)
        minivan_coord5 = random.randrange(310, 550)
        minivan_coord6 = random.randrange(310, 550)
        ####
        runner_coord1 = random.randrange(310, 550)
        runner_coord2 = random.randrange(310, 550)
        runner_coord3 = random.randrange(310, 550)
        runner_coord4 = random.randrange(310, 550)
        runner_coord5 = random.randrange(310, 550)
        runner_coord6 = random.randrange(310, 550)
        ####
        fuel_coord1 = random.randrange(310, 550)
        fuel_coord2 = random.randrange(310, 550)
        fuel_coord3 = random.randrange(310, 550)
        ####
        fighter_coord1 = random.randrange(310, 550)
        fighter_coord2 = random.randrange(310, 550)
        fighter_coord3 = random.randrange(310, 550)
        fighter_coord4 = random.randrange(310, 550)
        fighter_coord5 = random.randrange(310, 550)

    def coords():
        ##########
        if (lienzo.coords(mapa_5)[1]) == -27500:
            lienzo.coords(minivan, minivan_coord1, -50)
        elif (lienzo.coords(mapa_5)[1]) == -24500:
            lienzo.coords(minivan, minivan_coord2, -50)
        elif (lienzo.coords(mapa_5)[1]) == -19500:
            lienzo.coords(minivan, minivan_coord3, -50)
        elif (lienzo.coords(mapa_5)[1]) == -15500:
            lienzo.coords(minivan, minivan_coord4, -50)
        elif (lienzo.coords(mapa_5)[1]) == -11500:
            lienzo.coords(minivan, minivan_coord5, -50)
        elif (lienzo.coords(mapa_5)[1]) == -3500:
            lienzo.coords(minivan, minivan_coord6, -50)
        ###########
        elif (lienzo.coords(mapa_5)[1]) == -28200:
            lienzo.coords(mancha, mancha_coord1, -50)
        elif (lienzo.coords(mapa_5)[1]) == -23500:
            lienzo.coords(mancha, mancha_coord2, -50)
        elif (lienzo.coords(mapa_5)[1]) == -18200:
            lienzo.coords(mancha, mancha_coord3, -50)
        elif (lienzo.coords(mapa_5)[1]) == -9200:
            lienzo.coords(mancha, mancha_coord4, -50)
        elif (lienzo.coords(mapa_5)[1]) == -5300:
            lienzo.coords(mancha, mancha_coord5, -50)
        ###########
        elif (lienzo.coords(mapa_5)[1]) == -26500:
            lienzo.coords(runner, runner_coord1, -50)
        elif (lienzo.coords(mapa_5)[1]) == -22200:
            lienzo.coords(runner, runner_coord2, -50)
        elif (lienzo.coords(mapa_5)[1]) == -16300:
            lienzo.coords(runner, runner_coord3, -50)
        elif (lienzo.coords(mapa_5)[1]) == -13400:
            lienzo.coords(runner, runner_coord4, -50)
        elif (lienzo.coords(mapa_5)[1]) == -8500:
            lienzo.coords(runner, runner_coord5, -50)
        elif (lienzo.coords(mapa_5)[1]) == -6200:
            lienzo.coords(runner, runner_coord6, -50)
        ############
        elif (lienzo.coords(mapa_5)[1]) == -20500:
            lienzo.coords(fuel, fuel_coord1, -50)
        elif (lienzo.coords(mapa_5)[1]) == -10200:
            lienzo.coords(fuel, fuel_coord2, -50)
        elif (lienzo.coords(mapa_5)[1]) == -2200:
            lienzo.coords(fuel, fuel_coord3, -50)
        ##########
        elif (lienzo.coords(mapa_5)[1]) == -25300:
            lienzo.coords(fighter, fighter_coord1, -50)
        elif (lienzo.coords(mapa_5)[1]) == -21400:
            lienzo.coords(fighter, fighter_coord2, -50)
        elif (lienzo.coords(mapa_5)[1]) == -17500:
            lienzo.coords(fighter, fighter_coord3, -50)
        elif (lienzo.coords(mapa_5)[1]) == -12300:
            lienzo.coords(fighter, fighter_coord4, -50)
        elif (lienzo.coords(mapa_5)[1]) == -7300:
            lienzo.coords(fighter, fighter_coord5, -50)

    def car_main_move(tecla):
        if tecla.char == "q":
            global cgasolina
            cgasolina = 30
            aleatorio()
            while (lienzo.coords(mapa_5)[1]) < -10:
                box_rojo = lienzo.bbox(rojo)
                lap_rojo = lienzo.find_overlapping(box_rojo[0], box_rojo[1], box_rojo[2], box_rojo[3])
                coords()
                print(lienzo.coords(fighter)[1])
                lienzo.after(4, lienzo.move(mancha, 0, 10))
                lienzo.after(4, lienzo.move(minivan, 0, 15))
                lienzo.after(4, lienzo.move(runner, 0, 17))
                lienzo.after(4, lienzo.move(fuel, 0, 20))
                lienzo.after(4,lienzo.move(fighter, 0, 19))
                lienzo.after(4, lienzo.move(mapa_5, 0, 10))

                if (lienzo.coords(runner)[0]) > 338 and (lienzo.coords(runner)[0]) < 446:
                    for i in range(1):
                        lienzo.after(15, lienzo.move(runner, 11, 16))
                        lienzo.update()
                if (lienzo.coords(runner)[0]) > 500:
                    for i in range(1):
                        lienzo.after(15, lienzo.move(runner, -11, 16))
                        lienzo.update()
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
                elif lap_rojo == (1, 2, 4):
                    cgasolina -= 8
                    lienzo.coords(minivan, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                 anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -20, 0))
                elif lap_rojo == (1, 2, 5):
                    cgasolina -= 5
                    lienzo.coords(mancha, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                 anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -15, 0))
                elif lap_rojo == (1, 2, 6):
                    cgasolina -= 9
                    lienzo.coords(runner, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                 anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
                    lienzo.after(10, lienzo.move(rojo, -20, 0))
                elif lap_rojo == (1, 2, 7):
                    cgasolina += 10
                    lienzo.coords(fuel, -200, 0)
                elif lap_rojo == (1,2,8):
                    cgasolina -= 10
                    lienzo.coords(fighter, -200, 0)
                    choque = lienzo.create_image(lienzo.coords(rojo)[0], lienzo.coords(rojo)[1], image=car_main_choque,
                                                 anchor=NW)
                    lienzo.itemconfig(rojo, state="hidden")
                    lienzo.update()
                    time.sleep(0.2)
                    lienzo.delete(choque)
                    lienzo.itemconfig(rojo, state="disabled")
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


