import os
#import que fala se o arquivo existe ou não path-exist.
#aquivo com outro metodo de tratamento de leitura de arquivo 
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')

    data.close()
else:
    print('Você precisa do arquivo sketch.txt !')