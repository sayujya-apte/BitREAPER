# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QVBoxLayout
from PySide6.QtCore import Qt
import subprocess
import json
from PySide6.QtGui import QPixmap

def listDrives():
    cmd = ["powershell", "-Command", "Get-PhysicalDisk | Select-Object FriendlyName | ConvertTo-Json"]
    result = subprocess.run(cmd, capture_output = True, text = True)
    disks = json.loads(result.stdout)
    if isinstance(disks, dict):
            disks = [disks]
    return [disk["FriendlyName"] for disk in disks if "FriendlyName" in disk]

dic = listDrives()

class Page_1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BitReaper v1.0")
        self.showMaximized()

        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(QPixmap("bg.jpg"))
        self.bg_label.setScaledContents(True)  # scales image to widget size
        self.bg_label.lower()

        layout = QVBoxLayout()
        self.label1 = QLabel("<font color = red size = 100>BitReaper 1.0</font>")
        layout.addWidget(self.label1, alignment = Qt.AlignCenter)

        self.combo_box = QComboBox(self)
        self.combo_box.setMaximumWidth(200)
        self.combo_box.addItems(dic)
        self.combo_box.setFixedSize(350, 25)
        layout.addWidget(self.combo_box, alignment = Qt.AlignCenter)

        self.label = QLabel("Selected: None", self)
        layout.addWidget(self.label)

        self.combo_box.currentIndexChanged.connect(self.update_label)

        layout.setSpacing(100)
        layout.setContentsMargins(0,0,0,0)
        outer_layout = QVBoxLayout()
        outer_layout.addStretch()
        outer_layout.addLayout(layout)
        outer_layout.addStretch()
        self.setLayout(outer_layout)
        self.update_label(self.combo_box.currentIndex())   

    def update_label(self, index):
        selected_item = self.combo_box.currentText()
        self.label.setText(f"Selected: {selected_item}")


'''class Page_2(QWidget):
    super().__init__()
    def __init__(self):
        self.setWindowTitle("BitReaper v1.0")
        self.showMaximized()

        self.label1 = QLabel("Your chosen drive is ")'''



if __name__ == "__main__":
    app = QApplication([])
    window = Page_1()
    window.show()
    sys.exit(app.exec())
