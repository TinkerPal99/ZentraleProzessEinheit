from Tkinter import *
## initialize
root = Tk()

## photo set as variable (only gif, ppm/pgm
logo = PhotoImage(file="")

## stupid variable
explanation = "Filltext"  # type: str

## photolabel, side right, only ppm/pgm and gif
w1 = Label(root,
           image=logo).pack(
    side="right"
)

## first label, textlabel
w1 = Label(root,
           text="Hello Tkinter!"
           )

## second textlabel, advanced, automated pack with position arrangement
## alternative to justify --> justify= place ;--> compound=center (zentral)
w2 = Label(root,
           justify=LEFT,
           padx=10,
           text=explanation
           ).pack(
    side="left"
)

## Label, dass text und image kombiniert    compound gibt an, wie die Elemnet darin sich zueinander positioneren, jeweils obj1 zu 2
w4 = Label(root, compound=CENTER,
           text=explanation,
           image=logo
           )
## label that fits color(fg) and format(font) an background(bg)
w5 = Label(root,
           text=explanation,
           fg="red",
           font="Times").pack(side="right")

## label gets packed in gui
# w1.pack()

## start the gui
root.mainloop()
