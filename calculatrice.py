import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Calculatrice Futuriste")
fenetre.geometry("320x470")
fenetre.configure(bg="#0d1117")

ecran = tk.Entry(fenetre, font=("Arial", 22), bg="#161b22", fg="#e6edf3", bd=0, justify="right")
ecran.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

def ajouter(val):
    ecran.insert(tk.END, val)

def effacer():
    ecran.delete(0, tk.END)

def calculer():
    try:
        resultat = eval(ecran.get())
        ecran.delete(0, tk.END)
        ecran.insert(0, resultat)
    except:
        ecran.delete(0, tk.END)
        ecran.insert(0, "Erreur")

boutons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

cadre = tk.Frame(fenetre, bg="#0d1117")
cadre.pack()

ligne = 0
col = 0

for b in boutons:
    if b == "=":
        action = calculer
    else:
        action = lambda x=b: ajouter(x)

    tk.Button(
        cadre, text=b, command=action,
        fg="#e6edf3", bg="#238636", font=("Arial", 18),
        width=5, height=2, bd=0
    ).grid(row=ligne, column=col, padx=4, pady=4)

    col += 1
    if col > 3:
        col = 0
        ligne += 1

tk.Button(
    fenetre, text="CLEAR", command=effacer,
    fg="white", bg="#c53030", font=("Arial", 18),
    width=12, height=1, bd=0
).pack(pady=10)

fenetre.mainloop()
