gastos = []

while True:
  print()
  print("==============================")
  print("       CONTROLE DE GASTOS")
  print("==============================")

  print()
  print("1) Adicionar gasto")
  print("2) Listar gastos")
  print("3) Ver total de gastos")
  print("4) Sair/Exit")

  opcao = input("Digite uma opção: ")
  print()

  if opcao == "1":
    descricao = input("Descrição do gasto: ")
    valor = float(input("Valor do gasto: "))

    gastos.append([descricao, valor])

    print("Gasto cadastrado!")


  elif opcao == "2":
    for gasto in gastos:
      print(f"{gasto[0]} - R${gasto[1]:.2f}")

    print(f"Gastos cadastrados: {len(gastos)}")


  elif opcao == "3":
    total = 0

    for gasto in gastos:
      total = total + gasto[1]

    print(f"Total gasto: R$ {total:.2f}")

  elif opcao == "4":
    print("Encerrando...")
    break

  else:
    print("Opção inválida!")
