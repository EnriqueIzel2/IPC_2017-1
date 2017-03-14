#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Prof. Jucimar Jr.
#Enrique Leão Barbosa Izel         1715310048
#Desenhar um polígono com 3 lados iguais. Cada lado uma cor diferente.

import turtle  
t = turtle.Pen() 
turtle.bgcolor("purple") 
for x in range(1):
    t.pensize(20) 
    t.pencolor("red")
    t.forward(200) 
    t.left(120) 
    t.pencolor("blue")
    t.forward(200) 
    t.left(120) 
    t.pencolor("black")
    t.forward(200) 
    t.left(120) 
