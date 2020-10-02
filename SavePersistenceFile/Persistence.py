man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other man':
                    other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
        print('Está faltando o arquivo')

try:
    man_file = open('man_data.txt', 'w') # W é abrir os arquivos no modo de gravação
    other_file = open('other_data.txt' 'w')
    #ele cria os arquivos man_data.txt e other_data.txt 
    #abre os dois arquivos e atribui cada um dos objetos do arquivo

    print(man, file=man_file)
    print(other, file=other_file)

    man_file.close() # não pode esquecer de fechar os arquivos
    other_file.close()

    #lidando com uma exceção caso ocorra uma 
except IOError:
    print('File error.')
