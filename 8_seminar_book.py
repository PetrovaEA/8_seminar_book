def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice

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
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def print_result(phone_book):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    headers=dict(zip(fields, fields))
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
            break_line="";
            while (len(break_line)!=len(s)):
                break_line+='-'
            print(break_line)














def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))	    	
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        choice=show_menu()


work_with_phonebook()


















