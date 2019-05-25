import time
import pyautogui
from tkinter import *

root = Tk()
root.title('El raton bailando')
w = 260
h = 50
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/5) - (w/2)
y = (hs/5) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(bg='forest green')

def move():
	print("raton...")
	global stop
	if not stop:
		global x
		if x < 10:
			x = +x
		pyautogui.moveRel(x, 0)
		x = -x
		root.after(1000, move)
def bailando():
	global stop
	global x
	x = 10
	if button.config('relief')[-1] == 'raised':
		button.config(relief="sunken")
		button.config(text="duerme")
		stop = False
		move()
	else:
		button.config(relief="raised")
		button.config(text="bailando")
		stop = True

button = Button(root, 
                text="bailando", 
                bg="saddle brown",
                activebackground="DeepPink3",
                relief="raised", 
                command=bailando)
button.config(highlightbackground="DeepPink3")
button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()

