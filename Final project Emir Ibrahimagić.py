import tkinter as tk
from tkinter import messagebox


pitanja = [
    "Koliko igrača čini jedan tim u košarci?",
    "Ko je naslikao Mona Lisu?",
    "Koje su tri osnovne boje? a=plava, crvena, žuta. b=plava, žuta, zelena. c=crvena, žuta, ljubičasta?",
    "Koja je najveća planeta u Sunčevom sistemu?",
    "Koja životinja može spavati naopačke?",
    "Zašto astronauti lede u svemiru? a=nema kisika, b=nema gravitacije, c=previše gravitacije",
    "Koji je hemijski simbol za vodu?",
    "Koji je najtvrđi materijal na svijetu?",
    "Koja je formula za izračunavanje gustine tijela?",
    "Koji kontinent ima najviše država?",
    "Ko se smatra osnivačem dinastije Kotromanića?",
    "Ko je napisao Pinokija?",
    "Koji je najpoznatiji web pretraživač?",
    "Koliko iznosi pi (π) (bar 5 brojeva)?",
    "Ko je najbolji šahista?"
]

odgovori = [
    "5", "LEONARDO DA VINCI", "A", "JUPITER", "ŠIŠMIŠ",
    "B", "H2O", "DIJAMANT", "M/V", "AFRIKA",
    "STJEPAN KOTROMANIC", "KARLO KOLODI", "GOOGLE CHROME", "3.1415", "MAGNUS CARLSEN"
]


score = 0
trenutno_pitanje = 0

def provjeri_odgovor():
    global score, trenutno_pitanje

    odgovor = entry.get().upper()
    if odgovor == odgovori[trenutno_pitanje]:
        score += 1
        messagebox.showinfo("Tačno!", "Odgovor je tačan!")
    else:
        messagebox.showerror("Netačno", f"Netačan odgovor. Tačan je: {odgovori[trenutno_pitanje]}")

    trenutno_pitanje += 1

    if trenutno_pitanje < len(pitanja):
        pitanje_label.config(text=pitanja[trenutno_pitanje])
        entry.delete(0, tk.END)
    else:
        prikazi_rezultat()

def prikazi_rezultat():
    root.destroy()

    rezultat = tk.Tk()
    rezultat.title("Rezultat")
    rezultat.geometry("400x200")

    tekst = f"Osvojili ste {score} poena."

    if score == 0:
        preporuka = "Igra preporučena za tebe je Iks Oks."
    elif 0 < score < 6:
        preporuka = "Igra preporučena za tebe je Fortnite."
    elif 5 < score < 11:
        preporuka = "Igra preporučena za tebe je Roblox."
    else:
        preporuka = "Igra preporučena za tebe je Šah."

    label_rezultat = tk.Label(rezultat, text=tekst + "\n" + preporuka, font=("Arial", 14))
    label_rezultat.pack(pady=50)

    


root = tk.Tk()
root.title("Kviz")
root.geometry("600x300")


pitanje_label = tk.Label(root, text=pitanja[trenutno_pitanje], font=("Arial", 14))
pitanje_label.pack(pady=20)


entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)


dugme = tk.Button(root, text="Potvrdi odgovor", command=provjeri_odgovor)
dugme.pack(pady=20)
