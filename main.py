from tkinter import *
from random import *
import math

WIDTH = 500
HEIGHT = 500
COEFFICIENT = 3
PERIOD = 500

s = Canvas(Tk(), width=WIDTH, height=HEIGHT, background="black")
s.pack()

def display_gridlines():
  spacing = 50 
  for x in range(0, 800, spacing): 
    s.create_line(x, 25, x, 600, fill="white")
    s.create_text(x, 5, text=str(x), font="Times 9", anchor = N)

  for y in range(0, 600, spacing):
    s.create_line(25, y, 800, y, fill="white")
    s.create_text(5, y, text=str(y), font="Times 9", anchor = W)


def create_star(x, y):
  w = uniform(1, 3)
  offset_x = randint(-8, 8)
  offset_y = randint(-8, 8)
  s.create_oval(x+offset_x, y+offset_y, x+w+offset_x, y+w+offset_y, fill="white", outline="")

  offset_x = randint(-18, 18)
  offset_y = randint(-18, 18)
  w = uniform(0, 1)
  s.create_oval(x+offset_x, y+offset_y, x+w+offset_x, y+w+offset_y, fill="white", outline="")


spiral_size = 5
spiral_turns = 2
def create_spiral(negative, coeffecient, period, offset):
  angle = 0
  for theta in range(0, period, 1):
    x = negative * theta/100 * coeffecient * angle * math.cos(angle) 
    y = negative * theta/100 * coeffecient * angle * math.sin(angle) 
    create_star(x+WIDTH//2, y+HEIGHT//2)
    angle += spiral_turns * (2 * math.pi) / period + offset


angle_offset = 0
while True:  # Infinite loop for continuous rotation
  s.delete("all")  # Clear the canvas

  create_spiral(1, COEFFICIENT, int(PERIOD*1.1), angle_offset)
  create_spiral(-1, COEFFICIENT, int(PERIOD*1.1), angle_offset)
  create_spiral(1, COEFFICIENT*1.5, PERIOD, angle_offset)
  create_spiral(-1, COEFFICIENT*1.5, PERIOD, angle_offset)

  angle_offset += 0.00001
  s.update()
  s.after(10)

s.update()
s.mainloop()