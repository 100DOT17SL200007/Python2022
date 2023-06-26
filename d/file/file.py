#1.задача

with open('w.txt', 'w') as f:
    f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
pos1 = int(input('1: '))
pos2 = int(input('2: '))

with open('w.txt', 'r') as file:
    line = file.readlines()
if pos1 == 1 and pos2 == 2:
    line[0], line[1] = line[1], line[0]
elif pos1 == 1 and pos2 == 3:
    line[0], line[2] = line[2] + '\n', line[0]
elif pos1 == 2 and pos2 == 3:
    line[1], line[2] = line[2] + '\n', line[1]
else:
    print('Error')

with open('w.txt', 'w') as f:
    f.writelines(line)

#2.задача

# with open('w.txt', 'w') as f:
#     f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
#
# with open('w.txt', 'r') as file:
#     line = file.readlines()
# line[-1] = line[-1] + '\n'
# lines = line[::-1]
#
# with open('w.txt', 'w') as files:
#     files.writelines(lines)

#3.задача
# with open('w.txt', 'r') as f1, open('w.txt', 'r') as f2, open('w.txt', 'w') as f3:
#    file_1 = f1.readlines()
#    file_2 = f2.readlines()
#    f3.writelines(file_1 + file_2)
