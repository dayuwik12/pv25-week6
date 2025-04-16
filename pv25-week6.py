import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QSlider, QGroupBox, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class FontCustomizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font Customizer and Color Adjuster Ida Ayu Dewi Purnama Anjani")
        self.setGeometry(600, 300, 800, 400)
        self.setStyleSheet("background-color: #2b2b2b; color: white;")
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # GroupBox untuk label NIM
        nim_group = QGroupBox()
        nim_group.setStyleSheet("QGroupBox { border: none; }")
        nim_layout = QVBoxLayout()

        # Label NIM
        self.label = QLabel("F1D022050", self)
        self.label.setFont(QFont("Times New Roman", 40))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 0, 0);")
        self.label.setFixedHeight(200)  # Tetapkan tinggi tetap untuk label NIM
        nim_layout.addWidget(self.label)

        # Spacer yang digunkana untuk memastikan area label lebih luas
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        nim_layout.addSpacerItem(spacer)

        nim_group.setLayout(nim_layout)
        layout.addWidget(nim_group)

        # Slider font size
        layout.addWidget(self.create_slider_group("Font size", 20, 60, self.update_font_size))

        # Slider background color
        layout.addWidget(self.create_slider_group("Background Color", 0, 255, self.update_background_color))

        # Slider font color
        layout.addWidget(self.create_slider_group("Font Color", 0, 255, self.update_font_color))

        self.setLayout(layout)

    def create_slider_group(self, title, min_val, max_val, slot_function):
        group = QGroupBox()
        group.setStyleSheet("QGroupBox { border: none; }")
        layout = QHBoxLayout()

        label = QLabel(title)
        label.setFixedWidth(160)
        layout.addWidget(label)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(min_val + max_val // 2)
        slider.valueChanged.connect(slot_function)
        layout.addWidget(slider)

        group.setLayout(layout)
        return group

    def update_font_size(self, value):
        font = self.label.font()
        font.setPointSize(value)
        self.label.setFont(font)

    def update_background_color(self, value):
        style = self.label.styleSheet()
        font_color = self.extract_color(style, "color")
        self.label.setStyleSheet(f"color: {font_color}; background-color: rgb({value},{value},{value});")

    def update_font_color(self, value):
        style = self.label.styleSheet()
        bg_color = self.extract_color(style, "background-color")
        self.label.setStyleSheet(f"color: rgb({value}, {value}, {value}); background-color: {bg_color};")

    def extract_color(self, style, key):
        for part in style.split(";"):
            if key in part:
                return part.split(":")[1].strip()
        return "rgb(255,255,255)"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontCustomizer()
    window.show()
    sys.exit(app.exec_())