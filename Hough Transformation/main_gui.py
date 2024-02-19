import sys
from PyQt5 import QtWidgets
from HoughGUI import HoughGUI
        
if __name__ == "__main__":
    
    # create QApplication window object 
    app = QtWidgets.QApplication([])

    # create an instance from HoughGUI class and call it
    window = HoughGUI()

    # destroy app window
    app.exec()

    # kill python process
    sys.exit()