# Homework-session-3

from turtle import*
i = 3
n=90
while i < 9:
    i = i+1
    n = 360 / i
    for j in range(i):
      if j % 2 == 0 :
          color("red")
          forward(100)
          lt(n)
      else:
          color("blue")
          forward(100)
          lt(n)
