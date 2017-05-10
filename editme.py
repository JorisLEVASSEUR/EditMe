from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


master = Tk()
master.title("NoteMe")
master.geometry("400x300")

text = Text(master, width=400, height=380, font=("Andale Mono", 12), highlightthickness=0, bd=2)
text.pack()

# Methods

def new():
    ans = messagebox.askquestion(title="Sauvegarder", message="Veux tu sauvegarder ce fichier ?")
    if ans is True:
        save()
    deleteAll()

def openFile():
   new()
   file = filedialog.askopenfile()
   text.insert(INSERT, file.read())

def save():
    path = filedialog.asksaveasfilename()
    write = open(path, mode ='w')
    write.write(text.get("1.0", END))



def close():
    save()
    master.quit()

def cut():

    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)

def copy():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())

def paste():
    text.insert(INSERT, master.clipboard_get())

def delete():
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)

def selectAll():
    text.tag_add(SEL, "1.0", END)

def deleteAll():
    text.delete(1.0, END)


# Menu

menu = Menu(master)
master.config(menu=menu)
file_menu = Menu(menu)
menu.add_cascade(label="Fichier", menu=file_menu)

file_menu.add_command(label="Nouveau",command=new)
file_menu.add_command(label="Ouvrir", command=openFile)
file_menu.add_separator()
file_menu.add_command(label="Fermer", command=close)
file_menu.add_command(label="Sauvegarder", command=save)

# Edit Menu

editMenu = Menu(menu)
menu.add_cascade(label="Edition", menu=editMenu)
editMenu.add_command(label="Annuler", command=text.edit_undo)
editMenu.add_command(label="Avancer", command=text.edit_redo)
editMenu.add_separator()
editMenu.add_command(label="Couper", command=cut)
editMenu.add_command(label="Copier", command=copy)
editMenu.add_command(label="Coller", command=paste)
editMenu.add_command(label="Supprimmer", command=delete)
editMenu.add_separator()
editMenu.add_command(label="Tout selectionner", command=selectAll)

master.mainloop()
