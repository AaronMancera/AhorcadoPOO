import sys
import PyQt5.QtWidgets as QtWidgets

class Window:
    def __init__(self) -> None:
        pass
    def crear_ventana(self):
        app = QtWidgets.QApplication(sys.argv)
        win = QtWidgets.QMainWindow()
        win.show()        
        sys.exit(app.exec_())