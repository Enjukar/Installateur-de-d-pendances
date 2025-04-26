import tkinter as tk
from tkinter import messagebox, Toplevel
import subprocess
import sys

# Liste des dépendances de base
DEPENDANCES = [
    "pyinstaller",
    "cryptography",
    # Note : tkinter est inclus avec Python de base
]

# Dictionnaire descriptif des dépendances (enrichi)
DESCRIPTIONS = {
    "pyinstaller": "Création de fichiers exécutables (.exe) depuis des scripts Python",
    "cryptography": "Bibliothèque pour la cryptographie (chiffrement, signatures, etc.)",
    "tkinter": "Interface graphique de base (déjà intégré à Python)",
}

def installer_dependances():
    erreurs = []
    for package in DEPENDANCES:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            erreurs.append(package)
    
    if erreurs:
        messagebox.showerror(
            "Erreur",
            f"Erreur lors de l'installation des paquets suivants : {', '.join(erreurs)}"
        )
    else:
        messagebox.showinfo("Succès", "Toutes les dépendances de base ont été installées avec succès !")

def maj_dependances():
    erreurs = []
    for package in DEPENDANCES:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
        except subprocess.CalledProcessError:
            erreurs.append(package)
    
    if erreurs:
        messagebox.showerror(
            "Erreur",
            f"Erreur lors de la mise à jour des paquets suivants : {', '.join(erreurs)}"
        )
    else:
        messagebox.showinfo("Succès", "Toutes les dépendances de base ont été mises à jour avec succès !")

def installer_un_package():
    package = entry.get().strip()
    if package:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
            messagebox.showinfo("Succès", f"Le paquet '{package}' a été installé avec succès.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", f"Erreur lors de l'installation du paquet '{package}'.")
    else:
        messagebox.showwarning("Attention", "Veuillez entrer un nom de paquet.")

def afficher_dependances():
    top = Toplevel(root)
    top.title("Dépendances disponibles")
    top.geometry("500x400")
    
    label = tk.Label(top, text="Liste des dépendances disponibles :", font=("Arial", 12, "bold"))
    label.pack(pady=10)
    
    for package, description in DESCRIPTIONS.items():
        line = f"- {package} : {description}"
        tk.Label(top, text=line, wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

# Fenêtre principale
root = tk.Tk()
root.title("Installateur de Paquets")

# Interface
label = tk.Label(root, text="Nom du paquet à installer:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button_installer = tk.Button(root, text="Installer le paquet", command=installer_un_package)
button_installer.pack(pady=10)

separator = tk.Label(root, text="---------------", fg="gray")
separator.pack(pady=5)

# Note sur les dépendances de base
note_label = tk.Label(root, text="Dépendances de base : pyinstaller, cryptography (Tkinter est inclus avec Python)", fg="blue", wraplength=300, justify="center")
note_label.pack(pady=5)

button_dep = tk.Button(root, text="Installer les dépendances de base", command=installer_dependances)
button_dep.pack(pady=5)

button_maj = tk.Button(root, text="Mettre à jour les dépendances de base", command=maj_dependances)
button_maj.pack(pady=5)

button_afficher = tk.Button(root, text="Afficher la liste des dépendances", command=afficher_dependances)
button_afficher.pack(pady=10)

root.mainloop()
