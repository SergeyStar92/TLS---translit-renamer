#Функция перевода с русского на транслит
def translit(path):
    import os
    # def translit(path):
    #path = input("Введите путь: ")

    #принимается путь до файла и разделяется на две части
    #dr это имя файла
    #newpath это новый путь без имени файла
    dr = os.path.basename(path)
    newpath = path[:-len(dr)]


    #print(newpath)
    #dr = os.listdir(path)
    # print(dr)
    # print(len(dr))
    #print(dr[0])
    #print(file[:-4])

    #алфавит для перевода с русских на английские буквы
    alf = {
        "А" : "A", "Б" : "B", "В" : "V", "Г" : "G", "Д" : "D", "Е" : "E", "Ё" : "Jo",
        "Ж" : "Zh", "З" : "Z", "И" : "I", "Й" : "J", "К" : "K", "Л" : "L", "М" : "M",
        "Н" : "N", "О" : "O", "П" : "P", "Р" : "R", "С" : "S", "Т" : "T", "У" : "U",
        "Ф" : "F", "Х" : "H", "Ц" : "C", "Ч" : "Ch", "Ш" : "Sh", "Щ" : "Shh",
        "Ъ" : "''", "Ы" : "Y", "Ь" : "'", "Э" : "Ye", "Ю" : "Yu", "Я" : "Ya", "а" : "a",
        "б" : "b", "в" : "v", "г" : "g", "д" : "d", "е" : "e", "ё" : "jo", "ж" : "zh",
        "з" : "z", "и" : "i", "й" : "j", "к" : "k", "л" : "l", "м" : "m", "н" : "n",
        "о" : "o", "п" : "p", "р" : "r", "с" : "s", "т" : "t", "у" : "u", "ф" : "f",
        "х" : "h", "ц" : "c", "ч" : "ch", "ш" : "sh", "щ" : "shh", "ъ" : "''",
        "ы" : "y", "ь" : "'", "э" : "ye", "ю" : "yu", "я" : "ya", " " : " ", "_" : "_",
        "." : ".", "!" : "!", "?" : "?", "1" : "1", "2" : "2", "3" : "3", "4" : "4",
        "5": "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "0" : "0", '№' : '№',
        '-' : '-'
    }

#если нет исключений выполняй функции ниже
    try:
        #функция перевода на транслит имени файла без расширения
        def trlt(file):
            res = []
            for i in file:
                pr = alf[i]
                res = res + list(pr)

            result = "".join(res)
            return result
        #цикл определяющий расширение в каждом файле
        #если в перевернутом имени переменная j не встретила точку
        #то счетчик считает эти символы
        #если встретилась точка то цикл прекращается
        cnt = 0
        for j in dr[::-1]:
            if j != ".":
                cnt += 1
            elif j == ".":
                break
        #extencion это расширение которое извлекается из имени вместе с точкой cnt+1
        extencion = dr[-(cnt + 1):]
        #orig это имя файла без расширения
        orig = str(dr[:-(cnt + 1)])

        #переименовываем в папке файлы и склеиваем все части путь, имя, расширение
        os.rename(newpath + orig + extencion, newpath + trlt(orig) + extencion)

        #возвращаем сообщение об успешном переименовании
        return f'Файл {orig}{extencion} переименован в {trlt(orig)}{extencion}'

    #отлавливаем исключения и ворачиваем сообщения
    except KeyError:
        return "Файл не на русском языке"
    except FileNotFoundError:
        return "Файла не существует"



#Функция перевода с транслита на русский
def not_translit(path):
    import os
    # def translit(path):
    #path = input("Введите путь: ")
    dr = os.path.basename(path)
    newpath = path[:-len(dr)]
    #print(newpath)
    #dr = os.listdir(path)
    # print(dr)
    # print(len(dr))


    #print(dr[0])
    #print(file[:-4])
    alf = {
        "A" : "А", "B" : "Б", "V" : "В", "G" : "Г", "D" : "Д", "E" : "Е", "Jo" : "Ё",
        "Zh" : "Ж", "Z" : "З", "I" : "И", "J" : "Й", "K" : "К", "L" : "Л", "M" : "М",
        "N" : "Н", "O" : "О", "P" : "П", "R" : "Р", "S" : "С", "T" : "Т", "U" : "У",
        "F" : "Ф", "H" : "Х", "C" : "Ц", "Ch" : "Ч", "Sh" : "Ш", "Shh" : "Щ",
        "''" : "Ъ", "Y" : "Ы", "'" : "Ь", "Ye" : "Э", "Yu" : "Ю", "Ya" : "Я", "a" : "а",
        "b" : "б", "v" : "в", "g" : "г", "d" : "д", "e" : "е", "jo" : "ё", "zh" : "ж",
        "z" : "з", "i" : "и", "j" : "й", "k" : "к", "l" : "л", "m" : "м", "n" : "н",
        "o" : "о", "p" : "п", "r" : "р", "s" : "с", "t" : "т", "u" : "у", "f" : "ф",
        "h" : "х", "c" : "ц", "ch" : "ч", "sh" : "ш", "shh" : "щ", "''" : "ъ",
        "y" : "ы", "'" : "ь", "ye" : "э", "yu" : "ю", "ya" : "я", " " : " ", "_" : "_",
        "." : ".", "!" : "!", "?" : "?", "1" : "1", "2" : "2", "3" : "3", "4" : "4",
        "5": "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9", "0" : "0", '№' : '№',
        '-' : '-'
    }

    try:

        def trlt(file):
            res = []
            for i in file:
                pr = alf[i]
                res = res + list(pr)

            result = "".join(res)
            return result
        #col = 0
        #if col <= len(dr):
            #for i in range(len(dr)):
        cnt = 0
        for j in dr[::-1]:
            if j != ".":
                cnt += 1
            elif j == ".":
                break
        extencion = dr[-(cnt + 1):]
        orig = str(dr[:-(cnt + 1)])

        os.rename(newpath + orig + extencion, newpath + trlt(orig) + extencion)

        return f'Файл {orig}{extencion} переименован в {trlt(orig)}{extencion}'


    except KeyError:
        return "Файл не на транслите"
    except FileNotFoundError:
        return "Файла не существует"



