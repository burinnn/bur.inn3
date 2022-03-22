documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def p(n,a = "number",b = "name"):
    for i in range(len(documents)):
        if documents[i][a] == n:
            return documents[i][b]
    return "Документ не найден в базе"

def s(n):
    for i in directories:
        if n in directories[i]:
            return i
    return "Документ не найден в базе"

def l():
    for document in documents:
        print(f"№: {document['number']}, тип: {document['type']}, владелец: {document['name']}, полка хранения: {s(document['number'])}")


def main():
    a = input("Введите команду:\n")
    while a != "q":
        if a == "p":
            number = input("Введите номер документа:\n")
            print("Результат:")
            result = p(number)
            if result == "Документ не найден в базе":
                print(result)
            else:
                print(f"Владелец документа: {result}")

        elif a == "s":
            number = input("Введите номер документа:\n")
            print("Результат:")
            result = s(number)
            if result == "Документ не найден в базе":
                print(result)
            else:
                print(f"Документ хранится на полке: {result}")
        elif a == "l":
            l()
        elif a == "ads":
            number = input("Введите номер документа:\n")
            print("Результат:")
            if number in directories:
                print(f"Такая полка уже существует. Текущий перечень полок: {', '.join(directories.keys())}.")
            else:
                directories[number] = []
                print(f"Полка добавлена. Текущий перечень полок: {', '.join(directories.keys())}.")
        elif a == "ds":
            number = input("Введите номер полки:\n")
            print("Результат:")
            if len(directories[number]) > 0:
                print("На полке есть документа, удалите их перед удалением полки.")
                print(f"Текущий перечень полок: {', '.join(directories.keys())}.")
            else:
                directories.pop(number)
                print(f"Полка удалена. Текущий перечень полок: {', '.join(directories.keys())}.")
        elif a == "ad":
            number = input("Введите номер документа:\n")
            type = input("Введите тип документа:\n")
            name = input("Введите владельца документа:\n")
            deck = input("Введите полку для хранения:\n")
            documents.append({'type': type, 'number': number, 'name': name})
            directories[deck].append(number)
            print("Результат:")
            print("Документ добавлен. Текущий список документов:")
            l()
        elif a == "d":
            number = input("Введите номер документа:\n")
            f = False
            for doc in documents:
                if doc['number']==number:
                    documents.remove(doc)
                    f = True
                    break
            print("Результат:")
            if f:
                print("Документ удален.")
                print("Текущий список документов:")
                l()
            else:
                print("Документ не найден в базе.")
                print("Текущий список документов:")
                l()
        elif a == "m":
            number = input("Введите номер документа:\n")
            deck = input("Введите номер полки:\n")
            print("Результат:")
            if not deck in directories:
                print(f"Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}.")
            elif s(number) == "Документ не найден в базе":
                print("Документ не найден в базе")
                print("Текущий список документов:")
                l()
            else:

                directories[s(number)].remove(number)
                directories[deck].append(number)
                print("Документ перемещен.")
                print("Текущий список документов:")
                l()



        a = input("Введите команду:\n")



if __name__ == "__main__":
    main()