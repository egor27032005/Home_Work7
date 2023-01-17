#выполнял один
print("хотите добавить запись, введите add \nхотите вывести на экран, введите concl")
print('хотите экспорт, введите exp \nхотите импорт введите import')
print('хотите завершить введите NO')
def add_a_contact(distributor):
    file=open('справочник.txt', 'a')
    if distributor=='add':
        name=input("введите имя контакта ")
        number=input('введите номер контакта ')
        description=input('введите описание контакта ')
        return file.write('\n'+name+"; "+number+"; "+description)
    file.close()

def conclusion(distributor):
    file=open('справочник.txt', 'r')
    if distributor=='concl':
        d=file.read()
        return print(d)
    file.close()

def export(distributor):
    if distributor=="exp":
        line_count = sum(1 for line in open('справочник.txt'))
        file = open('справочник.txt', "r")
        all_sername = []
        line = file.readline().split()
        while line:
            all_sername.extend(line)
            line = file.readline().split()
        file.close()
        file2=open('наэкспорт.txt', 'w')
        print('Если хотите экспортировать в строчку введте row, если в столбик введите column')
        view_exp=input()
        print('введите фамилии, которые хотите exp,чтобы остановиться введите stop.\nесли хотите все, введите all')
        choos_surnam=input()
        k=0
        sername_exp=[]
        sername=''
        if choos_surnam!="all":
            sername_exp.append(choos_surnam)
            while sername!="stop":
                sername=input()
                if sername!="stop":
                    sername_exp.append(sername)
                    k=k+1
            if view_exp=="row":
                for i in range(k+1):
                    for j in range(line_count*4):
                        if sername_exp[i]==all_sername[j]:
                            for t in range(4):
                                file2.write(all_sername[j+t]+' ')
                                if t==3:
                                    file2.write('\n')
            elif view_exp=="column":
                for i in range(k+1):
                    for j in range(line_count*4):
                        if sername_exp[i]==all_sername[j]:
                            for t in range(4):
                                file2.write(all_sername[j+t]+'\n')
                        
        if choos_surnam=='all':
            if view_exp=='column':
                for i in range(line_count*4):
                    file2.write(all_sername[i]+'\n')
            elif view_exp=="row":
                for i in range(line_count*4):
                    file2.write(all_sername[i])
                    k=k+1
                    if k%4==0:
                        file2.write('\n')

        file2.close()
            

def importing(distributor):
    if distributor=="import":
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
                    return file3.write("\n"+lines[j])
                file3.close()

distributor=''   
while(distributor!="NO"):
    distributor=input()
    add_a_contact(distributor)
    conclusion(distributor)
    export(distributor)
    importing(distributor)
    print("желаете еще что-то? ")
     