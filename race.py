import random
from turtle import Turtle, Screen
from random import choice


corrida = False
screen = Screen()
screen.setup(width=500, height=400)

print("Opções de cores: 'red', 'green', 'yellow', 'black', 'blue'")
escolha = screen.textinput("APOSTA", "Escolha a cor de uma tartaruga: ")

turtles = ["a", "b", "c", "d", "e"]
colors = ["red", "green", "yellow", "black", "blue"]
final = []

c = 0
y = -20
for i in turtles:
    i = Turtle(shape="turtle")
    i.color(colors[c])
    i.penup()
    i.goto(-240, y)
    y += 20
    c += 1
    final.append(i)

if escolha:
    corrida = True

ganhadora = ""
number = [x for x in range(10)]
while corrida:
     for tart in final:
         if tart.xcor() >= 230:
             ganhadora = tart
             corrida = False
         tart.forward(choice(number))
if escolha == ganhadora.pencolor():
    print("Parabéns, você venceu.")
else:
    print(f"Que pena, você perdeu! A vencedora foi a {ganhadora.pencolor()}")

screen.exitonclick()