from tkinter import *

window = Tk()

def converter():
    kilos = float(in1.get())
    gramsT.delete("1.0",END)
    gramsT.insert(END,kilos*1000)
    lbsT.delete("1.0",END)
    lbsT.insert(END,kilos*2.20462)
    ozT.delete("1.0",END)
    ozT.insert(END,kilos*35.274)



kgText = Label(window, text="Kg")
kgText.grid(row=0, column=0)

in1_value = StringVar()
in1 = Entry(window, textvariable=in1_value)
in1.grid(row=0, column=1)

convButton = Button(window,text = "Convert",command=converter)
convButton.grid(row=0,column=2)

gramsT = Text(window, height=1, width=20)
gramsT.grid(row=1, column=1)

lbsT = Text(window, height=1, width=20)
lbsT.grid(row=1, column=2)

ozT = Text(window, height=1, width=20)
ozT.grid(row=1, column=3)

window.mainloop()