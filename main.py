import turtle
import time
import random
s=turtle.Turtle()
clist=["yellow","hotpink","goldenrod","cyan","orangered","mediumblue","turquoise","magenta","greenyellow","deeppink"]
p=[(-350,-350),(-350,-280),(-350,-210),(-350,-140),(-350,-70),(-350,0),(-350,70),(-350,140),(-350,210),(-350,280)]
number=[(-315,-335),(-245,-335),(-175,-335),(-105,-335),(-35,-335),(35,-335),(105,-335),(175,-335),(245,-335),(315,-335),(315,-265),(245,-265),(175,-265),(105,-265),(35,-265),(-35,-265),(-105,-265),(-175,-265),(-245,-265),(-315,-265),(-315,-195),(-245,-195),(-175,-195),(-105,-195),(-35,-195),(35,-195),(105,-195),(175,-195),(245,-195),(315,-195),(315,-125),(245,-125),(175,-125),(105,-125),(35,-125),(-35,-125),(-105,-125),(-175,-125),(-245,-125),(-315,-125),(-315,-55),(-245,-55),(-175,-55),(-105,-55),(-35,-55),(35,-55),(105,-55),(175,-55),(245,-55),(315,-55),(315,15),(245,15),(175,15),(105,15),(35,15),(-35,15),(-105,15),(-175,15),(-245,15),(-315,15),(-315,85),(-245,85),(-175,85),(-105,85),(-35,85),(35,85),(105,85),(175,85),(245,85),(315,85),(315,155),(245,155),(175,155),(105,155),(35,155),(-35,155),(-105,155),(-175,155),(-245,155),(-315,155),(-315,225),(-245,225),(-175,225),(-105,225),(-35,225),(35,225),(105,225),(175,225),(245,225),(315,225),(315,295),(245,295),(175,295),(105,295),(35,295),(-35,295),(-105,295),(-175,295),(-245,295),(-315,295)]
sl=[[4,36,(-35,-105),180],[38,62,(-245,105),180],[10,87,(105,245),90],[57,96,(-35,315),0],[42,5,(-35,-315),0],[69,13,(175,-245),180],[92,55,(35,35),0],[99,8,(175,-315),180]]
decorpc=["blue","cyan"]
dice=[[(500,-10)],[(555,45),(445,-70)],[(445,45),(500,-15),(555,-70)],[(445,45),(555,-70),(555,45),(445,-70)],[(445,45),(555,-70),(555,45),(445,-70),(500,-15)],[(445,45),(555,-70),(555,45),(445,-70),(445,-12.5),(555,-12.5)]]
s.ht()
s.pu()
turtle.bgcolor("deeppink")
s.pencolor("yellow")
s.goto(-200,120)
s.write("Presented By:-",align="center",font=("Times",50,"bold"))
time.sleep(2)
s.goto(200,-120)
s.write("Sarthak Puri",align="center",font=("Times",50,"bold"))
time.sleep(3)
for i in range(4):
        s.undo()
turtle.bgcolor("lawngreen")
s.pencolor("orangered")
s.goto(-200,120)
s.write("Powered By:-",align="center",font=("Times",50,"bold"))
time.sleep(2)
s.goto(200,-120)
s.write("Turtle",align="center",font=("Times",50,"bold"))
time.sleep(2)
for i in range(4):
        s.undo()
turtle.bgcolor("mistyrose")
s.pencolor("black")
s.goto(-590,130)
s.write("Snake",align="center",font=("Times",50,"bold"))
s.goto(-530,0)
s.write("&",align="center",font=("Times",50,"bold"))
s.goto(-490,-130)
s.write("Ladders",align="center",font=("Times",50,"bold"))
s.speed(0)
s.pensize(4)
s.lt(90)
for k in range(10):     #drawboard
	s.pu()
	s.goto(p[k])
	s.pd()
	s.rt(90)
	clist.append(clist[0])
	clist.pop(0)
	for i in range(10):
		s.color("black",clist[i])
		if i>0:
			s.rt(90)
		s.begin_fill()
		for j in range(5):
			s.fd(70)
			s.lt(90)
		s.end_fill()
def spbox(loc):
	s.pu()
	s.goto(loc)
	s.pd()
	s.color("black","red")
	s.begin_fill()
	for j in range(4):
		s.fd(70)
		s.lt(90)
	s.end_fill()
	s.lt(90)
	for i in range(6):
		s.fd(10)
		s.rt(90)
		s.pencolor("yellow")
		for j in range(6):
			s.pu()
			s.fd(9)
			s.pd()
			s.fd(1)
		s.rt(180)
		s.pu()
		s.fd(60)
		s.rt(90)
	s.rt(90)
