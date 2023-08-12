#импортируем библиотеки Tkinter, os, и две наши функции из файла tls.py
from tls import translit
from tls import not_translit
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#создаем окно и запрещаем изменение размеров
root = Tk()
root.title("Translit")
root.geometry('650x430')
root.resizable(width=False, height=False)

#описываем функцию для открытия папки с файлами
files = []
#путь возвращается с первого встреченного файла и отображается в окне программы
folderpath = ''
def open_folder():
    global files
    global folderpath
    files = list(filedialog.askopenfilenames())
    list_files = []
    for path_file in files:
        name = []
        for sym in path_file[::-1]:
            if sym != "/":
                name = list(sym) + name

            else:
                break
        join_name = str("".join(name))
        list_files.append(join_name)
    folderpath = files[0][:-len(list_files[0])]
    print(folderpath)
    print(type(folderpath))
    files_var = Variable(value=list_files)
    files_list = Listbox(listvariable=files_var, selectmode=BROWSE, width=39, height=20)
    files_list.grid(column=1, row=1, padx=10, pady=5)
#folderpath = filedialog.askdirectory()

    # txt_label = ttk.Label(text=f'{folderpath}')
    # txt_label.grid(column=0, row=0, padx=[5, 0])
    txt_label = ttk.Entry()
    txt_label.insert(0, f'{folderpath}')
    txt_label.grid(column=0, row=0, ipadx=130, ipady=4, padx=[5, 0])
    return folderpath


#отображение и инициализация функции перевода с русского на транслит
def start_translit():
    result_text = Text(width=48, height=20, wrap="word")
    result_text.grid(column=0, row=1, padx=[5, 0], pady=5)

    for path_file in files:
        result_text.insert("1.0", f"{translit(path_file)}\n")

    result_text.insert(END, f"Завершено\n")
    #os.open(f"{folderpath}", )
    #os.system(f'{folderpath}')
    os.startfile(folderpath)


#отображение и инициализация функции перевода с транслита на русский
def start_not_translit():
    result_text = Text(width=48, height=20, wrap="word")
    result_text.grid(column=0, row=1, padx=[5, 0], pady=5)

    for path_file in files:
        result_text.insert("1.0", f"{not_translit(path_file)}\n")

    result_text.insert(END, f"Завершено\n")
    os.startfile(folderpath)



#описание всех кнопок с указанием рабочих функций
open_button = ttk.Button(text="Выбрать файлы", command=open_folder)
open_button.grid(column=1, row=0, ipadx=55, ipady=4, padx=25)

txt_label = ttk.Entry()
txt_label.insert(0, f'Здесь отобразится путь к файлам')
txt_label.grid(column=0, row=0, ipadx=130, ipady=4, padx=[5, 0])

files_var = Variable()
files_list = Listbox(listvariable=files_var, selectmode=EXTENDED, width=39, height=20)
files_list.grid(column=1, row=1, padx=10, pady=5)

result_text = Text(width=48, height=20)
result_text.grid(column=0, row=1, padx=[5, 0], pady=5)


start_button = ttk.Button(text="Переименовать на Транслит", command=start_translit)
start_button.grid(column=0, row=2, ipadx=105, ipady=6, pady=[10,5])

start_button = ttk.Button(text="Вернуть файлу исходное имя", command=start_not_translit)
start_button.grid(column=1, row=2, ipadx=33, ipady=6, pady=[10,5])


root.mainloop()


