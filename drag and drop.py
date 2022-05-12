from tkinter import *

def drag_start(event):
	widget = event.widget
	widget.startX = event.x
	widget.startY = event.y

def drag_motion(event):
	widget = event.widget
	x = widget.winfo_x() - widget.startX + event.x
	y = widget.winfo_y() - widget.startY + event.y
	widget.place(x = x , y = y)

window = Tk()

red_label = Label(window,bg="red",width = 10, height=5)
red_label.place(x=0,y=0)

red_label.bind("<Button-1>",drag_start)
red_label.bind("<B1-Motion>",drag_motion)

blue_label = Label(window,bg="blue",width = 10, height=5)
blue_label.place(x = 100,y = 100)

blue_label.bind("<Button-1>",drag_start)
blue_label.bind("<B1-Motion>",drag_motion)


window.mainloop()         
