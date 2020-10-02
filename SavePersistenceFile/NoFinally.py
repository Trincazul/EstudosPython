#lembrar de comentar pra executar um por um

try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man, file=man_file)
    print(other, file=other_file)
except IOError as err:
    print('Erro no arquivo: ' + str(err))
finally:
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()

# usando instrução with

try:
    with open('man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('other_man.txt' 'w') as other_file:
        print(other, file=other_file)
except IOError as err:
    print('File error:' + str(err))

# usando duas instruções with para reescrever o código sem o conjunto finally

with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
    print(man, file=man_file)
    print(other, file=other_file)

    