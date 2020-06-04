# encoding: utf-8

from tkinter import *
from app.read_data import DataReader

class Display():
    main_bg = 'grey'
    right_clicks = 0
    cells = {}
    # cells = []
    dr = None
    master = None

    def __init__(self):


        self.dr = DataReader()
        self.results_data = self.dr.get_data()
        self.height = len(self.results_data)
        self.width = len(self.results_data[0])

        self.master = Tk()
        self.master.attributes("-fullscreen", True)
        self.master.configure(bg=self.main_bg)
        frame = Frame(self.master)
        frame.pack(expand=True)

        for i in range(self.height): #Rows
            for j in range(self.width): #Columns
                text = self.results_data[i][j]
                fg = 'black' if i == 0 else self.main_bg
                b = Label(frame, text=text, fg=fg, font=('Arial', 32, 'bold'), relief=RIDGE, width=10, bg=self.main_bg)
                b.grid(row=i, column=j)
                self.cells[(i,j)] = b

        self.master.bind('<Right>', lambda event: self.show_next_record(event))

    def show_next_record(self, event):
        if self.right_clicks < self.height - 1:
            for j in range(self.width):
                self.cells[(self.height - self.right_clicks - 1, j)].config(fg='black')
            self.right_clicks += 1

    def hide_previous_record(self, event):
        if self.right_clicks < self.height - 1:
            for j in range(self.width):
                self.cells[(self.height - self.right_clicks - 1, j)].config(fg='black')
            self.right_clicks += 1


Display()
mainloop()