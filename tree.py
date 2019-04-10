from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem

app = QApplication([])
window = QWidget()
layout = QVBoxLayout(window)

tw = QTreeWidget()
tw.setHeaderLabels(["Status", "Key", "Value"])
tw.setAlternatingRowColors(True)



cg_1 = QTreeWidgetItem(tw, ["fart", "leaver"])

cg_2 = QTreeWidgetItem(cg_1, ["green", "leaf"])
cg_2.setDisabled(True)
#cg_2.setIcon(icon)

tw.addTopLevelItem(cg_2)



layout.addWidget(tw)
window.show()

app.exec_()
