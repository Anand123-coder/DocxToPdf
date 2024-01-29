import tkinter as tk 
from docx2pdf import convert
from tkinter.filedialog import askopenfile
from tkinter import messagebox


win = tk.Tk()
win.title('Docx2pdf')

def openFile():
    file= askopenfile(filetypes=[('word files ', '*.docx')])
    convert(file.name)
    messagebox.showinfo('Done','File Successfully converted')
label=tk.Label(win,text='Choose File: ')
label.grid(row=0,column=0)

button= tk.Button(win, text="----Select----",width=30,command=openFile )
button.grid(row=0,column=1)
win.mainloop()