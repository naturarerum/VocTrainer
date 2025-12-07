from PySide6.QtCore import QSize
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow, QWidget,QApplication,QTableWidget,QFileDialog,QTableWidgetItem,QMessageBox
from filemanager import FileManager 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vocab")
        self.setMinimumSize(QSize(400, 300))
        # L'instance du gestionnaire de fichiers
        self.manager = FileManager()
        # Liste pour stocker les données en mémoire
        self.vocabulaire = []
        
        # Initialisation de l'UI
        self.setup_ui()
       

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()
        # Afficher la table vide au démarrage
        self.display_csv_data()

    def create_widgets(self):
        self.load_button = QPushButton("Ouvrir Fichier...")
        self.tbl_vocab = QTableWidget()
        self.tbl_vocab.setColumnCount(3) # 3 colonnes fixes
        self.tbl_vocab.setHorizontalHeaderLabels(['Mot', 'Traduction', 'Catégorie'])
        # Ajuster les colonnes pour prendre l'espace disponible
        self.tbl_vocab.horizontalHeader().setStretchLastSection(True)

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QVBoxLayout(self)
        

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.load_button)
        self.main_layout.addWidget(self.tbl_vocab)
        

    def setup_connections(self):
        self.load_button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        """ Ouvre QFileDialog pour sélectionner un fichier CSV et charge les données. """
        
        # Ajout du filtre pour ne montrer que les fichiers CSV
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Sélectionner un fichier Vocabulaire CSV",
            "", # Dossier de départ
            "Fichiers CSV (*.csv);;Tous les fichiers (*)"
        )

        if filename:
            try:
                # 1. Met à jour le gestionnaire de fichiers avec le nom
                self.manager.filename = filename
                
                # 2. Charge les données dans la liste en mémoire
                self.vocabulaire = self.manager.read_csv()
                
                # 3. Affiche les données
                self.display_csv_data()
                
                self.setWindowTitle(f"Vocab - {filename}")
                QMessageBox.information(self, "Chargement Réussi", f"Le fichier **{filename}** a été chargé.")

            except Exception as e:
                QMessageBox.critical(self, "Erreur de Chargement", f"Impossible de lire le fichier : {e}")
                self.vocabulaire = [] # Vide les données en cas d'erreur
                self.display_csv_data()
        else:
            print("Sélection de fichier annulée.")
            
    def display_csv_data(self):
        """ Affiche les données du self.vocabulaire dans le QTableWidget. """
        
        # 1. Réinitialiser le tableau
        self.tbl_vocab.setRowCount(0)
        
        if not self.vocabulaire:
            return

        # 2. Définir le nombre de lignes
        self.tbl_vocab.setRowCount(len(self.vocabulaire))

        # 3. Remplir le tableau ligne par ligne
        for row_index, entry in enumerate(self.vocabulaire):
            # Créer des QTableWidgetItem pour chaque colonne
            mot_item = QTableWidgetItem(entry.get('Mot', ''))
            traduction_item = QTableWidgetItem(entry.get('Traduction', ''))
            categorie_item = QTableWidgetItem(entry.get('Catégorie', ''))
            
            # Insérer les QTableWidgetItem dans les colonnes de self.tbl_vocab
            self.tbl_vocab.setItem(row_index, 0, mot_item)     # Colonne 0 : Mot
            self.tbl_vocab.setItem(row_index, 1, traduction_item) # Colonne 1 : Traduction
            self.tbl_vocab.setItem(row_index, 2, categorie_item) # Colonne 2 : Catégorie
            
            

app = QApplication([])
window = MainWindow()
window.show()
app.exec()