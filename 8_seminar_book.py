
def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            if (line.rstrip('\n').strip('\t').strip()!=""):
                record = dict(zip(fields, list(map(lambda x: x.rstrip('\n').strip('\t').strip(), line.split(',')))))
                #record = list(filter(lambda x: x[0]!="", record))
                #dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
                phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(1,len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    headers=dict(zip(fields, fields))
    if (phone_book[0]['Фамилия']!='Фамилия'):
        phone_book.insert(0, headers)
    max_len = dict()
    for key in fields:
        max_len[key] = len(max(phone_book, key = lambda x: len(x[key]))[key])
    for i in range(len(phone_book)):
        s='|'
        for key, v in phone_book[i].items():
            maximize_v = v
            while len(maximize_v)!=max_len[key]+1:
                maximize_v += " "
            s = s + maximize_v + '|'
        print(f'{s}')
        if (i == 0):
            break_line=""
            while (len(break_line)!=len(s)):
                break_line+='-'
            print(break_line)

def find_by_lastname(phone_book,last_name):
    result = list(filter(lambda x: x['Фамилия'] == last_name, phone_book))
    return result

def find_by_number(phone_book,number):
    result = list(filter(lambda x: x['Телефон'] == number, phone_book))
    return result

def change_number(phone_book,last_name,new_number):
    conut_changes = 0
    for i in range(len(phone_book)):
        if (phone_book[i]['Фамилия'] == last_name):
            phone_book[i]['Телефон'] = new_number
            conut_changes+=1
    return (f"Phone number is changed. Count changes: {conut_changes}")

def add_user(phone_book,user_data):
    u_data=' '.join(user_data.split()) 
    data=user_data.split(" ", 3)
    while len(data) < 4:
        print('Недостаточно данных для добавления абонента')
        new_data=input('new data ')
        data=new_data.split(" ", 3)
    new_record = dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'], data))
    phone_book.append(new_record)
    return (f"User added successfully")

def delete_by_lastname(phone_book,lastname):
    count_del=0
    for_del = []
    for i in range(len(phone_book)):
        if phone_book[i]['Фамилия'] == lastname:
            for_del.append(i)
            count_del+=1
    for i in for_del:
        del phone_book[i]            
    return (f"Number of entries to delete: {count_del}")

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить номер телефона по фамилии\n"
          "5. Добавить абонента в справочник\n"
          "6. Удалить абонента по фамилии\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        #1. Отобразить весь справочник
        if choice==1:
            print_result(phone_book)
        #2. Найти абонента по фамилии
        elif choice==2:
            last_name=input('lastname ')
            print_result(find_by_lastname(phone_book,last_name))           
        elif choice==3:
            number=input('number ')
            print_result(find_by_number(phone_book,number))
        #3. Изменить номер телефона по фамилии
        elif choice==4:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
            save=input('save changes? (y/n) ')
            if (save.lower() == 'y'):
                write_txt('phonebook.txt',phone_book)
                print('Changes saved')
            else:
                phone_book=read_txt('phonebook.txt')
        #4. Добавить абонента в справочник
        elif choice==5:
            user_data=input('new data ')
            print(add_user(phone_book,user_data))
            write_txt('phonebook.txt',phone_book)
        elif choice==6:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
            save=input('save changes? (y/n) ')
            if (save.lower() == 'y'):
                write_txt('phonebook.txt',phone_book)
                print('Changes saved')
            else:
                phone_book=read_txt('phonebook.txt')
        choice=show_menu()


work_with_phonebook()



















