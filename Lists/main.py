import random;
import sys;
from PySide6 import QtCore, QtWidgets, QtGui;

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(student_names))

def open_window():
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()
    sys.exit(app.exec())

# Defining two lists: one for student names and another for their corresponding grades
student_names = ["Rory", "Caden", "Leon", "Joy", "Nima", "Trent"]
student_grades = [25, 100, 95, 99, 96, 101]

# Accessing elements using positive indexing (Random)
print(random.choice(student_names))

# Accessing elements using negative indexing
print(student_grades[-5])

# Getting the length of the student_grades list
print(len(student_grades))
open_window();

student_names[0] = "Alex"  # Modifying the first element of the student_names list
student_names.append("Sam")  # Adding a new student name to the end of the list
student_names.remove("Joy")  # Removing a student name from the list
student_names.insert(0, "AJ")  # Sorting the student_names list in ascending order
print(student_names)
print("Caden" in student_names)  # Checking if "Caden" is in the student_names list
