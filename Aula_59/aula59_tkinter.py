from tkinter import *
import os

c = os.path.dirname(__file__)
nomeArquivo = c + "\\nomes.txt"

app = Tk()
app.title("O titulo do programa vai aqui")
app.geometry("500x300")
app.configure(background="#dde")

def impDados():
    arquivo = open(nomeArquivo, "a")
    arquivo.write(" Nome....: %s" % vnome.get())
    arquivo.write("\n Telefone: %s" % vfone.get())
    arquivo.write("\n E-mail..: %s" % vemail.get())
    arquivo.write("\n Obs.....: %s" % vobs.get("1.0", END))
    arquivo.write("\n \n")


Label(app, text="Nome", background="#dde", foreground="#009", anchor="w").place(x=10, y=10, width=100, height=20)
vnome = Entry(app)
vnome.place(x=10, y=30, width=200, height=20)

Label(app, text="Telefone", background="#dde", foreground="#009", anchor="w").place(x=10, y=50, width=100, height=20)
vfone = Entry(app)
vfone.place(x=10, y=70, width=200, height=20)

Label(app, text="E-Mail", background="#dde", foreground="#009", anchor="w").place(x=10, y=90, width=100, height=20)
vemail = Entry(app)
vemail.place(x=10, y=110, width=200, height=20)

Label(app, text="OBS:.", background="#dde", foreground="#009", anchor="w").place(x=10, y=130, width=100, height=20)
vobs = Text(app)
vobs.place(x=10, y=150, width=200, height=80)

Button(app,text="Imprimir", command=impDados).place(x=10, y=270, width=100,height=20)

app.mainloop()