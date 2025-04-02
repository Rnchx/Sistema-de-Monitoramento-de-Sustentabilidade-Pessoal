from datetime import datetime

print("Programa para monitoramento de sustentabilidade pessoal")

# Validar a data
while True:
    todayDate = input("Qual a data de hoje? (formato DD/MM/AAAA) ")
    
    try:
        todayDate = todayDate.strip()
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
        AmountOfWaterConsumed = float(input("Quantos litros de água você consumiu hoje? 'aproximadamente' "))

        if AmountOfWaterConsumed < 0:
            print("Erro: O consumo de água não pode ser negativo!")
            continue

        if AmountOfWaterConsumed < 150:
            waterConsumption = '🟢 Alta sustentabilidade'
        elif AmountOfWaterConsumed >= 150 and AmountOfWaterConsumed <= 200:
            waterConsumption = '🟡 Moderada sustentabilidade'
        else:
            waterConsumption = '🔴 Baixa sustentabilidade'

        break
    except ValueError:
        print("Digite apenas números para dizer os litros usados!!")

# Validar consumo de energia
while True:
    try:
        AmountOfEnergyConsumed = float(input("Quantos kWh de energia elétrica você consumiu hoje? 'aproximadamente' "))

        if AmountOfEnergyConsumed < 0:
            print("Erro: O consumo de energia não pode ser negativo!")
            continue

        if AmountOfEnergyConsumed < 5:
            energyConsumption = '🟢 Alta sustentabilidade'
        elif AmountOfEnergyConsumed >= 5 and AmountOfEnergyConsumed <= 10:
            energyConsumption = '🟡 Moderada sustentabilidade'
        else:
            energyConsumption = '🔴 Baixa sustentabilidade'

        break
    except ValueError:
        print("Digite apenas números para dizer os kWh de energia usados!!")

# Validar resíduos não recicláveis gerados
while True:
    try:
        AmountOfNonRecyclabeWasteGenerated = float(input("Quantos kg de resíduos não recicláveis você gerou hoje? 'aproximadamente' "))

        if AmountOfNonRecyclabeWasteGenerated < 0:
            print("Erro: O peso dos resíduos não recicláveis não pode ser negativo!")
            continue
        break
    except ValueError:
        print("Digite apenas números para dizer os Kgs de resíduos gerados!!")

# Validar a porcentagem de resíduos reciclados
while True:
    try:
        percentageOfRecycledWasteInTotal = float(input("Qual a porcentagem de resíduos reciclados no total? (em %) "))

        if percentageOfRecycledWasteInTotal < 0 or percentageOfRecycledWasteInTotal > 100:
            print("Erro: A porcentagem de resíduos reciclados deve ser entre 0% e 100%. Tente novamente.")
            continue

        if percentageOfRecycledWasteInTotal > 50:
            wasteClassification = '🟢 Alta sustentabilidade'
        elif percentageOfRecycledWasteInTotal >= 20 and percentageOfRecycledWasteInTotal <= 50:
            wasteClassification = '🟡 Moderada sustentabilidade'
        else:
            wasteClassification = '🔴 Baixa sustentabilidade'
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
        transportOption = int(input("Escolha uma opção (1-6): "))
        
        if transportOption < 1 or transportOption > 6:
            print("Digite uma opção de transporte que esteja dentro do parâmetro!!")
        else:
            if transportOption == 2 or transportOption == 3:
                transportClassification = '🟢 Alta sustentabilidade'
            elif transportOption == 5 or transportOption == 6:
                transportClassification = '🟡 Moderada sustentabilidade'
            else:
                transportClassification = '🔴 Baixa sustentabilidade'
            break
    except ValueError:
        print("Digite apenas números para dizer a opção de transporte utilizada!!")


print(f"""
Quadro de monitoramento de sustentabilidade pessoal:

1. Seu consumo de água está em {waterConsumption}

2. Seu consumo de energia está em {energyConsumption}

3. Sua reciclagem está classificada como {wasteClassification}

4. O transporte que você utilizou hoje está classificado como {transportClassification}
""")
