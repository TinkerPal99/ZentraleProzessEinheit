from Tkinter import *
from library import reference
from Library.PyClass.piviz import *


root = Tk()
root.configure(background='black')
output = StringVar()
output.set("Bootvorgang anbgeschlossen...Guten Tag.")

__Title = "PiViz - GUI"
assistent = PiViz(reference.getList(reference._Guardian))


def onclick(event):
    output.set(assistent.run(assistent.onInput(__input_Entry1.get())))
    return output


__Headline = Label(root,
                   # compound=RIGHT,
                   padx=50,
                   width=46,
                   justify=LEFT,
                   text=__Title,
                   font="Times, 25")
__Border_vertically = Label(root,
                            width=2,
                            height=800,
                            bg="black")
__output_Label1 = Label(root,
                        width=43,
                        #height=20,
                        borderwidth=5,
                        relief="groove",
                        text=output,
                        font="Times, 15")
__input_Entry1 = Entry(root,
                       width=43,
                       #height=20,
                       borderwidth=5,
                       relief="groove",
                       text="Test",
                       font="Times, 15")

__Border_horizontally = Label(root,
                              width=90,
                              # height=,
                              bg="black")

__Headline.grid(row=0, columnspan=4)
__Border_horizontally.grid(row=1, columnspan=4)
__output_Label1.grid(row=2, columnspan=2)
__input_Entry1.grid(row=2, column=2, columnspan=2)
output1 = root.bind('<Return>', onclick)
root.mainloop()