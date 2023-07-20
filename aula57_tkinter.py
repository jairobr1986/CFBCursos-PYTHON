from tkinter import *

app = Tk()
app.title("TIDAI")
app.geometry("500x300")
app.configure(background="#D3D3D3")

txt1 = Label(app, text="Menu do Programa", background="#fff", foreground="#007")
txt1.place(x=10, y=10, width=150, height=20)

vtxt = "INTRODUÇÃO"
vbg = "#ff0"
vfg = "#000"
txt2 = Label(app,text=vtxt, bg=vbg, fg=vfg)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=Y, expand=True)

app.mainloop()