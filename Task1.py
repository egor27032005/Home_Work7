
def add_a_contact(p):
    file=open('справочник.txt', 'a')
    if p==1:
        name=input("введите имя контакта ")
        number=input('введите номер контакта ')
        description=input('введите описание контакта ')
        return file.write(name+"\n"+number+"\n"+description)
    file.close()
def conclusion(p):
    file=open('справочник.txt', 'r')
    if p==2:
        d=file.read()
        return print(d)
    file.close()
def export(p):
    if p==3:
        mylines = [] 
        with open ('справочник.txt', 'rt') as myfile:
            for myline in myfile: 
                mylines.append(myline)
        print("сколько номеров вы хотите забрать? ")
        pul=int(input())
        for i in range(pul):
            print("введите фамилию ")
            sername=input()
            for j in range(6):
                if sername in mylines[j]:
                    file2=open('наэксорт.txt', 'a')
                    return file2.write(mylines[j]+'\n')
                file2.close()


continuation="YES"   
while(continuation!="NO"):
    s=int(input())
    add_a_contact(s)
    conclusion(s)
    export(s)
    print("желаете еще что-то? ")
    continuation=input()
     