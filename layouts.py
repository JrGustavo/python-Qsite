from PySide6.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self):
        super().__init__()
        #Indicamos que se puede colocar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        #Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColot(QPalette.Window, Qcolor(nuevo_color))
        #Aplicamos el nuevo color del componente
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')
        componente_con_color_fondo = Color('red')
        #El componente se expande a cubrir el tamaño disponible
        self.setCentralWidget(componente_con_color_fondo)

if __name__=='__main__':
    app =    QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()