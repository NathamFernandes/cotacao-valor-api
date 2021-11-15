import pip._vendor.requests
import json
import time

while True:
    valreal = float(input('Insira a quantidade de dinheiro você possui, em R$: '))
    identi = input('Insira o código da moeda que você pretende converter (USD, EUR, etc.): ').upper()

    cotacoes = pip._vendor.requests.get("https://economia.awesomeapi.com.br/json/all")
    cotacoes = cotacoes.json()
    cotacao = float(cotacoes[identi]['bid'])

    time.sleep(1.5)
    print(' ')
    print('Cotação atual do {}: {:.2f}'.format(identi, cotacao))

    valabso = valreal/cotacao

    time.sleep(1.5)
    print('Convertendo R$ {:.2f} em {}, o valor total é de: {} {:.2f}.'.format(valreal, identi, identi, valabso))
    print(' ')

    time.sleep(3)
    x = int(input('Gostaria de rodar o programa novamente? \n - Se sim, digite "1". \n - Se não, digite "2". \n'))
    time.sleep(1)
    if x == 2:
        break

