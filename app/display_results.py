# encoding: utf-8

from tkinter import *
from app.read_data import DataReader

main_bg = 'grey'
right_clicks = 0
cells = {}

dr = DataReader()
results_data = dr.get_data()
height = len(results_data)
width = len(results_data[0])

master = Tk()
master.attributes("-fullscreen", True)
master.configure(bg=main_bg)
frame = Frame(master)
frame.pack(expand=True)

for i in range(height): #Rows
    for j in range(width): #Columns
        text = results_data[i][j]
        fg = 'black' if i == 0 else main_bg
        b = Label(frame, text=text, fg=fg, font=('Arial', 32, 'bold'), relief=RIDGE, width=2, bg=main_bg)
        b.grid(row=i, column=j)
        cells[(i,j)] = b

def read_key(event):
    # if right_clicks < height:
        for j in range(width):
            cells[(3,j)].config(fg='black')
        # right_clicks += 1


master.bind('<Right>', lambda event: read_key(event))
mainloop()