#выполнял один
print("хотите добавить запись, введите 1 \n хотите вывести на экран, введите 2")
print('хотите экспорт, введите 3 \n хотите поменять экспорт введите 5')
print('хотите импорт введите 4 \n хотите завершить введите NO')
def add_a_contact(p):
    file=open('справочник.txt', 'a')
    if p==1:
        name=input("введите имя контакта ")
        number=input('введите номер контакта ')
        description=input('введите описание контакта ')
        return file.write('\n'+name+"; "+number+"; "+description)
    file.close()

def conclusion(p):
    file=open('справочник.txt', 'r')
    if p==2:
        d=file.read()
        return print(d)
    file.close()

def export(p):
    if p==3:
        file=open('справочник.txt', 'r')
        lin=0
        for line in file:
            lin += 1
        lines = [] 
        with open ('справочник.txt', 'rt') as myfile:
            for myline in myfile: 
                lines.append(myline)
        print("сколько номеров вы хотите забрать? ")
        pul=int(input())
        for i in range(pul):##не понимаю, почему он не учитывает i, подскажите пожалуйста
            print("введите фамилию ")
            sername=input()
            for j in range(lin):
                if sername in lines[j]:
                    file2=open('наэкспорт.txt', 'a')
                    return file2.write(lines[j]+'\n')
                file2.close()
def change(p):
    if p==5:
        file=open('наэкспорт.txt', 'r')
        map=file.read()
        file.close
        map2 = map.split()
        file2=open("наэкспорт.txt", 'w')
        print('сколько номеров вы забрали?')
        n=int(input())
        for i in range(4*n):
            file2.write(map2[i]+'\n')
        file2.close


def importing(p):
    if p==4:
        file=open('импорт.txt', 'r')
        lin=0
        for line in file:
            lin += 1
        lines = [] 
        with open ('импорт.txt', 'rt') as myfile:
            for myline in myfile: 
                lines.append(myline)
        print("сколько номеров вы хотите добавить? ")
        pul=int(input())
        for i in range(pul):
            print("введите фамилию ")
            sername=input()
            for j in range(lin):
                if sername in lines[j]:
                    file3=open('справочник.txt', 'a')
                    return file3.write(lines[j]+'\n')
                    file3.close()

continuation="YES"   
while(continuation!="NO"):
    p=int(input())
    add_a_contact(p)
    conclusion(p)
    export(p)
    importing(p)
    change(p)
    print("желаете еще что-то? ")
    continuation=input()
     