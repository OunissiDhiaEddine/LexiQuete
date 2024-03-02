import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtGui import QPixmap , QFont, QFontDatabase
from PyQt5.QtGui import QPalette, QBrush
from PyQt5.QtCore import Qt, QRect, QEasingCurve, QPropertyAnimation, QTimer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LexQuete")
        self.setGeometry(100, 100, 700, 500)
        self.setFixedSize(700, 500)
    
        background = QPixmap("assets/sky2.jpg").scaled(self.size())
        brush = QBrush(background)
        palette = QPalette()
        palette.setBrush(QPalette.Background, brush)
        
        # Set the palette and the font
        self.setPalette(palette)
        QFontDatabase.addApplicationFont("/Users/didou/Developer/Projects/LexiQuete/fonts/noodle.ttf")

        left_layout = QVBoxLayout()

        logo_label = QLabel()
        pixmap = QPixmap("assets/logo3.png")
        pixmap = pixmap.scaled(400, 400,)  
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(logo_label)

        text_label = QLabel("A L3 ISIL Project / Module RI / Group 5")
        text_label.setFont(QFont("BigNoodleTitling", 20))
        text_label.setStyleSheet("color: #0a3556")
        left_layout.addWidget(text_label)

        text_label2= QLabel("Developed by:\n● Ounissi Dhia eddine \n● Rasoul Anis \n● Serir Louai Abdelmouiz \n● Hadil med Chérif \n● Assia nezar kebaiLi \n● Kara nesrine \n")
        text_label2.setWordWrap(True)
        text_label2.setStyleSheet("font-size: 12px")
        text_label2.setStyleSheet("color: #16cbaf")
        left_layout.addWidget(text_label2)
        
     
        

        # Right Side
        right_layout = QVBoxLayout()
    
        big_text_label = QLabel("LexQuete is a text analyzing program that allows you \nto preform multiple operations on your selected file")
        big_text_label.setWordWrap(True)
        big_text_label.setContentsMargins(10, 60, 10, 0)
        big_text_label.setFont(QFont("BigNoodleTitling", 26))
        right_layout.addWidget(big_text_label)

        bigger_text_label = QLabel("Let's start by choosing a file \n(english .txt or .docx)")
        bigger_text_label.setWordWrap(True)
        bigger_text_label.setContentsMargins(0, 150, 0, 0)
        bigger_text_label.setFont(QFont("BigNoodleTitling", 22))
        bigger_text_label.setStyleSheet("color: #000000")
        right_layout.addWidget(bigger_text_label)

        choose_file_button = QPushButton("Choose File")
        choose_file_button.setStyleSheet("background-color: #f99e1a; color: white; font-size: 15px; padding: 10px 15px; border-radius: 10px; border: none;")
        right_layout.addWidget(choose_file_button)

        
        
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

        
