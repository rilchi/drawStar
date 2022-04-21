 #ce programme desinne une etoile a 6 sommets a partir de 2 triangles equilaterales
 #size est la longueur des branches a dessiner
import turtle
from turtle import *
import math
   
def star(size) : 
    angle = 60    
    for i in range(1,12):
       if math.fmod(i, 2) == 0:
          angle = angle - 180
       else:
          angle = 60
       forward(size)
       left(angle)
    forward(size)

size = turtle.numinput('star()',"Entrez la taille de l'etoile: ")
star(size)
if size == 0:
    turtle.write("Vous devez entrer un nombre superieur a zero pour que l'etoile s'affiche",align="center", font=('Verdana', 12, 'normal'))

turtle.exitonclick()
