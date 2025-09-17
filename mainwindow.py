# This Python file uses the following encoding: utf-8

import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QVBoxLayout, QPushButton, QStackedWidget, QFrame, QGridLayout
from PySide6.QtCore import Qt, QThread, Signal
import subprocess
import json
from PySide6.QtGui import QPixmap, QFont, QFontDatabase, QMovie
import csv
import time
#font addition
import os

subprocess.run(["./getdrive.sh"])
class WorkerThread1(QThread):
    finished = Signal()

    def run(self):
        #subprocess.run(["./wipe.sh"])
        os.system("./wipe.sh")
        #time.sleep(500)
        self.finished.emit()

class WorkerThread2(QThread):
    finished = Signal()

    def run(self):
        #subprocess.run(["./test.sh"])
        os.system("./wipe.sh")
        #time.sleep(400)
        self.finished.emit()


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
        '''font_id = QFontDatabase.addApplicationFont("bergstena.ttf")
        if font_id==-1:
            print("Failed to load font")
            lucida = QFont("Arial", 20)
        else:
            print("Success")
            lucida = QFontDatabase.applicationFontFamilies(font_id)
            lucida = QFont(lucida[0], 20)'''

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

        # Frame and inner layout
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(4)

        layout = QVBoxLayout(self.frame)
        layout.setSpacing(30)

        self.label1 = QLabel("<font size = 5>Your chosen drive is</font>")
        self.label2 = QLabel("<font size = 5>Are you sure you want to continue?</font>")
        self.label3 = QLabel("<font size = 5>(THIS WILL BEGIN THE WIPE PROCESS)</font>")

        layout.addWidget(self.label1, alignment=Qt.AlignCenter)
        layout.addWidget(self.label2, alignment=Qt.AlignCenter)
        layout.addWidget(self.label3, alignment=Qt.AlignCenter)

        # Button layout inside the frame
        button_layout = QGridLayout()
        self.yes = QPushButton("Yes")
        self.no = QPushButton("No")
        self.yes.setFixedSize(100, 25)
        self.no.setFixedSize(100, 25)

        button_layout.addWidget(self.yes, 0, 0)
        button_layout.addWidget(self.no, 0, 1)
        layout.addLayout(button_layout)

        # Outer layout for centering
        outer_layout = QVBoxLayout()
        outer_layout.addStretch()
        outer_layout.addWidget(self.frame, alignment=Qt.AlignCenter)
        outer_layout.addStretch()

        self.setLayout(outer_layout)

        # Example navigation signal (optional)
        self.no.clicked.connect(self.prev_page)

        self.yes.clicked.connect(self.begin_process)

    def prev_page(self):
        self.stack.setCurrentIndex(0)

    def begin_process(self):
        self.stack.setCurrentIndex(2)
        self.stack.widget(2).start_process()
        #subprocess.run(['./wipe.sh'])


#3rd Page
class Page_3(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stack = stacked_widget
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(4)

        self.layout = QVBoxLayout(self.frame)
        self.layout.setSpacing(30)
        self.label = QLabel("<font size = 4>Processing Data Wipe:")
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.spinner = QLabel()
        #self.movie = QMovie("loading.gif")  # Put a real spinner gif here
        #self.spinner.setMovie(self.movie)
        self.layout.addWidget(self.spinner, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        self.thread = WorkerThread1()
        self.thread.finished.connect(self.end_process)

    def start_process(self):
        #self.movie.start()
        self.thread.start()

    def end_process(self):
        #self.movie.stop()
        self.label.setText("Finished")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.stack.setCurrentIndex(3)
        self.stack.widget(3).start_process()

#4th Page
class Page_4(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(4)

        self.layout = QVBoxLayout(self.frame)
        self.layout.setSpacing(10)
        self.label = QLabel("<font size = 4>Verifying Data Wipe</font>")
        self.layout.addWidget(self.label, alignment=Qt.AlignCenter)

        self.spinner = QLabel()
        #self.movie = QMovie("loading.gif")  # Put a real spinner gif here
        #self.spinner.setMovie(self.movie)
        self.layout.addWidget(self.spinner, alignment=Qt.AlignCenter)

        self.setLayout(self.layout)

        self.thread = WorkerThread2()
        self.thread.finished.connect(self.end_process)

    def start_process(self):
        #self.movie.start()
        self.thread.start()

    def end_process(self):
        #self.movie.stop()
        self.label.setText("<font size = =6>Finished Data Wipe</font>")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        




#main
if __name__ == "__main__":
    app = QApplication([])
    stacker  = QStackedWidget()
    stacker.setWindowTitle("BitReaper 1.0")
    stacker.setMinimumSize(800,600)
    page2 = Page_2(stacker)
    page1 = Page_1(stacker, page2)
    page3 = Page_3(stacker)
    page4 = Page_4(stacker)
    stacker.addWidget(page1)
    stacker.addWidget(page2)
    stacker.addWidget(page3)
    stacker.addWidget(page4)
    stacker.setCurrentIndex(0)
    stacker.resize(400,300)
    stacker.show()
    sys.exit(app.exec())
