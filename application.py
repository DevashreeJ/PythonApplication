from Tkinter import *
import tkFileDialog
root = Tk("Text Editor")
text = Text(root)
text.grid()


def saveas():
	global text
	t = text.get("1.0", "end-1c")
	savelocation = tkFileDialog.asksaveasfilename()
	file1 = open(savelocation, "w+")

	file1.write(t)
	file1.close()

button = Button(root, text= "Save", command=saveas)
button.grid()

def FontHelvetica():
	global text
	text.config(font = "Helvetica")
	
def FontCourier():
	global text
	text.config(font = "Courier")
	
def FontArial():
	global text
	text.config(font = "Arial")
	
def FontTimes():
	global text
	text.config(font = "Times")
	
font = Menubutton(root, text="Font")

font.grid()

font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
Helvetica = IntVar()
arial = IntVar()
times = IntVar()
courier = IntVar()

font.menu.add_checkbutton(label = "Courier", variable= courier, command=FontCourier)
font.menu.add_checkbutton(label = "Helvetica", variable= Helvetica, command=FontHelvetica)
font.menu.add_checkbutton(label = "Times", variable= times, command=FontTimes)


root.mainloop()