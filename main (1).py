from funcoes import avaliar_orcamento, calc_autonomia, calc_consumo_medio, calc_custo_combustivel, calc_paradas, calc_consumo_medio, comparar_veiculos, avaliar_orcamento


while True:
        print("\n===== MENU =====")
        print("1. Consumo Médio")
        print("2. Calcular Custo do Combustível")
        print("3. Calcular Autonomia")
        print("4. Calcular Paradas")
        print("5. Comparar Veículos")
        print("6. Avaliar Orçamento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            km = float(input("Digite a quantidade de quilômetros que irá percorrer:  "))
            litros = float(input("Digite a quantidade de gasolina consumida (em litros): "))

            result_consumo = calc_consumo_medio(km, litros)

            print(f"O consumo médio do veículo é: {result_consumo:.3f} km/L")

        if opcao == "2":
            distancia_total = float(input("Digite a distância total da viagem (em km): "))
            consumo_medio = float(input("Digite o consumo médio do seu veículo (km/l): "))
            preco_combustivel = float(input("Digite o preço do combustível (R$): "))

            result_custo = calc_custo_combustivel(distancia_total, consumo_medio, preco_combustivel)
            print(f"Custo estimado da viagem: R$ {result_custo:.2f}")

        if opcao == "3":
            capacidade_tanque = float(input("Qual é a capacidade total do tanque do seu carro (em litros)? "))
            consumo_medio = float(input("Qual o consumo médio do seu carro (km/l)? "))

            result_autonomia = calc_autonomia(capacidade_tanque, consumo_medio)
            print(f'A autonomia total do seu veículo é de: {result_autonomia} km')

        if opcao == "4":
            distancia_total = float(input("Digite a distância total da viagem (em km): "))
            autonomia_total = float(input("Digite a autonomia total do veículo (em km): "))

            result_paradas = calc_paradas(distancia_total, autonomia_total)
            print(f'Quantidade de paradas necessárias: {result_paradas}')

        if opcao == "5":
            tanque1 = float(input("Qual é a capacidade total do tanque do primeiro veículo (em litros)? "))
            consumo1 = float(input("Qual o consumo médio do primeiro veículo (km/l)? "))
            tanque2 = float(input("Qual é a capacidade total do tanque do segundo veículo (em litros)? "))
            consumo2 = float(input("Qual o consumo médio do segundo veículo (km/l)? "))

            vencedor, diferenca = comparar_veiculos(tanque1, consumo1, tanque2, consumo2)
            print(f"O melhor é o {vencedor} por uma diferença de {diferenca} km!")

        if opcao == "6":
            distancia_total = float(input("Digite a distância total da viagem (em km): "))
            consumo_medio = float(input("Digite o consumo médio do seu veículo (km/l): "))
            preco_combustivel = float(input("Digite o preço do combustível (R$): "))
            orcamento = float(input("Digite o valor do seu orçamento (R$): "))

            custo_viagem = calc_custo_combustivel(distancia_total, consumo_medio, preco_combustivel)
            if avaliar_orcamento(custo_viagem, orcamento):
                print(f"O custo estimado da viagem é de R$ {custo_viagem:.2f}, que está dentro do seu orçamento.")
            else:
                print(f"O custo estimado da viagem é de R$ {custo_viagem:.2f}, que excede o seu orçamento.")

        if opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

