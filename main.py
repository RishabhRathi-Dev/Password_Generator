import tkinter as tk
import password_generator_module as pg

window = tk.Tk()
txt = tk.Text(window, state = 'normal')
head = tk.Label(text='Password Generator')
head.pack()

length = 0

#dis = tk.Label()

def cleaner():
    txt.delete(1.0, tk.END)

def displ():
    
    val = pg.generator()
    length = len(val)

    txt.insert('insert', val)
    txt.insert('insert', '\n')
    txt.pack()

gen = tk.Button(
                text='Generate',
                fg='green',
                command=displ
)
gen.pack(side=tk.LEFT)

cln = tk.Button(
    text='Clear',
    fg='yellow',
    command=cleaner
).pack(side=tk.LEFT)


QUIT = tk.Button( 
                   text="QUIT", 
                   fg="red",
                   command=quit)

QUIT.pack(side=tk.RIGHT)


window.wm_title("Password Generator")
window.geometry('400x200')
window.mainloop()

