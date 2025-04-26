import tkinter as tk
from tkinter import messagebox, Toplevel
import subprocess
import sys
import requests
import zipfile
import os
import io

# URL de la release GitHub - Remplace par l'URL de ton propre repo
GITHUB_REPO = "https://github.com/votre_utilisateur/votre_repo/archive/refs/tags/v1.0.zip"

# Version actuelle du programme
current_version = "v1.0"

def check_for_update():
    """
    Vérifie si une mise à jour est disponible sur GitHub.
    """
    try:
        # Effectuer une requête GET pour récupérer la dernière release
        response = requests.get(f"https://api.github.com/repos/votre_utilisateur/votre_repo/releases/latest")
        response.raise_for_status()
        latest_version = response.json()['tag_name']
        
        if latest_version != current_version:
            if messagebox.askyesno("Mise à jour disponible", f"Une mise à jour est disponible ({latest_version}). Voulez-vous la télécharger ?"):
                update_application(latest_version)
        else:
            messagebox.showinfo("Aucune mise à jour", "Vous avez déjà la dernière version.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de vérifier les mises à jour: {e}")

def update_application(version):
    """
    Télécharge la dernière version du dépôt GitHub et met à jour le programme.
    """
    try:
        # Télécharger le fichier ZIP de la release
        url = f"https://github.com/votre_utilisateur/votre_repo/archive/refs/tags/{version}.zip"
        response = requests.get(url)
        response.raise_for_status()

        # Extraire le fichier ZIP téléchargé
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall("mise_a_jour")  # Extraire dans un dossier temporaire

        # Remplacer les fichiers du projet par ceux téléchargés
        # (ici, on suppose que l'archive contient les mêmes fichiers que ton projet)
        for filename in zip_file.namelist():
            file_path = os.path.join("mise_a_jour", filename)
            if os.path.isfile(file_path):
                dest_path = os.path.join(os.getcwd(), filename.split('/')[-1])  # Remplacer les fichiers à la racine
                os.replace(file_path, dest_path)

        # Afficher un message de réussite
        messagebox.showinfo("Mise à jour réussie", f"La mise à jour vers la version {version} a été effectuée avec succès.")
        # Mettre à jour la version actuelle
        global current_version
        current_version = version
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la mise à jour: {e}")

def installer_dependances():
    """
    Installe les dépendances de base.
    """
    DEPENDANCES = [
        "pyinstaller",
        "cryptography",
    ]
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

def afficher_dependances():
    """
    Affiche la liste des dépendances disponibles.
    """
    top = Toplevel(root)
    top.title("Dépendances disponibles")
    top.geometry("500x400")
    
    label = tk.Label(top, text="Liste des dépendances disponibles :", font=("Arial", 12, "bold"))
    label.pack(pady=10)
    
    for package, description in DESCRIPTIONS.items():
        line = f"- {package} : {description}"
        tk.Label(top, text=line, wraplength=480, justify="left").pack(anchor="w", padx=10, pady=2)

# Dictionnaire descriptif des dépendances (enrichi)
DESCRIPTIONS = {
    "pyinstaller": "Création de fichiers exécutables (.exe) depuis des scripts Python",
    "cryptography": "Bibliothèque pour la cryptographie (chiffrement, signatures, etc.)",
    "tkinter": "Interface graphique de base (déjà intégré à Python)",
}

# Fenêtre principale
root = tk.Tk()
root.title("Installateur de Paquets")

# Interface
label = tk.Label(root, text="Nom du paquet à installer:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button_installer = tk.Button(root, text="Installer le paquet", command=installer_dependances)
button_installer.pack(pady=10)

separator = tk.Label(root, text="---------------", fg="gray")
separator.pack(pady=5)

# Note sur les dépendances de base
note_label = tk.Label(root, text="Dépendances de base : pyinstaller, cryptography (Tkinter est inclus avec Python)", fg="blue", wraplength=300, justify="center")
note_label.pack(pady=5)

button_dep = tk.Button(root, text="Installer les dépendances de base", command=installer_dependances)
button_dep.pack(pady=5)

button_maj = tk.Button(root, text="Vérifier les mises à jour", command=check_for_update)
button_maj.pack(pady=5)

button_afficher = tk.Button(root, text="Afficher la liste des dépendances", command=afficher_dependances)
button_afficher.pack(pady=10)

root.mainloop()
