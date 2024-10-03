import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QVBoxLayout, QMainWindow, 
    QMenuBar, QMenu, QAction, QFileDialog, QMessageBox, 
    QHBoxLayout, QPushButton
)

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 900, 700)
        self.setWindowTitle("pyedit")
        
        # Menu bar starting
        self.menu = self.menuBar()
        # Menu list
        self.file_menu = self.menu.addMenu('File')
        self.edit_menu = self.menu.addMenu('Edit')
        
        # Menu actions
        # File menu Actions
        self.new_file_action = QAction('New', self)
        self.open_file_action = QAction('Open', self)
        self.save_file_action = QAction('Save', self)
        self.exit_action = QAction('Exit', self)
        
        # Add File menu actions
        self.file_menu.addAction(self.new_file_action)
        self.file_menu.addAction(self.open_file_action)
        self.file_menu.addAction(self.save_file_action)
        self.file_menu.addAction(self.exit_action)
        
        # Edit menu Actions
        self.undo_action = QAction('Undo', self)
        self.redo_action = QAction('Redo', self)
        
        # Add Edit menu actions
        self.edit_menu.addAction(self.undo_action)
        self.edit_menu.addAction(self.redo_action)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.textbox_layout = QVBoxLayout()
        self.text_box = QTextEdit(self)
        self.textbox_layout.addWidget(self.text_box)
        self.central_widget.setLayout(self.textbox_layout)
        
        # Connect the menu actions
        self.new_file_action.triggered.connect(self.new_file)
        self.open_file_action.triggered.connect(self.open_file)
        self.save_file_action.triggered.connect(self.save_file)
        self.exit_action.triggered.connect(self.close)
        self.undo_action.triggered.connect(self.undo)
        self.redo_action.triggered.connect(self.redo)

    def new_file(self):
        self.text_box.clear()    

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", 
            "Text Files (*.txt);;Python Files (*.py);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                self.text_box.setText(file.read())

    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", 
            "Text Files (*.txt);;Python Files (*.py);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.text_box.toPlainText())

    def undo(self):
        if self.text_box.document().isUndoAvailable():
            self.text_box.undo()
        else:
            QMessageBox.information(self, "Undo", "Nothing to undo available.")

    def redo(self):
        if self.text_box.document().isRedoAvailable():
            self.text_box.redo()
        else:
            QMessageBox.information(self, "Redo", "Nothing to redo available.")
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())
