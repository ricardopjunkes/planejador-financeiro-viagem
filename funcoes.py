#Função calcular_consumo_medio()
def calc_consumo_medio(km, litros):
    consumo_medio = km / litros
    return consumo_medio



#Função calcular_custo_combustivel()
def calc_custo_combustivel(distancia_total, calc_consumo_medio, preco_combustivel):
    litros_necessarios = distancia_total / calc_consumo_medio
    custo_total = litros_necessarios * preco_combustivel
    return custo_total



#Função calcular_autonomia()
def calc_autonomia(capacidade_tanque, consumo_medio):
    autonomia_total = capacidade_tanque * consumo_medio
    return autonomia_total



#Função calcular_paradas()
import math
def calc_paradas(distancia_total, autonomia_total):
  quantidade_paradas = math.ceil(distancia_total / autonomia_total)
  return quantidade_paradas


#Função comparar_veiculos()
def comparar_veiculos(tanque1, consumo1, tanque2, consumo2):
    auto1 = calc_autonomia(tanque1, consumo1)
    auto2 = calc_autonomia(tanque2, consumo2)
    
    diferenca_car1 = (auto1 - auto2)
    diferenca_car2 = (auto2 - auto1)
    if auto1 >= auto2:
        return "Carro 1", diferenca_car1
    else:
        return "Carro 2", diferenca_car2
    


#Função avaliar_orcamento()
def avaliar_orcamento(custo_viagem, orcamento):
    if orcamento >= custo_viagem:
        return True
    else:
        return False