spbox((-350,280))
spbox((-350,-350))
def decor(loc,word):
	smpl=40
	s.goto(loc)
	for i in range(2):
		s.pencolor(decorpc[i])
		s.write(word,align="center",font=("arial",smpl-i,"bold"))
		smpl-=4
decor((-385,-347.5),"S")
decor((-385,282.5),"W")

s.pensize(40)         #snake1
s.pencolor("red")
s.goto(-255,315)
s.rt(90)
s.pd()
ps=40
s.pensize(25)
for j in range(6):
	for i in range(15):
		s.fd(10)
		if j%2==0:
			s.rt(7.5)
		else:
			s.lt(7.5)
		s.pensize(ps)
		ps-=0.2
s.pu()
s.goto(-250,320)
s.pd()
s.pencolor("khaki")
s.pensize(3)
s.circle(4)
s.pu()
s.goto(-250,305)
s.pd()
s.circle(4)


s.pu()    				  #snake2
s.pencolor("orangered")
s.goto(245,315)
s.pd()
s.rt(180)
ps=30
for j in range(3):
	for i in range(15):
		s.fd(9)
		if j%2==0:
			s.lt(7.5)
		else:
			s.rt(7.5)
		s.pensize(ps)
		ps-=0.2
s.pu()
s.goto(235,320)
s.pd()
s.pencolor("black")
s.pensize(3)
s.circle(4)
s.pu()
s.goto(235,305)
s.pd()
s.circle(4)


s.pu()    				  #snake3
s.pencolor("darkviolet")
s.goto(245,105)
s.pd()
s.rt(90)
ps=30
for j in range(3):
	for i in range(15):
		s.fd(9)
		if j%2==0:
			s.lt(7.5)
		else:
			s.rt(7.5)
		s.pensize(ps)
		ps-=0.2
s.pu()
s.goto(235,105)
s.pd()
s.pencolor("black")
s.pensize(3)
s.circle(4)
s.pu()
s.goto(235,90)
s.pd()
s.circle(4)


s.pu()						#snake4
s.pencolor("chartreuse")
s.goto(-245,-35)
ps=30
s.lt(45)
s.pd()
for j in range(3):
	for i in range(15):
		s.fd(9)
		if j%2==0:
			s.rt(7.5)
		else:
			s.lt(7.5)
		s.pensize(ps)
		ps-=0.2
s.pu()
s.goto(-240,-25)
s.pd()
s.pencolor("red")
s.pensize(3)
s.circle(4)
s.pu()
s.goto(-240,-40)
s.pd()
s.circle(4)


s.pu()
s.pensize(10)
s.pencolor("firebrick")
s.goto(-134,-320)                #ladder1
s.pd()
s.rt(175)
s.fd(240)
s.pu()
s.rt(90)
s.fd(53)
s.pd()
s.rt(90)
s.fd(240)
s.pu()
s.goto(-134,-320)
s.rt(180)
s.pd()
for i in range(6):
	s.fd(35)
	s.rt(90)
	s.fd(53)
	s.rt(180)
	s.fd(53)
	s.rt(90)
s.pu()             #ladder2
s.goto(290,-320)
s.pd()
s.lt(38)
s.fd(600)
s.pu()
s.rt(90)
s.fd(53)
s.pd()
s.rt(90)
s.fd(600)
s.pu()
s.goto(290,-320)
s.rt(180)
s.pd()
for i in range(16):
	s.fd(36)
	s.rt(90)
	s.fd(53)
	s.rt(180)
	s.fd(53)
	s.rt(90)
s.pu()             #ladder3
s.goto(-200,-115),s.pd(),s.rt(2),s.fd(230),s.pu(),s.rt(90)
s.fd(53)
s.pd()
s.rt(90)
s.fd(230)
s.pu()
s.goto(-200,-115)
s.rt(180)
s.pd()
for i in range(6):
	s.fd(33)
	s.rt(90)
	s.fd(53)
	s.rt(180)
	s.fd(53)
	s.rt(90)
s.pu()             #ladder4
s.goto(-130,25)
s.pd()
s.rt(32)
s.fd(300)
s.pu()
s.rt(90)
s.fd(53)
s.pd()
s.rt(90)
s.fd(300)
s.pu()
s.goto(-130,25)
s.rt(180)
s.pd()
for i in range(7):
	s.fd(37)
	s.rt(90)
	s.fd(53)
	s.rt(180)
	s.fd(53)
	s.rt(90)


