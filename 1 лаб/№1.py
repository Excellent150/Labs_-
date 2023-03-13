f = open ('mygroup.txt', encoding='utf-8')
f.readline()
name, surname, marks = [], [], []
for c in f:
    c = c.strip()
    if len(c) > 3:
        if "Name" in c:
            name.append(c[9:-2])
        if "surname" in c:
            surname.append(c[12:-2])
        if "marks" in c:
            marks.append(c[10:-1:3])

s = float(input())
for i in range(len(name)):
    if (int(marks[i][0]) + int(marks[i][1]) + int(marks[i][2])) / 3 >= s:
        print(name[i], surname[i], '\n',(int(marks[i][0]) + int(marks[i][1]) + int(marks[i][2]))/3)