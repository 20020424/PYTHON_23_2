import tkinter as tk
from tkinter import PhotoImage
import random
import time

tiempo = 30
crx = False

lista_op=[]
# [0] opcion 1
# [1] opcion 2
# [2] opcion 3
# [3] opcion 4
# acomodados aleatoriamente por un random.shuffle()

prob_res=[]
# [0] primer numero en la operacion
# [1] segundo numero en la operacion
# [2] Tipo de operacion a realizar (+,-,/,*)

# ROOT----------------------------------------------
root = tk.Tk()
root.geometry("720x480")
root.title("Crono-máticas")
root.resizable(width=False, height=False)

## MENU PRINCIPAL-------------------------------------------
def menu_principal():
    global tiempo
    tiempo = 30
    # TITULOOOOO---------------------------------------------
    #et_titulo.place(x=230, y=50)
    menu_label.place(x=0, y=0)
    botones_menu()

#BOTONES------------------------------------------
def botones_menu():
    bniv1.place(x=280, y=150)

    
    #bniv2.place(x=280, y=220)
    #bniv2.config(state=tk.DISABLED) # PROXIMAMENTE JSJSJS
    #bniv3.place(x=280, y=290)
    #bniv3.config(state=tk.DISABLED) # PROXIMAMENTE TAMBIEN JSJSJS

# ACTIVA CUENTA REGRESIVA---------------------
def cuenta_regre():
    global tiempo, crx

    if crx and tiempo >= 1:
        crono.config(text=f" Tiempo: {tiempo}")
        tiempo -= 1
        root.after(1000, cuenta_regre)
    elif crx:
        crono.config(text="¡Se acabó el tiempo!")
        regresar_menu()
        crx = False

# OPCIONES ( NIVEL 1 ) ----------------------------------------------- (NIVEL 1)
def opciones1():
    global crx, tiempo

    lista_op.clear()
    prob_res.clear()
    bniv1.place_forget()
    #bniv2.place_forget()
    #bniv3.place_forget()
    #et_titulo.place_forget()
    menu_label.place_forget()
    crono.place(x=35, y=425)

    nivel1()

    niv_txt.config(font=("Arial",30,"bold"), text= f"{prob_res[0]} {prob_res[2]} {prob_res[1]} = ")
    niv_txt.place(x=300, y=50)

    op1_1.config(font=("Arial",30,"bold"),text=f"{lista_op[0]}",width=6, height=1)
    op1_1.place(x=170, y=200)

    op2_1.config(font=("Arial",30,"bold"),text=f"{lista_op[1]}",width=6, height=1)
    op2_1.place(x=395, y=200)

    op3_1.config(font=("Arial",30,"bold"),text=f"{lista_op[2]}",width=6, height=1)
    op3_1.place(x=170, y=325)

    op4_1.config(font=("Arial",30,"bold"),text=f"{lista_op[3]}",width=6, height=1)
    op4_1.place(x=395, y=325)

    if not crx:
        crx = True
        cuenta_regre()

# NIVEL 1 -------------------------------------------------
def nivel1():
    #SUMA -----------------------------------------------------------
    def suma_1():
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        result = num1 + num2
        lista_op.append(result)

        # validar numero en la lsita
        while len(lista_op) < 4:
            nran = random.randint(2,10)

            if nran in lista_op:
                nran = random.randint(2,10)
            else:
                lista_op.append(nran)

        prob_res.append(num1)
        prob_res.append(num2)
        txt_oper="+"
        prob_res.append(txt_oper)

        random.shuffle(lista_op)
        return lista_op, prob_res

    # RESTA ----------------------------------------------------------
    def resta_1():
        while True:
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            result = num1 - num2

            # resultado no sea menor o igual a 0
            if result <= 0:
                continue
            else:
                lista_op.append(result)
                break

        # validar numero en la lsita
        while len(lista_op) < 4:
            nran = random.randint(1,10)

            if nran in lista_op:
                nran = random.randint(1,10)
            else:
                lista_op.append(nran)

        prob_res.append(num1)
        prob_res.append(num2)
        txt_oper="-"
        prob_res.append(txt_oper)

        random.shuffle(lista_op)
        return lista_op, prob_res
    
    # MULTIPLICACION
    def multi_1():
        while True:
            num1 = random.randint(1,5)
            num2 = random.randint(1,5)
            result = num1 * num2
            lista_op.append(result)

            # validar numero en la lsita
            while len(lista_op) < 4:
                nran = random.randint(1,50)

                if nran in lista_op:
                    nran = random.randint(1,50)
                else:
                    lista_op.append(nran)

            prob_res.append(num1)
            prob_res.append(num2)
            txt_oper="x"
            prob_res.append(txt_oper)

            random.shuffle(lista_op)
            return lista_op, prob_res
    
    # DIVISION
    def divi_1():
        while True:
            num1 = random.randint(1,10)
            num2 = random.randint(1,2)

            if num1 % 2 == 0:
                result = num1 / num2
                result = int(result)
                lista_op.append(result)
            else:
                continue

            # validar numero en la lsita
            while len(lista_op) < 4:
                nran = random.randint(1,10)

                if nran in lista_op:
                    nran = random.randint(1,10)
                else:
                    lista_op.append(nran)

            prob_res.append(num1)
            prob_res.append(num2)
            txt_oper="/"
            prob_res.append(txt_oper)

            random.shuffle(lista_op)
            return lista_op, prob_res

    # TIPO DE OPERACION ---------------------------------------------
    prob = random.randint(1,4)
    if prob == 1:
        suma_1()
    elif prob == 2:
        resta_1()
    elif prob == 3:
        multi_1()
    else:
        divi_1()

