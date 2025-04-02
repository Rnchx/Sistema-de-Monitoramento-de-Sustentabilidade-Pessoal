from datetime import datetime

# Função para garantir que a data tenha o formato DD/MM/AAAA
def formatar_data(data):
    data = data.replace(".", "/").replace("-", "/")  # Substituir outros delimitadores por "/"
    if len(data) == 8:  # Caso o usuário digite no formato sem as barras, ex: 01012025
        data = data[:2] + '/' + data[2:4] + '/' + data[4:]
    return data

print("Programa para monitoramento de sustentabilidade pessoal")

# Validar a data
while True:
    todayDate = input("Qual a data de hoje? (formato DD/MM/AAAA) ")
    
    try:
        todayDate = todayDate.strip()
        todayDate = formatar_data(todayDate)  # Formatar a data antes de validar
        formatedDate = datetime.strptime(todayDate, "%d/%m/%Y").date()
        if formatedDate != datetime.today().date():
            print("Erro: A data informada não corresponde à data atual!")
        else:
            break
    except ValueError:
        print("Formato de data inválido! Use DD/MM/AAAA.")

# Validar consumo de água
while True:
    try:
        QuantidadeDeAguaConsumida = float(input("Quantos litros de água você consumiu hoje? 'aproximadamente' "))

        if QuantidadeDeAguaConsumida < 0:
            print("Erro: O consumo de água não pode ser negativo!")
            continue
        if QuantidadeDeAguaConsumida < 150:
            consumoAgua = '🟢 Alta sustentabilidade'
        elif QuantidadeDeAguaConsumida >= 150 and QuantidadeDeAguaConsumida <= 200:
            consumoAgua = '🟡 Moderada sustentabilidade'
        else:
            consumoAgua = '🔴 Baixa sustentabilidade'
        break
    except ValueError:
        print("Digite apenas números para dizer os litros usados!!")

# Validar consumo de energia
while True:
    try:
        QuantidadeDeEnergiaConsumida = float(input("Quantos kWh de energia elétrica você consumiu hoje? 'aproximadamente' "))

        if QuantidadeDeEnergiaConsumida < 0:
            print("Erro: O consumo de energia não pode ser negativo!")
            continue

        if QuantidadeDeEnergiaConsumida < 5:
            consumoEnergia = '🟢 Alta sustentabilidade'
        elif QuantidadeDeEnergiaConsumida >= 5 and QuantidadeDeEnergiaConsumida <= 10:
            consumoEnergia = '🟡 Moderada sustentabilidade'
        else:
            consumoEnergia = '🔴 Baixa sustentabilidade'

        break
    except ValueError:
        print("Digite apenas números para dizer os kWh de energia usados!!")

# Validar resíduos não recicláveis gerados
while True:
    try:
        QuantidadeDeResiduosNaoReciclaveisGerados = float(input("Quantos kg de resíduos não recicláveis você gerou hoje? 'aproximadamente' "))

        if QuantidadeDeResiduosNaoReciclaveisGerados < 0:
            print("Erro: O peso dos resíduos não recicláveis não pode ser negativo!")
            continue
        break
    except ValueError:
        print("Digite apenas números para dizer os Kgs de resíduos gerados!!")

# Validar a porcentagem de resíduos reciclados
while True:
    try:
        percentageOfRecycledWasteInTotal = float(input("Qual a porcentagem de resíduos reciclados no total? (em %) "))

        if porcentagemDeResiduosRecicladosNoTotal < 0 or porcentagemDeResiduosRecicladosNoTotal > 100:
            print("Erro: A porcentagem de resíduos reciclados deve ser entre 0% e 100%. Tente novamente.")
            continue

        if porcentagemDeResiduosRecicladosNoTotal > 50:
            classificacaoGasto = '🟢 Alta sustentabilidade'
        elif porcentagemDeResiduosRecicladosNoTotal >= 20 and porcentagemDeResiduosRecicladosNoTotal <= 50:
            classificacaoGasto = '🟡 Moderada sustentabilidade'
        else:
            classificacaoGasto = '🔴 Baixa sustentabilidade'
        break
    except ValueError:
        print("Digite apenas números para dizer a porcentagem de resíduos reciclados no total!!")

# Escolha do meio de transporte
print(""" 
        Qual o meio de transporte você usou hoje? 
        1. Transporte público (ônibus, metrô, trem). 
        2. Bicicleta. 
        3. Caminhada. 
        4. Carro (combustível fósseis). 
        5. Carro elétrico. 
        6. Carona compartilhada.
      """)

while True:
    try:
        opcaoTransporte = int(input("Escolha uma opção (1-6): "))
        
        if opcaoTransporte < 1 or opcaoTransporte > 6:
            print("Digite uma opção de transporte que esteja dentro do parâmetro!!")
        else:
            if opcaoTransporte == 2 or opcaoTransporte == 3:
                classificacaoTransporte = '🟢 Alta sustentabilidade'
            elif opcaoTransporte == 5 or opcaoTransporte == 6:
                classificacaoTransporte = '🟡 Moderada sustentabilidade'
            else:
                classificacaoTransporte = '🔴 Baixa sustentabilidade'
            break
    except ValueError:
        print("Digite apenas números para dizer a opção de transporte utilizada!!")


print(f"""
Quadro de monitoramento de sustentabilidade pessoal:

1. Seu consumo de água está em {consumoAgua}

2. Seu consumo de energia está em {consumoEnergia}

3. Sua reciclagem está classificada como {classificacaoGasto}

4. O transporte que você utilizou hoje está classificado como {classificacaoTransporte}
""")
