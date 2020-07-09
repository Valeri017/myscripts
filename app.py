import tkinter as tk
from tkinter import ttk
import webbrowser

app = tk.Tk()
app.title('поисковая система')#оглавление

search_label = ttk.Label(app, text='Поиск')#надпись
search_label.grid(row=0, column=0)

text_field = ttk.Entry(app, width=50)#поле ввода пользователя
text_field.grid(row=0, column=1)
#функция поиска


def search():
	if text_field.get().strip() != '':
	    webbrowser.open('https://www.google.com/search?q=' + text_field.get())

def searchBtn():
	search()

def enterBtn(event):
	search()

def enterBtn(event):
	webbrowser.open('https://www.google.com/search?q=' + text_field.get())

#создание кнопочки
btn_search = ttk.Button(app, text='Найти', width=15, command=search)
btn_search.grid(row=0, column=3)

text_field.bind('<Return>', enterBtn)

app.mainloop()#ВАЖНО!!! что бы не закрывалось