menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
saque = 0

while True:

	opcao = input(menu)

	if opcao == "d":
		print("Depósito")
		deposito = int(input("Informe o valor do depósito: "))
		print("Depositando...")
		saldo += deposito
		extrato += f"""
Depósito no valor de R$ {deposito:.2f} realizado
		"""
		print("Depósito realizado com sucesso.")

	elif opcao == "s":
		print("Saque")
		if numero_saque <= LIMITE_SAQUE:
			saque = int(input("Informe o valor do saque: "))
		
			if saldo >= saque:
				print("Sacando...")
				saldo -= saque
				numero_saque +=1
				extrato += f"""
Saque no valor de R$ {saque:.2f} realizado
				"""
				print("Saque realizado com sucesso!")
			else:
				print("Saldo insuficiente para realizar o saque.")

		else:
			print("Limite de saques diários ultrapassado.")
	
	elif opcao == "e":
		print("Extrato")
		print("Exibindo o extrato...")
		print(f"""
============= EXTRATO =============
			{extrato}

Saldo: R$ {saldo:.2f}
===================================
		"""
		)

	elif opcao == "q":
		print("Obrigado por usar nosso sistema bancário, até logo!")
		break

	else:
		print("Operação inválida, por favor selecione novamente a operação desejada.")
