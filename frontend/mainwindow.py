# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QVBoxLayout, QPushButton, QStackedWidget, QFrame
from PySide6.QtCore import Qt
import subprocess
import json
from PySide6.QtGui import QPixmap, QFont, QFontDatabase
import csv

#font addition




#finds the drives from the computer
driveListfile = open("./drives.csv", "r")
reader = csv.reader(driveListfile)
driveListpretty = []
driveList = []
for i in list(reader):
    driveListpretty.append(f"{i[0][5:]}:{i[1]} ({i[2].strip()}) | {i[3].strip()} {i[4]}")
    driveList.append(i)
driveListfile.close()


#1st Page
class Page_1(QWidget):


    def next_page(self):
        chosen_drive = self.combo_box.currentText()
        chosen_drive_number = self.combo_box.currentIndex()
        response = open("./response.csv", "w")
        writer = csv.writer(response)
        writer.writerow([i.strip() for i in driveList[chosen_drive_number]])
        self.page2.label1.setText(f"<font size = 4>Your chosen drive is <font color = red>{chosen_drive}</font></font>")
        self.stack.setCurrentIndex(1)
    
        
    def __init__(self, stacked_widget, page2):
        super().__init__()
        font_id = QFontDatabase.addApplicationFont("bergstena.ttf")
        if font_id==-1:
            print("Failed to load font")
            lucida = QFont("Arial", 20)
        else:
            print("Success")
            lucida = QFontDatabase.applicationFontFamilies(font_id)
            lucida = QFont(lucida[0], 20)

        self.stack = stacked_widget
        self.page2 = page2
        #background image [NOT WORKING]

        '''self.bg_label = QLabel(self) 
        self.bg_label.setPixmap(QPixmap("bg.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()
        self.bg_label.resize(self.size())'''


        #inner layout

        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(4)
        self.frame.setFont(QFont("lucon.ttf", 10))
        layout = QVBoxLayout(self.frame)

        #widgets on screen

        self.label1 = QLabel("<font color = red size = 7>BitReaper 1.0</font>")
        self.label2 = QLabel("<font size = 5> Select the drive you need to wipe: </font>")
        self.label2.setStyleSheet("padding:15px")
        layout.addWidget(self.label1, alignment = Qt.AlignCenter)
        layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        self.combo_box = QComboBox(self)
        self.combo_box.setMaximumWidth(200)
        self.combo_box.addItems([item for item in driveListpretty])
        font_box = QFont()
        font_box.setPointSize(16)
        self.combo_box.setFont(font_box)
        self.combo_box.setFixedSize(300, 25)
        layout.addWidget(self.combo_box, alignment = Qt.AlignCenter)

        self.NextButton = QPushButton("Next")
        self.NextButton.setFixedSize(100, 25)
        layout.addWidget(self.NextButton, alignment= Qt.AlignCenter)
        self.NextButton.clicked.connect(self.next_page)

        layout.setSpacing(75)
        layout.setContentsMargins(0,0,0,0)
        outer_layout = QVBoxLayout()
        outer_layout.addStretch()
        outer_layout.addWidget(self.frame, alignment=Qt.AlignCenter)
        outer_layout.addStretch()
        self.setLayout(outer_layout)


#2nd Page
class Page_2(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stack = stacked_widget
        layout = QVBoxLayout()
        #self.setFont(lucida)

        self.label1 = QLabel("<font size = 3>Your chosen drive is</font>")
        layout.addWidget(self.label1, alignment=Qt.AlignTop)
        self.setLayout(layout)
    def prev_page(self):
        self.stack.setCurrentIndex(0)

#main
if __name__ == "__main__":
    app = QApplication([])
    stacker  = QStackedWidget()
    stacker.setWindowTitle("BitReaper 1.0")
    stacker.setMinimumSize(800,600)
    page2 = Page_2(stacker)
    page1 = Page_1(stacker, page2)
    stacker.addWidget(page1)
    stacker.addWidget(page2)
    stacker.setCurrentIndex(0)
    stacker.showMaximized()
    sys.exit(app.exec())
