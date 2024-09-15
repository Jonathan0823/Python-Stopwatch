import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.stopwatch_label = QLabel("00:00:00:00",self)
        self.button_start = QPushButton('Start', self)
        self.button_stop = QPushButton('Stop', self)
        self.button_reset = QPushButton('Reset', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 250, 500, 400)
        self.setWindowTitle('Stopwatch')
        self.show()

        self.stopwatch_label.setAlignment(Qt.AlignCenter)

        
        self.setStyleSheet( """QPushButton{
                                font-size: 30px;
                                font-family: Arial;
                                padding: 15px 75px;
                                margin: 20px;
                                border: 3px solid #78acfa;
                                border-radius: 10px;
                                background-color: #b5d2ff;
                                }
                           
                                QPushButton:hover{
                                background-color: #cce0ff;
                                }
                           
                                QLabel{
                                    font-size: 100px;
                                    color: black;
                                    background-color: #b5d2ff;
                                    border-radius: 10px;
                                    border: 3px solid #78acfa;
                                    font-family: Arial;
                                    font-weight: bold;
                                }
                           """)
        
        self.button_start.clicked.connect(self.start)
        self.button_stop.clicked.connect(self.stop)
        self.button_reset.clicked.connect(self.reset)

        vbox = QVBoxLayout()
        vbox.addWidget(self.stopwatch_label)
        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button_start)
        hbox.addWidget(self.button_stop)
        hbox.addWidget(self.button_reset)
        vbox.addLayout(hbox)
        

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)


    def time_format(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f'{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}'


    def update_label(self):
        self.time = self.time.addMSecs(10) 
        self.stopwatch_label.setText(self.time_format(self.time))


    def start(self):
        self.timer.start()
        self.button_start.setEnabled(False)


    def stop(self):
        self.timer.stop()
        self.button_start.setEnabled(True)

    def reset(self):
        self.time = QTime(0,0,0,0)
        self.stopwatch_label.setText(self.time_format(self.time))
        self.button_start.setEnabled(True)
        self.timer.stop()

def main():
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()