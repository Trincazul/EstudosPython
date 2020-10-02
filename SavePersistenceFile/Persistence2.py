try:
    man_file = open('man_data.txt', 'w') # W é abrir os arquivos no modo de gravação
    other_file = open('other_data.txt', 'w')
    #ele cria os arquivos man_data.txt e other_data.txt 
    #abre os dois arquivos e atribui cada um dos objetos do arquivo

    print(man, file=man_file)
    print(other, file=other_file)

    man_file.close() # não pode esquecer de fechar os arquivos
    other_file.close()

    #lidando com uma exceção caso ocorra uma 
except IOError:
    print('Erro no arquivo.')

finally:
    man_file.close()
    other_file.close()