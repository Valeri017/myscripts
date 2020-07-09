
from tkinter import *
import math
root = Tk()

root.title('Синус от х')#заголовок
root.geometry('1220x630')#размер окна

canvas = Canvas(root, width=1000, height=640, bg='#002')#объект холста
canvas.pack(side='right')#выравнивание по правой стороне

#линии сетки по вертикали
for y in range(21):
	k = 50 * y
	canvas.create_line(20+k, 620, 20+k, 20, width=1, fill='#191938')
#линии сетки по горизонтали
for x in range(13):
	k = 50 * x
	canvas.create_line(20, 20+k, 1000, 20+k, width=1, fill='#191938')
# Линии координат Х и У
canvas.create_line(20, 20, 20, 620,width=1, arrow=FIRST, fill='white')# ось У
canvas.create_line(10, 320, 1000, 320,width=1, arrow=FIRST, fill='white')# ось X

canvas.create_text(20, 10, text='300', fill= 'white')
canvas.create_text(20, 630, text='-300', fill= 'white')
canvas.create_text(10, 310, text='0', fill= 'white')
canvas.create_text(990, 310, text='1000', fill= 'white')

label_w = Label(root, text='Циклическая частота')
label_w.place(x=0, y=10)
label_phi = Label(root, text='Cмещение графика по Х')
label_phi.place(x=0, y = 30)
label_A = Label(root, text='Амплитуда') 
label_A.place(x=0, y = 50)
label_dy = Label(root, text='Cмещение графика по У')
label_dy.place(x=0, y = 70)

entry_w = Entry(root)
entry_w.place(x=150, y=10)
entry_phi = Entry(root)
entry_phi.place(x=150, y=30)
entry_A = Entry(root)
entry_A.place(x=150, y=50)
entry_dy = Entry(root)
entry_dy.place(x=150, y=70)

'''w = 0.0209  #цикличекая частота
phi = 10    #смещение графика по х
A = 200     #амплитуда
dy =310     #смещение графика по у

xy = []

for x in range(1000):
	y = math.sin(x * w)
	xy.append(x + phi) 
	xy.append(y * A + dy)
sin_line = canvas.create_line(xy, fill='blue')'''
#canvas.pack()

btn_cals = Button(root, text='Расчитать')
btn_cals.bind('<button-1>')
btn_cals.place(x=10, y=100)

btn_clean = Button(root, text='Очистить')
btn_clean.bind('<Butoon-1>')
btn_clean.place(x=100, y=)

root.mainloop()#последняя строчка кода