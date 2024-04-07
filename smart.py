from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
from PyQt5.QtGui import QKeySequence

import json
import os 

def writetofile():
    with open("smart.json","w", encoding ='utf=8') as file:
        json.dump(notes, file )
with open("smart.json","r", encoding ='utf=8') as file:
    notes = json.load(file)

app = QApplication([])
window = QWidget()
width = 600
height = 800



text_editor= QTextEdit()
text_editor.setPlaceholderText("Введіть текст ....")

list_widget_1 = QListWidget()
list_widget_1.setStyleSheet('background-color: pink;')

list_widget_2 = QListWidget()
list_widget_2.setStyleSheet('background-color: pink;')

text_searcher = QLineEdit()
text_searcher.setPlaceholderText("Введіть текст .... ")
text_searcher.setStyleSheet('background-color: green;')

input_dialog = QLineEdit()
input_dialog.setPlaceholderText("Введіть тег .... ")
input_dialog.setStyleSheet('background-color: green;')

make_note= QPushButton()
make_note.setStyleSheet('background-color: green;')
make_note.setText("Створити замітку")

delete_note= QPushButton()
delete_note.setStyleSheet('background-color: green;')
delete_note.setText("Видалити замітку")

save_note= QPushButton()
save_note.setStyleSheet('background-color: green;')
save_note.setText("Зберегти замітку")

search_for_text =QPushButton()
search_for_text.setStyleSheet('background-color: green;')
search_for_text.setText("Шукати замітку по тексту")

search_for_note =QPushButton()
search_for_note.setStyleSheet('background-color: green;')
search_for_note.setText("Шукати замітку за тегом")

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: green;')
add_to_note.setText("Додати до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: green;')
unpin_to_note.setText("Відкріпити від замітки")

action_theme_btn = QPushButton()
action_theme_btn.setText("Змінити тему на чорну")
action_theme_btn.setStyleSheet("background-color: pink;")

export_as_text = QPushButton()
export_as_text.setText("Конвертувати у txt")

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2= QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1= QVBoxLayout()
col1.addWidget(text_editor)

col2= QVBoxLayout()
col2.addWidget(QLabel("Список питать"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів"))
col2.addWidget(list_widget_2)
col2.addWidget(input_dialog)
col2.addWidget(text_searcher)
col2.addLayout(row2)
col2.addWidget(search_for_note)
col2.addWidget(search_for_text)
col2.addWidget(export_as_text)
col2.addWidget(action_theme_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

def search_note():
    tag = input_dialog.text()
    if search_for_note.text() == 'Шукати замітки за тегом'
        filtered_njtes[key]['теги']:
        for key in notes[key] = notes[key]
    search_for_note.setText("Скинути пошук")

    list_widget_1.clear()
    list_widget_1.addItems(filtered_notes)
    list_widget_1.clear()
    text_editor.clear()


    elif search_for_note.text() == 'Скинути пошук':
        search_for_note.setText('Шукати замітки за тегом')
        list_widget_1.clear()
        list_widget_1.addItems(notes)
        text_editor.clear()
        input_dialog.clear()




window.setStyleSheet('background-color: yellow; font-size:20px')
window.setLayout(layout_note)
window.resize(main_width,main_height)
window.show()
app.exec_()