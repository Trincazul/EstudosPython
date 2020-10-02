try:
    with open('its.txt', 'w') as data:
        print("Isso é ... ", file=data)
except IOError as err:
    print('Erro no arquivo', + str(err))

#Quando você usa with, não precisa mais se preocupar em fechar os arquivos close()
