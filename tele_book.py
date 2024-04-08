import sys
import sqlite3  

def menu():   
    print('1. Добавить новый контакт')  
    print('2. Показать контакты')  
    print('3. Редоктировать контакты')  
    print('4. Удалить контакты')
    print('5. Поиск контактов')
    print('0. Выход')

def addcontact():
    while True:  
        name = input("Имя контакта: ") 
        if len(name) != 0:  
            break       
    while True:  
        surname = input("Фамилия контакта: ")  
        if len(surname) != 0:  
            break      
    while True:  
        num = input("Номер телефона контакта: ")    
        if num != 0:  
            break  
    cursor.execute('''INSERT INTO phonebook (name, surname, phone_number) VALUES (?,?,?)''',
                   (name, surname, num))  
    conn.commit()      
    print("Контакт " + surname + ' ' + name + " сохранен")

def showcontact():
    cursor.execute("SELECT surname, name, phone_number FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)

def key_pair_reception(str):
    print ("\nВыберете поле для " + str + " ")  
    print('1. Имя')  
    print('2. Фамилия')  
    print('3. Номер телефона')  
    print('0. Назад в меню')
    n = int(input('Ваш выбор: '))
    if n == 1:  
        field = "name"
        fil = "Имя"
    elif n == 2:  
        field = "surname"
        fil = "Фамилия"
    elif n == 3:  
        field = "phone_number"
        fil = "Номер телефона"
    else:
        return None
    keyword = input("\nВведите " + fil + " = ")
    keypair = field + "='" + keyword + "'"
    return keypair

def editcontacts():
    s = key_pair_reception('поиска')
    u = key_pair_reception('обновления')
    if s != None:
        sql = "UPDATE phonebook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("Контакт изменен.\n")

def deletecontacts():
    s = key_pair_reception('поиска')
    if s != None:
        sql = 'DELETE FROM phonebook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("Контак удален.\n")

def findcontacts():
    s = key_pair_reception('поиска')
    if s != None:
        sql = 'SELECT surname, name, phone_number FROM phonebook WHERE ' + s + ' ORDER BY surname'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)




print ('\nТелефонная книжка')
conn = sqlite3.connect('my.txt')  
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                Имя text NOT NULL,
                Фамилия text,
                Номер text)''')
m = -1  
while m != 0:
    menu()  
    m = int(input('Ваш выбор: '))  
    if m == 1:  
        addcontact()
        continue
    elif m == 2:  
        showcontact()
        continue
    elif m == 3:  
        editcontacts()
        continue
    elif m == 4:  
        deletecontacts()
        continue
    elif m == 5:  
        findcontacts()
        continue
    elif m == 0:  
        print('Пока Пока, До встречи!\n')
        conn.close()
        sys.exit(0)  