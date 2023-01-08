import tkinter as tk
import random 

root = tk.Tk()
root.geometry("1100x700")
twoj_wynik=0
wynik_przeciwnika=0

twoj_ruch=""

opcja=tk.StringVar(value="Łatwiutki")
zmienna=""
opcje = ['Łatwiutki','Średnio','Trudny']
ruchy_przeciwnika = ['papier','kamien','nozyce']
def jezeli_papier():
    global zmienna,twoj_ruch
    zmienna= "papier"
    if zmienna == "papier":
      komunikat.config(text="Wybrałeś papier !")
      twoj_ruch="papier"
      potwierdzanie = tk.Button(root,text="potwierdz" ,font=('Times', 24), command=po_potwierdzeniu)
      potwierdzanie.place(relx=0.5, rely=0.790, anchor=tk.CENTER, width=256, height= 50)  
def jezeli_kamien():
    global zmienna,twoj_ruch
    zmienna= "kamien"
    if zmienna == "kamien":
      komunikat.config(text="Wybrałeś kamień! ")
      twoj_ruch="kamien"
      potwierdzanie = tk.Button(root,text="potwierdz" ,font=('Times', 24), command=po_potwierdzeniu)
      potwierdzanie.place(relx=0.5, rely=0.790, anchor=tk.CENTER, width=256, height= 50)
def jezeli_nozyce():
    global zmienna,twoj_ruch
    zmienna= "nozyce"
    if zmienna == "nozyce":
      komunikat.config(text="Wybrałeś nozyce! ")
      twoj_ruch="nozyce"
      potwierdzanie = tk.Button(root,text="potwierdz" ,font=('Times', 24), command=po_potwierdzeniu)
      potwierdzanie.place(relx=0.5, rely=0.790, anchor=tk.CENTER, width=256, height= 50)
choice=""
enemychoice=""
def display_selected(choice):
    choice = opcja.get()
    print(choice)
    if opcja.get():
        wynik_przeciwnika=0
        twoj_wynik=0
        entrybox1.config(text= twoj_wynik)
        entrybox2.config(text= wynik_przeciwnika)
    

def po_potwierdzeniu():
   if opcja.get() =="Łatwiutki":
     
      global twoj_wynik,wynik_przeciwnika
      
      if twoj_ruch == "kamien":
         komunikat.config(text="Wygrałeś kamieniem na nożyce! ",fg= 'black')
         twoj_wynik += 1
         entrybox1.config(text= twoj_wynik)
      if twoj_ruch == "papier":
         komunikat.config(text="Wygrałeś papierem na kamien! ",fg= 'black')
         twoj_wynik += 1
         entrybox1.config(text= twoj_wynik)
      if twoj_ruch == "nozyce":
         komunikat.config(text="Wygrałeś nozycami na papier!! ",fg= 'black')
         twoj_wynik += 1
         entrybox1.config(text= twoj_wynik)
   elif opcja.get() =="Średnio":
      
      
      enemychoice = random.choice(ruchy_przeciwnika)
       
      if twoj_ruch == enemychoice:
        komunikat.config(text="remis ",fg= 'black')
      elif twoj_ruch == "kamien":     
         if enemychoice =="nozyce":
             komunikat.config(text="Wygrałeś kamieniem na nożyce! ",fg= 'black')
             twoj_wynik += 1
             entrybox1.config(text= twoj_wynik)
         else:
            komunikat.config(text="Przegrałeś kamieniem na papier!",fg= 'black')
            wynik_przeciwnika += 1
            entrybox2.config(text= wynik_przeciwnika)
      elif twoj_ruch == "papier":     
         if enemychoice =="kamien":
             komunikat.config(text="Wygrałeś papierem na kamien! ",fg= 'black')
             twoj_wynik += 1
             entrybox1.config(text= twoj_wynik)
         else:
            komunikat.config(text="Przegrałeś papierem na nozyce!!",fg= 'black')
            wynik_przeciwnika += 1
            entrybox2.config(text= wynik_przeciwnika)
      elif twoj_ruch == "nozyce":     
         if enemychoice =="papier":
             komunikat.config(text="Wygrałeś nożycami na papier! ",fg= 'black')
             twoj_wynik += 1
             entrybox1.config(text= twoj_wynik)
         else:
            komunikat.config(text="Przegrałeś nożycami na kamień!!!",fg= 'black')
            wynik_przeciwnika += 1
            entrybox2.config(text= wynik_przeciwnika)
   elif opcja.get() =="Trudny":
      
      if twoj_ruch =="kamien":
          komunikat.config(text="Przegrałeś kamieniem na papier!",fg= 'black')
          wynik_przeciwnika += 1
          entrybox2.config(text= wynik_przeciwnika)
      elif twoj_ruch =="papier":
          komunikat.config(text="Przegrałeś papierem na nozyce!",fg= 'black')
          wynik_przeciwnika += 1
          entrybox2.config(text= wynik_przeciwnika)
      elif twoj_ruch =="nozyce":
         komunikat.config(text="Przegrałeś nozycami na kamien!!",fg= 'black')
         wynik_przeciwnika += 1
         entrybox2.config(text= wynik_przeciwnika)
   if twoj_wynik>9:
      twoj_wynik=0
      wynik_przeciwnika=0
      komunikat.config(text="WYGRAŁEŚ GRE!",fg= 'green')
      entrybox1.config(text= twoj_wynik)
      entrybox2.config(text= wynik_przeciwnika)
   elif wynik_przeciwnika>9:
      twoj_wynik=0
      wynik_przeciwnika=0
      komunikat.config(text="PRZEGRAŁEŚ GRE!",fg= 'red')
      entrybox1.config(text= twoj_wynik)
      entrybox2.config(text= wynik_przeciwnika)
   elif twoj_wynik-3 == wynik_przeciwnika:
      twoj_wynik=0
      wynik_przeciwnika=0
      komunikat.config(text="WYGRAŁEŚ GRE!",fg= 'green')
      entrybox1.config(text= twoj_wynik)
      entrybox2.config(text= wynik_przeciwnika)
   elif wynik_przeciwnika-3 == twoj_wynik:
      twoj_wynik=0
      wynik_przeciwnika=0
      komunikat.config(text="PRZEGRAŁEŚ GRE!",fg= 'red')
      entrybox1.config(text= twoj_wynik)
      entrybox2.config(text= wynik_przeciwnika)


