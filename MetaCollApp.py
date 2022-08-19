from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QTextEdit
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction
from PyQt5.QtGui import QIcon
import csv
import os.path


class MetaCollApp(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        # Window setup
        self.resize(600, 600)
        self.setWindowTitle('Starting a new imaging session?')
        self.setWindowIcon(QIcon('square_black.jpg'))
        self.folder = False
        font = self.font()
        font.setPointSize(16)
        self.window().setFont(font)
        # Menu setup
        menu_bar = self.menuBar()
        settings_menu = menu_bar.addMenu('&Settings')
        change_settings = QAction('&Change Settings', self)
        change_settings.triggered.connect(self.change_settings)
        settings_menu.addAction(change_settings)
        help_menu = menu_bar.addMenu('&Help')
        document = QAction('&Documentation', self)
        document.triggered.connect(self.change_settings)
        help_menu.addAction(document)
        folder_lbl = QLabel()
        folder_lbl.setText(
            "Select data folder <html><img height=16 src='info.png'></html>")
        folder_lbl.setToolTip(
            "<html>Select or create folder where you will save the \
            images</html>")
        self.folder_edt = QLineEdit()
        browse = QPushButton('Browse')
        browse.clicked.connect(self.get_folder)  # change to get folder path
        description_lbl = QLabel()
        description_lbl.setText(
            "Description <html><img height=16 src='info.png'></html>")
        description_lbl.setToolTip(
            "Briefly describe your aim for today's imaging session")
        self.description_edt = QLineEdit()
        bioentity_lbl = QLabel()
        bioentity_lbl.setText(
            "Biological Entity <html><img height=16 src='info.png'></html>")
        bioentity_lbl.setToolTip(
            "What is being imaged? Try to use an ontology entry")
        self.bioentity_edt = QLineEdit()
        organism_lbl = QLabel()
        organism_lbl.setText(
            "Organism <html><img height=16 src='info.png'></html>")
        organism_lbl.setToolTip(
            "Species. Try to use a taxonomy entry")
        self.organism_edt = QLineEdit()
        variables_lbl = QLabel()
        variables_lbl.setText(
            "Variables <html><img height=16 src='info.png'></html>")
        variables_lbl.setToolTip(
            "<html>What's changed? May include intrisic (e.g. genetic), \
            extrinsic (e.g. reagent) and/or experimental (e.g. time) \
            variables</html>")
        self.variables_edt = QLineEdit()
        add_lbl = QLabel()
        add_lbl.setText(
                    "Other <html><img height=16 src='info.png'></html>")
        add_lbl.setToolTip(
                    "<html>Any other information you would like to include</html>")
        self.add_edt = QTextEdit()
        # Save Button
        save_btn = QPushButton('Save')
        save_btn.clicked.connect(self.save_metadata)
        # Save and Close Button
        close_btn = QPushButton('Save and Close')
        close_btn.clicked.connect(self.save_and_close)
        # Layout
        self.grid = QGridLayout(self)
        self.grid.addWidget(folder_lbl, 0, 0)
        self.grid.addWidget(self.folder_edt, 0, 1)
        self.grid.addWidget(browse, 0, 2)
        self.grid.addWidget(description_lbl, 1, 0)
        self.grid.addWidget(self.description_edt, 1, 1, 1, 2)
        self.grid.addWidget(bioentity_lbl, 2, 0)
        self.grid.addWidget(self.bioentity_edt, 2, 1, 1, 2)
        self.grid.addWidget(organism_lbl, 3, 0)
        self.grid.addWidget(self.organism_edt, 3, 1, 1, 2)
        self.grid.addWidget(variables_lbl, 4, 0)
        self.grid.addWidget(self.variables_edt, 4, 1, 1, 2)
        self.grid.addWidget(add_lbl, 5, 0)
        self.grid.addWidget(self.add_edt, 5, 1, 1, 2)
        self.grid.addWidget(save_btn, 6, 1)
        self.grid.addWidget(close_btn, 6, 2)

    def get_folder(self):
        self.folder = QFileDialog.getExistingDirectory(
                None, "Select Folder", "/home/laura")
        self.folder_edt.setText(self.folder)

    def save_metadata(self):
        if self.folder and os.path.exists(self.folder):
            with open(self.folder+'/Metadata.csv', 'w') as csvfile:
                filewriter = csv.writer(
                    csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(
                    ['Study Component Description', self.description_edt.text()])
                filewriter.writerow(
                    ['Biological Entity', self.bioentity_edt.text()])
                filewriter.writerow(['Organism', self.organism_edt.text()])
                filewriter.writerow(['Variables', self.variables_edt.text()])
                filewriter.writerow(['Other', self.add_edt.toPlainText()])
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Please select an existing folder")
            msg.setWindowTitle("Folder Missing")
            msg.setStandardButtons(QMessageBox.Ok)
            # start the app
            msg.exec_()

    def save_and_close(self):
        self.save_metadata()
        exit()

    def change_settings(self):
        print("change settings")
