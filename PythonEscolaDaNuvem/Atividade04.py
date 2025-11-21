# Atividade 04 - Vários exercícios

# 1 - Calculadora básica
def calculadora():
	print("Calculadora básica")
	try:
		a = float(input("Digite o primeiro número: "))
		op = input("Escolha a operação (+, -, *, /): ")
		b = float(input("Digite o segundo número: "))
	except ValueError:
		print("Entrada inválida: digite um número válido.")
		return

	if op == "+":
		resultado = a + b
	elif op == "-":
		resultado = a - b
	elif op == "*":
		resultado = a * b
	elif op == "/":
		if b == 0:
			print("Erro: divisão por zero.")
			return
		resultado = a / b
	else:
		print("Operação inválida.")
		return

	print(f"Resultado: {resultado}")


# 2 - Registrar notas dos alunos e calcular média da turma
def registrar_notas():
	print("\nRegistro de notas e média da turma")
	try:
		n = int(input("Quantos alunos deseja cadastrar? "))
		if n <= 0:
			print("Número de alunos deve ser maior que zero.")
			return
	except ValueError:
		print("Entrada inválida: digite um número inteiro.")
		return

	alunos = []
	soma = 0.0
	for i in range(1, n+1):
		nome = input(f"Nome do aluno {i}: ").strip()
		while True:
			try:
				nota = float(input(f"Nota do(a) {nome}: "))
				break
			except ValueError:
				print("Nota inválida. Digite um número (ex: 7.5).")
		alunos.append((nome, nota))
		soma += nota

	media = soma / n
	print("\nNotas registradas:")
	for nome, nota in alunos:
		print(f"- {nome}: {nota}")
	print(f"Média da turma: {media:.2f}")


# 3 - Verificador de senha (mínimo 8 caracteres e pelo menos um número)
def verificar_senha():
	print("\nVerificador de senha")
	senha = input("Digite a senha para verificação: ")
	erros = []
	if len(senha) < 8:
		erros.append("deve ter pelo menos 8 caracteres")
	if not any(ch.isdigit() for ch in senha):
		erros.append("deve conter pelo menos um número")

	if not erros:
		print("Senha atende aos critérios básicos de segurança.")
	else:
		print("Senha NÃO atende aos critérios:")
		for e in erros:
			print(f"- {e}")


# 4 - Analisar números: classificar pares e ímpares e contar quantos de cada
def classificar_pares_impares():
	print("\nClassificador de pares e ímpares")
	try:
		total = int(input("Quantos números você vai digitar? "))
		if total <= 0:
			print("Quantidade deve ser maior que zero.")
			return
	except ValueError:
		print("Entrada inválida: digite um número inteiro.")
		return

	pares = 0
	impares = 0
	lista_pares = []
	lista_impares = []

	for i in range(1, total+1):
		while True:
			try:
				num = int(input(f"Digite o número {i}: "))
				break
			except ValueError:
				print("Entrada inválida. Digite um número inteiro.")

		if num % 2 == 0:
			pares += 1
			lista_pares.append(num)
		else:
			impares += 1
			lista_impares.append(num)

	print(f"\nTotal de números: {total}")
	print(f"Pares ({pares}): {lista_pares}")
	print(f"Ímpares ({impares}): {lista_impares}")


# Executa os exercícios em sequência, no formato das atividades anteriores
print("Atividade 04 - Exercícios")
calculadora()
registrar_notas()
verificar_senha()
classificar_pares_impares()

