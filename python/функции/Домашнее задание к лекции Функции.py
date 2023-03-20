documents = [{'type': 'passport',
              'number': '2207 876234',
              'name': 'Василий Гупкин'},
             {'type': 'invoice',
              'number': '11-2',
              'name': 'Геннадий Покемонов'},
             {'type': 'insurance',
              'number': '10006',
              'name': 'Аристарх Павлов'}]

directories = {'1': ['2207 876234', '11-2'],
               '2': ['10006'],
               '3': []}
#p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def ask():
    found = False
    num = input("Введите номер документа:")
    for dic in documents:
        if "number" in dic.keys() and dic["number"] == num:
            print(dic["name"])
            found = True

    if not found:
        print("Документ не найден в базе")
        print("")
     
#s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится        
def shelf(document_number):
    for k in directories:
        if document_number in directories[k]:
            return k
    return "document undefined"
#l – list – команда, которая выведет список всех документов в формате
#passport "2207 876234" "Василий Гупкин"  
def list():
    for x in documents:
        type = x['type']
        number = x['number']
        name = x['name']
        print('{0}"{1}" "{2}"'.format(type, number, name))
        print("")
#d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
def delete(doc_number):
    initial_len = len(documents)
    for i, delete in enumerate(documents):
        if delete["number"] == doc_number:
            documents.pop(i)
    if initial_len == len(documents):
        return "Документ не существует"
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
    return "Документ успешно удален"

print("по команде “p” можно узнать владельца документа по его номеру")
print("по команде “s” можно по номеру документа узнать на какой полке он хранится")
print("по команде “l” можно увидеть полную информацию по всем документам")
print("по команде “ds” можно удалить существующую полку из данных (только если она пустая)")
end_str = 'go'
while end_str == 'go':
    txt = input("Веедите команду : ")
    if txt == "p":
        ask()
    elif txt == "s":
        document_number = input("Введите номер документа: ")
        print("")
        print(shelf(document_number))
        print("")
    elif txt == "l":
        list()
        document_number = input("Введите номер документа: ")
        print(ask(document_number))
    elif txt == "d":
        doc_number = input("Введите номер документа, который хотите удалить: ")
        print("")
        delete(doc_number)
        print("")
        print(documents)
        print("")
        print(directories)
        print("")
    elif txt == "end":
        end_str = 'end'
    else :
        print("Вы ввели", txt , 'такого пункта нету, попробуйте еще раз')
        print("")
