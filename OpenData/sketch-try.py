#Script para Ler um aquivo de txt e depois e printar na tela o said 
#como abrir um arquivo
try:
    data = open('sketch.txt')
#criando uma repetição de leitura 
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            pass
    #fechando a leitura terminando com data.close 
    data.close()
except:
    print('Você não tem o arquivo para fazer a leitura !')

    #criei outro metodo de leitura 