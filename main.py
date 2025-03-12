from tkinter import *
from tkinter import ttk

cor_1 = "#3B3B3B" # black/preto
cor_2 = "#FEFFFF" # white/branco
cor_3 = "#38576B" # blue/azul
cor_4 = "#ECEFF1" # gray/cinza
cor_5 = "#FFAB40" # orange/laranja



janela = Tk()
janela.title("Calculator")
janela.geometry("235x310")
janela.config(background = cor_1)

#criando frame
frame_tela = Frame(janela, width = 235, height = 50, background = cor_3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row=1, column=0)

# variavel todos os valores vazia
todos_valores = ''

# criando as funções
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    #passando valor para a tela
    valor_texto.set(todos_valores)

# função calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

# função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
    

# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable = valor_texto, width = 16, height = 2, padx = 7, relief = FLAT, anchor="e", justify = RIGHT, font=('Ivy', 18), background=cor_3, foreground= cor_2)
app_label.place(x=0, y=0)

#criando botoes
# 1 fila
b_1 = Button(frame_corpo, command = limpar_tela ,text= "C", width = 11, height = 2, background = cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_1.place(x=0,y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores("%"), text= "%", width = 5, height = 2, background = cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_2.place(x=118,y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores("/"), text= "/", width = 5, height = 2, background = cor_5, foreground=cor_2, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_3.place(x=177,y=0)

# 2 fila
b_4 = Button(frame_corpo, command = lambda: entrar_valores("7"),text= "7", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_4.place(x=0,y=52)
b_5 = Button(frame_corpo, command = lambda: entrar_valores("8"),text= "8", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_5.place(x=59,y=52)
b_6 = Button(frame_corpo, command = lambda: entrar_valores("9"),text= "9", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_6.place(x=118,y=52)
b_7 = Button(frame_corpo, command = lambda: entrar_valores("*"),text= "*", width = 5, height = 2, background=cor_5, foreground=cor_2, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_7.place(x=177,y=52)

# 3 fila
b_8 = Button(frame_corpo, command = lambda: entrar_valores("4"),text= "4", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_8.place(x=0,y=104)
b_9 = Button(frame_corpo, command = lambda: entrar_valores("5"),text= "5", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_9.place(x=59,y=104)
b_10 = Button(frame_corpo, command = lambda: entrar_valores("6"),text= "6", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_10.place(x=118,y=104)
b_11 = Button(frame_corpo, command = lambda: entrar_valores("-"),text= "-", width = 5, height = 2, background=cor_5, foreground=cor_2, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_11.place(x=177,y=104)

# 4 fila
b_12 = Button(frame_corpo, command = lambda: entrar_valores("1"),text= "1", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_12.place(x=0,y=156)
b_13 = Button(frame_corpo, command = lambda: entrar_valores("2"),text= "2", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_13.place(x=59,y=156)
b_14 = Button(frame_corpo, command = lambda: entrar_valores("3"),text= "3", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_14.place(x=118,y=156)
b_15 = Button(frame_corpo, command = lambda: entrar_valores("+"),text= "+", width = 5, height = 2, background=cor_5, foreground=cor_2, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_15.place(x=177,y=156)

# 5 fila
b_16 = Button(frame_corpo, command = lambda: entrar_valores("0"),text= "0", width = 11, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_16.place(x=0,y=208)
b_17 = Button(frame_corpo, command = lambda: entrar_valores("."),text= ".", width = 5, height = 2, background=cor_4, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_17.place(x=118,y=208)
b_18 = Button(frame_corpo, command = calcular,text= "=", width = 5, height = 2, background=cor_5, foreground=cor_2, font=('Ivy', 13, 'bold'), relief = RAISED, overrelief = RIDGE)
b_18.place(x=177,y=208)

janela.mainloop()