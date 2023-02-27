import json

# 1. Ler os dados de faturamento diário a partir de um arquivo JSON
with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

# 2. Calcular o menor e o maior valor de faturamento diário no mês
menor_valor = min(faturamento)
maior_valor = max(faturamento)

# 3. Calcular a média mensal de faturamento, ignorando os dias sem faturamento
dias_com_faturamento = [valor for valor in faturamento if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# 4. Calcular o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

# Imprimir os resultados
print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias acima da média: {dias_acima_da_media}")