s.pencolor("black")
s.pu()
s.goto(-315,-335)
for i in range(1,101):   #numbering
	s.goto(number[i-1])
	if i in [99,92,69,42]:
		s.write("",align="center",font=("arial",23,"bold"))
	else:
		s.write(i,align="center",font=("arial",23,"bold"))

z=turtle.Turtle()                  #ScoreBoard
z.ht()
z.pu()
z.pensize(6)
z.speed(0)
player1=turtle.textinput("Snake & Ladders","Enter Name of Player 1")
z.goto(500,200)
z.write(player1,align="center",font=("arial",35,"bold"))
player2=turtle.textinput("Snake & Ladders","Enter Name of Player 1")
z.goto(500,-250)
z.write(player2,align="center",font=("arial",35,"bold"))


s=turtle.Turtle()
s.pu()
s.goto(-385,-315)
s.color("black","navy")
s.shape("circle")
s.shapesize(2)
p=turtle.Turtle()
p.pu()
p.goto(-385,-315)
p.shape("circle")
p.color("black","lawngreen")
p.shapesize(2)

p1=0
gameover=0
p2=0

y=turtle.Turtle()
y.shapesize(4)
y.pu()
y.speed(0)
y.rt(90)
for i in range(10000):
	a=random.randint(1,6)
	if gameover==1:
		break
	y.rt(180)
	if i%2==0:
		y.color("black","navy")
		y.goto(500,185)
	else:
		y.color("black","lawngreen")
		y.goto(500,-190)
	p11=p1
	p21=p2
	for k in range(7):
		if p11==sl[k][0]:
			p1=sl[k][1]
			s.goto(sl[k][2])
			s.rt(sl[k][3])
	for f in range(7):
		if p21==sl[f][0]:
			p2=sl[f][1]
			p.goto(sl[f][2])
			p.rt(sl[f][3])
	move=turtle.textinput("Click Enter","Write a wish if you want!  :-)")
	z.color("black","red")
	z.goto(400,-100)
	z.pd()
	z.begin_fill()
	for j in range(4):
		z.fd(200)
		z.lt(90)
	z.end_fill()
	z.color("black","black")
	for de in range(a):
		z.begin_fill()
		z.pu()
		z.goto(dice[a-1][de])
		z.pd()
		z.circle(15)
		z.end_fill()
	z.pu()
	for j in range(a):
		if (((100-p11)>=a and p11!=0) or 0<p11<95) and i%2==0:
			s.fd(70)
			p1+=1
			time.sleep(0.2)
			if p1 in [10,11,30,31,50,51,70,71,90,91]:
				s.lt(90)
			elif p1 in [20,21,40,41,60,61,80,81]:
				s.rt(90)
			elif p1==100:
				s.fd(70)
				gameover=1
		elif (((100-p21)>=a and p21!=0)or 0<p21<95) and i%2==1:
			p.fd(70)
			p2+=1
			time.sleep(0.2)
			if p2 in [10,11,30,31,50,51,70,71,90,91]:
				p.lt(90)
			elif p2 in [20,21,40,41,60,61,80,81]:
				p.rt(90)
			elif p2==100:
				p.fd(70)
				gameover=1
	if a==6 and i%2==0 and p11==0:
		s.fd(70)
		p1+=1
	elif a==6 and i%2==1 and p21==0:
		p.fd(70)
		p2+=1
if i%2==1:
        playerW=player1
        playerL=player2
else:
        playerW=player2
        playerL=player1
z.pensize(1)
z.goto(355,-350)
z.pd()
z.color("cyan","cyan")
z.begin_fill()
for j in range(2):
      z.fd(400)
      z.lt(90)
      z.fd(700)
      z.lt(90)
z.end_fill()
z.color("red","red")
z.lt(90)
z.fd(400)
z.begin_fill()
z.rt(180)
z.fd(400)
z.lt(90)
z.fd(1000)
z.end_fill()
z.pencolor('black')
z.pu()
z.goto(500,200)
z.write("Congrats! "+playerW,align="center",font=("Times",25,"bold"))
z.goto(515,150)
z.write("You Won The Game!",align="center",font=("Times",25,"bold"))
z.goto(500,-150)
z.write("Well Tried "+playerL,align="center",font=("Times",25,"bold"))
z.goto(515,-200)
z.write("Better Luck Next Time!",align="center",font=("Times",22,"bold"))
time.sleep(1000)