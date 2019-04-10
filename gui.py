from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

app = QApplication([])

label = QLabel("Hola")
#label.show()

layout = QVBoxLayout()
layout.addWidget(label)

window = QWidget()
window.setLayout(layout)
window.show()

app.exec_()
