# Classificador de idade

def classificar_idade(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade <= 19:
        return "Adolescente"
    elif idade <= 64:
        return "Adulto"
    else:
        return "Idoso"
    
print("Classificador de Idade")
idade = int(input("Digite a sua idade: "))
categoria = classificar_idade(idade)
print(f"Você é classificado como: {categoria}")

# Calculadora de IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
print("\nCalculadora de IMC")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calcular_imc(peso, altura)
categoria_imc = classificar_imc(imc)
print(f"Seu IMC é: {imc:.2f}, classificado como: {categoria_imc}")

# Conversor de temperaturas celsius, fahrenheit e kelvin

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_para_kelvin(celsius):
    return celsius + 273.15
print("\nConversor de Temperaturas")
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)
kelvin = celsius_para_kelvin(celsius)
print(f"{celsius}°C é igual a {fahrenheit:.2f}°F e {kelvin:.2f}K")

# Verificador de Ano Bissexto 

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False
print("\nVerificador de Ano Bissexto")
ano = int(input("Digite um ano: "))
if eh_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")



