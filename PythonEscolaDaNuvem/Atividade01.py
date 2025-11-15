#Programa de saudação

print('Olá Mundo")')

#Calculadora de Soma 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é: {soma}")

#Calculadora de Volume 

comprimento = float(input("Digite o comprimento do paralelepípedo (em cm): "))
largura = float(input("Digite a largura do paralelepípedo (em cm): "))
altura = float(input("Digite a altura do paralelepípedo (em cm): "))
volume = comprimento * largura * altura
print(f"O volume do paralelepípedo é: {volume} cm³")

#Calculadora de Preço Total 

nomeProduto = input("Digite o nome do produto: ")
precoUnitario = float(input("Digite o preço unitário do produto (em R$): "))
quantidade = int(input("Digite a quantidade desejada: "))
precoTotal = precoUnitario * quantidade
print(f"O preço total para {quantidade} unidades de {nomeProduto} é: R$ {precoTotal:.2f}!")
