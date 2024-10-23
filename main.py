import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QFileDialog

from app.service.extract_text_from_pdf import process_pdf, process_image

class OCRApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('OCR PDF to Text')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.btn_select_file = QPushButton('Select PDF', self)
        self.btn_select_file.clicked.connect(self.select_pdf_file)

        self.btn_process = QPushButton('Process PDF', self)
        self.btn_process.clicked.connect(self.process_pdf)
        self.btn_process.setEnabled(False)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        layout.addWidget(self.btn_select_file)
        layout.addWidget(self.btn_process)
        layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.pdf_path = None

    def select_pdf_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if file_name:
            self.pdf_path = file_name
            self.btn_process.setEnabled(True)

    def process_pdf(self):
        if self.pdf_path:
            images = process_pdf(self.pdf_path)
            text = process_image(images)
            self.text_edit.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OCRApp()
    window.show()
    sys.exit(app.exec_())
