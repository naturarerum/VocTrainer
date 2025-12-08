import sys
import csv  
from PySide6.QtWidgets import QFileDialog, QMessageBox


class FileManager:
    """
    Gère les opérations de lecture et d'écriture sur le fichier CSV de vocabulaire.
    """

    def __init__(self):
        self.filename = None

    def read_csv(self):
        """ Lit les données du fichier CSV et les retourne sous forme de liste de dictionnaires. """
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as f:
               # csvreader = csv.reader(csvfile)
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError as e:
            print(f"Error: Unable to find file, Error: {e}")
    
    
    def add_word(self, mot, traduction, categorie):
        """ Ajoute une nouvelle entrée au fichier CSV. """
        
        nouvelle_entree = {'Mot': mot, 'Traduction': traduction, 'Catégorie': categorie}   
        fieldnames = ['Mot', 'Traduction', 'Catégorie'] 
        try:
            with open(self.filename, mode='a', newline='', encoding='utf-8') as f:
                
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(nouvelle_entree)
        except Exception as e:
            print(f"Error: Unable to write to file, Error: {e}")    
       

