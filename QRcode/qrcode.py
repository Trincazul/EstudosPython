import pyqrcode
site = input('Digite o site para gerar o QRcode: ')
url = pyqrcode.create(site)
# cria uma imagem em png do QRcode
url.svg('meuqr.svg', scale=8)
url.eps('meuqr.eps', scale=2)
# print no terminal
print(url.terminal(quiet_zone=1))
