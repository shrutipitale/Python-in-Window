from turtle import *

#Background
speed(2)
bgcolor("white")
penup()
goto(-50,60)
pendown()

#Window
color("cyan")
begin_fill()
goto(100,100)
goto(100,-100)
goto(-50,-60)
goto(-50,60)
end_fill()
color("white")

#Vertical Line
goto(15,100)
color("white")
width(5)
goto(15,-100)
penup()

#Horizontal Line
goto(100,0)
pendown()
goto(-100,0)

done()