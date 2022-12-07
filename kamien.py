import tkinter as tk

root = tk.Tk()
root.geometry("1100x700")
zmienna1 = tk.IntVar()
zmienna2 = tk.IntVar()

def printinput(*args):
   print(zmienna1.get())
def printinput(*args):
   print(zmienna2.get())
text = tk.StringVar
root.title("Kalkulator")
message2 = tk.Label(root, text='Kółko i krzyżyk ',  fg= 'black', font=("bold", 30, "italic"))
message2.grid(row=1 )
message2.place(relx=0.5, rely=0.090, anchor=tk.CENTER)
wskazowka = tk.Label(root, text='Wybierz poziom trudności',  fg= 'black', font=("bold", 20, "italic"))
wskazowka.grid(row=1 )
wskazowka.place(relx=0.5, rely=0.190, anchor=tk.CENTER)
textbox1 = tk.Entry(root, textvariable=zmienna1 , font=('Times', 24))
textbox1.place(relx=0.2, rely=0.290, anchor=tk.CENTER, width=256, height= 50)
opcje = ['Łatwiutki','Średnio','Trudny']
textbox2 = tk.Entry(root, textvariable=zmienna2 , font=('Times', 24) )
textbox2.place(relx=0.8, rely=0.290, anchor=tk.CENTER, width=256, height= 50)

opcja =tk.StringVar(value="WYBIERZ")


dropdown = tk.OptionMenu(root, opcja, *opcje )
dropdown.pack()
dropdown.grid(row=5,column=4)
dropdown.place(relx=0.5, rely=0.300, anchor=tk.CENTER, width=256, height= 50)
dropdown.config(font=('Times', 24))
message3 = tk.Label(root,   fg= 'black', font=("bold", 30, "italic"))
message3.grid(row=1 )
message3.place(relx=0.5, rely=0.530, anchor=tk.CENTER)





root.resizable(False, False)    

root.mainloop()





