# encoding: utf-8

from tkinter import *
from app.read_data import DataReader

class Display():
    main_bg = 'grey'
    right_clicks = 0
    cells = []
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
            row = []
            for j in range(self.width): #Columns
                text = self.results_data[i][j]
                fg = 'black' if i == 0 else self.main_bg
                b = Label(frame, text=text, fg=fg, font=('Arial', 32, 'bold'), relief=RIDGE, width=10, bg=self.main_bg)
                b.grid(row=i, column=j)
                row.append(b)
            self.cells.append(row)

        self.master.bind('<Right>', lambda event: self.show_next_record(event))
        self.master.bind('<Left>', lambda event: self.hide_last_record(event))
        self.master.bind('<Escape>', lambda event: self.close(event))

    def show_next_record(self, event):
        for cell in self.cells[-self.right_clicks-1]:
            cell.config(fg='black')
        self.right_clicks += 1

    def hide_last_record(self, event):
        if not self.right_clicks == 0:
            for cell in self.cells[-self.right_clicks]:
                cell.config(fg=self.main_bg)
            self.right_clicks -= 1

    def close(self, event):
        self.master.withdraw()  # if you want to bring it back
        sys.exit()


Display()
mainloop()