text = tk.StringVar
root.title("Kalkulator")
message2 = tk.Label(root, text='Kamień, papier nożyce ',  fg= 'black', font=("bold", 30, "italic"))
message2.grid(row=1 )
message2.place(relx=0.5, rely=0.090, anchor=tk.CENTER)
autor = tk.Label(root, text='Kamil Janowski 3TPA',  fg= 'black', font=("bold", 15, "italic"))
autor.grid(row=1 )
autor.place(relx=0.5, rely=0.050, anchor=tk.CENTER)
wskazowka = tk.Label(root, text='Wybierz poziom trudności',  fg= 'black', font=("bold", 20, "italic"))
wskazowka.grid(row=1 )
wskazowka.place(relx=0.5, rely=0.190, anchor=tk.CENTER)
textbox1 = tk.Label(root, text='Pkt użytkownika', font=('Times', 24))
textbox1.place(relx=0.2, rely=0.290, anchor=tk.CENTER, width=256, height= 50)
entrybox1 = tk.Label(root,text="0", font=('Times', 24))
entrybox1.pack
entrybox1.place(relx=0.2, rely=0.390, anchor=tk.CENTER, width=256, height= 50)
textbox2 = tk.Label(root, text="PKT WROGA" , font=('Times', 24) )
textbox2.place(relx=0.8, rely=0.290, anchor=tk.CENTER, width=256, height= 50)
entrybox2 = tk.Label(root,text="0", font=('Times', 24) )
entrybox2.place(relx=0.8, rely=0.390, anchor=tk.CENTER, width=256, height= 50)
dropdown = tk.OptionMenu(root, opcja, *opcje, command=display_selected )
dropdown.pack()
dropdown.grid(row=5,column=4)
dropdown.place(relx=0.5, rely=0.300, anchor=tk.CENTER, width=256, height= 50)
dropdown.config(font=('Times', 24))
opcjapapier = tk.Button(root, text="papier" , font=('Times', 24),command=jezeli_papier)
opcjapapier.place(relx=0.2, rely=0.490, anchor=tk.CENTER, width=256, height= 50)
opcjakamien = tk.Button(root, text="kamień" ,font=('Times', 24),command=jezeli_kamien)
opcjakamien.place(relx=0.5, rely=0.490, anchor=tk.CENTER, width=256, height= 50)
opcjanozyce = tk.Button(root, text="nożyce" ,font=('Times', 24),command=jezeli_nozyce)
opcjanozyce.place(relx=0.8, rely=0.490, anchor=tk.CENTER, width=256, height= 50)
komunikat = tk.Label(root , font=('Times', 30) )
komunikat.place(relx=0.5, rely=0.690, anchor=tk.CENTER, width=706, height= 50)




   
    

root.resizable(False, False)    

root.mainloop()





