
#Testando tratamento de erro, quando arquivo não existe para abrir
try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError:
    print('Erro no arquivo!')
finally:
    if 'data' in locals():
        data.close()

