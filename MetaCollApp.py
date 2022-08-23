from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit, QGridLayout, QTextEdit
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSettings
import csv
import os.path


class home(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        # Window setup
        self.resize(600, 600)
        self.setWindowTitle('Starting a new imaging session?')
        self.setWindowIcon(QIcon('square_black.jpg'))
        self.settings = QSettings()
        # Menu setup
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        load_file_act = QAction('Load', self)
        load_file_act.triggered.connect(self.load_file)
        file_menu.addAction(load_file_act)
        settings_menu = menu_bar.addMenu('&Settings')
        change_settings_act = QAction('&Change Settings', self)
        self.change_settings = Editor(self.settings)
        change_settings_act.triggered.connect(self.change_settings.show)
        settings_menu.addAction(change_settings_act)
        help_menu = menu_bar.addMenu('&Help')
        document = QAction('&Documentation', self)
        # document.triggered.connect(self.change_settings.show)
        help_menu.addAction(document)
        self.setCentralWidget(self.centralWidget())

    def centralWidget(self):
        self.folder = False
        font = self.font()
        font.setPointSize(16)
        self.window().setFont(font)
        folder_lbl = QLabel()
        folder_lbl.setText(
            "Select data folder <html><img height=16 src='info.png'></html>")
        folder_lbl.setToolTip(
            "<html>Select or create folder where you will save the \
            images</html>")
        self.folder_edt = QLineEdit()
        self.folder = self.settings.value('Data Folder')
        self.folder_edt.setText(self.folder)
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
        self.grid = QGridLayout()
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
        w = QWidget()
        w.setLayout(self.grid)
        return(w)

    def get_folder(self):
        self.folder = QFileDialog.getExistingDirectory(
            None, "Select Folder", self.folder_edt.text())
        self.folder_edt.setText(self.folder)

    def save_metadata(self):
        if self.folder and os.path.exists(self.folder):
            meta_dict = {default.split(',')[0]: default.split(',')[
                                       1] for default in self.settings.value('Defaults').replace(', ', ',').split('\n')}
            user_dict = {'Study Component Description': self.description_edt.text(),
                         'Biological Entity': self.bioentity_edt.text(),
                         'Organism': self.organism_edt.text(),
                         'Variables': self.variables_edt.text(),
                         'Other': self.add_edt.toPlainText()}
            meta_dict.update(user_dict)
            with open(self.folder+'/Metadata.csv', 'w', newline='') as csvfile:
                filewriter = csv.writer(csvfile)
                for key in meta_dict:
                    filewriter.writerow([key, meta_dict[key]])
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

    def load_file(self):
        self.file = QFileDialog.getOpenFileName(
                    None, "Select Metadata File", self.folder_edt.text())
        # opening the CSV file
        with open(str(self.file[0]), mode='r')as file:
            reader = csv.reader(file)
            meta_dict = {rows[0]: rows[1] for rows in reader}
            self.description_edt.setText(
                    meta_dict['Study Component Description'])
            self.bioentity_edt.setText(meta_dict['Biological Entity'])
            self.organism_edt.setText(meta_dict['Organism'])
            self.variables_edt.setText(meta_dict['Variables']),
            self.add_edt.setPlainText(meta_dict['Other'])


class Editor(QWidget):
    def __init__(self, settings):
        QWidget.__init__(self)
        self.textEdit = QTextEdit()
        folder_lbl = QLabel()
        folder_lbl.setText("Select default data folder")
        self.folder_edt = QLineEdit()
        browse = QPushButton('Browse')
        browse.clicked.connect(lambda: self.get_folder(settings))
        try:
            self.textEdit.setPlainText(settings.value('Defaults'))
            self.folder_edt.setText(settings.value('Data Folder'))
        except:
            self.textEdit.setPlainText(
                'Imaging Method, None\n Microscope, None')
            self.folder_edt.setText(settings.value(''))
        self.label = QLabel("Settings for all users")
        # Save Button
        save_btn = QPushButton('Save and Close')
        save_btn.clicked.connect(
                    lambda: self.save_settings(settings))
        # Layout
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(folder_lbl, 1, 0)
        layout.addWidget(self.folder_edt, 1, 1)
        layout.addWidget(browse, 1, 2)
        layout.addWidget(self.textEdit, 2, 0, 1, 3)
        layout.addWidget(save_btn, 3, 0, 1, 3)
        self.setLayout(layout)

    def save_settings(self, settings):
        settings.setValue(
                    'Data Folder', self.folder_edt.text())
        settings.setValue(
                    'Defaults', self.textEdit.toPlainText())
        self.close()

    def get_folder(self, settings):
        self.folder = QFileDialog.getExistingDirectory(
                    None, "Select Folder", settings.value('Data Folder'))
        self.folder_edt.setText(self.folder)