# VERIFICAR RESPUESTA ( NIVEL 1)----------------------------------------
def resp_corr1():
    if prob_res[2] == '+':
        if prob_res[0] + prob_res[1] == lista_op[0]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()
            
    elif prob_res[2] == '-':
        if prob_res[0] - prob_res[1] == lista_op[0]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == 'x':
        if prob_res[0] * prob_res[1] == lista_op[0]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == '/':
        if prob_res[0] // prob_res[1] == lista_op[0]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

def resp_corr2():
    if prob_res[2] == '+':
        if prob_res[0] + prob_res[1] == lista_op[1]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == '-':
        if prob_res[0] - prob_res[1] == lista_op[1]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == 'x':
        if prob_res[0] * prob_res[1] == lista_op[1]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == '/':
        if prob_res[0] // prob_res[1] == lista_op[1]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

def resp_corr3():
    if prob_res[2] == '+':
        if prob_res[0] + prob_res[1] == lista_op[2]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == '-':
        if prob_res[0] - prob_res[1] == lista_op[2]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == 'x':
        if prob_res[0] * prob_res[1] == lista_op[2]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == '/':
        if prob_res[0] // prob_res[1] == lista_op[2]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

def resp_corr4():
    if prob_res[2] == '+':
        if prob_res[0] + prob_res[1] == lista_op[3]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == '-':
        if prob_res[0] - prob_res[1] == lista_op[3]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == 'x':
        if prob_res[0] * prob_res[1] == lista_op[3]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

    elif prob_res[2] == '/':
        if prob_res[0] // prob_res[1] == lista_op[3]:
            siguiente()
        else:
            resp_txt2.place(x=50, y=425)
            regresar_menu()

# SIGUIENTE PROBLEMA (SI CONTESTA CORRECTAMENTE) ( NIVEL 1) ----------------------------
def siguiente():
    niv_txt.place_forget()
    op1_1.place_forget()
    op1_1.place_forget()
    op2_1.place_forget()
    op3_1.place_forget()
    op4_1.place_forget()

    return opciones1()

# BOTON REGRESAR (AL PERDER)
def regresar_menu():
    op1_1.config(state=tk.DISABLED)
    op2_1.config(state=tk.DISABLED)
    op3_1.config(state=tk.DISABLED)
    op4_1.config(state=tk.DISABLED)
    crono.place_forget()
    global tiempo
    tiempo = 0

    btn_back.place(x=600, y=425)
    juego_label.place(x=0, y=0)

# LIMPIAR PANTALLA (regresar al menu)
def limpiar_pantalla():
    niv_txt.place_forget()
    op1_1.place_forget()
    op1_1.place_forget()
    op2_1.place_forget()
    op3_1.place_forget()
    op4_1.place_forget()
    resp_txt2.place_forget()
    btn_back.place_forget()

    op1_1.config(state=tk.NORMAL)
    op2_1.config(state=tk.NORMAL)
    op3_1.config(state=tk.NORMAL)
    op4_1.config(state=tk.NORMAL)
    return menu_principal()

# IMAGEN PANTALLA JUEGO -----------------------------------
juego_imagen = PhotoImage(file="fondo_juego.png")
juego_imagen = juego_imagen.subsample(1,1)
juego_label = tk.Label(root, image=juego_imagen)
juego_label.place(x=0, y=0)


# IMAGEN PANTALLA INICIO ----------------------------------
#et_titulo = tk.Label(root, text="Cronomaticas")
#et_titulo.config(font=("Arial",30,"bold"))

menu_imagen = PhotoImage(file="fondo2.png")
menu_imagen = menu_imagen.subsample(1,1)
menu_label = tk.Label(root, image=menu_imagen)
menu_label.place(x=0, y=0)


# CRONOMETRO (CUENTA REGRESIVA) --------------------------
crono=tk.Label(root,text=" ")
crono.config(font=("Arial",15,"bold"))

# INCORRECTO (PERDIO EL JUEGO)
resp_txt2=tk.Label(root,text="Fin del juego")
resp_txt2.config(font=("Arial",20,"bold"))

# BOTONES BESCOGER NIVEL ----------------------------------------
bniv1 = tk.Button(root,text=" Nivel 1 ",width=10, height=1, command=opciones1)
bniv1.config(font=("Arial",20,"bold"))




#bniv2 = tk.Button(root,text=" Nivel 2 ",width=10, height=1)
#bniv2.config(font=("Arial",20,"bold"))
#bniv3 = tk.Button(root,text=" Nivel 3 ",width=10, height=1)
#bniv3.config(font=("Arial",20,"bold"))

# TEXTO OPERACION (NIVEL 1)---------------------------------------
niv_txt = tk.Label(root, text= " ")
niv_txt.config(font=("Arial",30,"bold"))

# BOTONES OPCIONES (NIVEL 1)--------------------------------------
op1_1 = tk.Button(root,text=" ", command= resp_corr1)
op1_1.config(font=("Arial",30,"bold"))

op2_1 = tk.Button(root,text=" ", command= resp_corr2)
op2_1.config(font=("Arial",30,"bold"))

op3_1 = tk.Button(root,text=" ", command= resp_corr3)
op3_1.config(font=("Arial",30,"bold"))

op4_1 = tk.Button(root,text=" ", command= resp_corr4)
op4_1.config(font=("Arial",30,"bold"))

# BOTON REGRESAR-------------------------------------------
btn_back=tk.Button(root,text="Menú", command=limpiar_pantalla)
btn_back.config(font=("Arial",10,"bold"))

# LLAMAR FUNCION MENU PRINCIPAL
menu_principal()

# MAINLOOP-------------------------------------------------
root.mainloop()