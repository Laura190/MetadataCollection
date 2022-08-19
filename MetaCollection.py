"""
CAMDU Metadata Collection Application
2022 Laura Cooper, camdu@warwick.ac.uk
"""

# Packages
# PyQt
import sys
from PyQt5.QtWidgets import QApplication
import MetaCollApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MetaCollApp.MetaCollApp()
    window.show()
    sys.exit(app.exec())
