from datetime import datetime

print("Programa para monitoramento de sustentabilidade pessoal")

while True:
    todayDate = input("Qual a data de hoje? (formato DD/MM/AAAA) ")
    
    try:
        formatedDate = datetime.strptime(todayDate, "%d/%m/%Y").date()
        break
    except ValueError:
        print("Formato de data inválido! Use DD/MM/AAAA.")

while True:
    try:
        AmountOfWaterConsumed = float(input("Quantos litros de água você consumiu hoje? 'aproximadamente' "))

        if AmountOfWaterConsumed < 150:
            waterConsumption = '🟢 Alta sustentabilidade'
        elif AmountOfWaterConsumed >= 150 and AmountOfWaterConsumed <= 200:
            waterConsumption = '🟡 Moderada sustentabilidade'
        else:
            waterConsumption = '🔴 Baixa sustentabilidade'

        break
    except ValueError:
        print("Digite apenas números para dizer os litros usados!!")

while True:
    try:
        AmountOfEnergyConsumed = float(input("Quantos kWh de energia elétrica você consumiu hoje? 'aproximadamente' "))

        if AmountOfEnergyConsumed < 5:
            energyConsumption = '🟢 Alta sustentabilidade'
        elif AmountOfEnergyConsumed >= 5 and AmountOfEnergyConsumed <= 10:
            energyConsumption = '🟡 Moderada sustentabilidade'
        else:
            energyConsumption = '🔴 Baixa sustentabilidade'

        break
    except ValueError:
        print("Digite apenas números para dizer os kWh de energia usados!!")

while True:
    try:
        AmountOfNonRecyclabeWasteGenerated = float(input("Quantos kg de resíduos não recicláveis você gerou hoje? 'aproximadamente' "))
        break
    except ValueError:
        print("Digite apenas números para dizer os Kgs de resíduos gerados!!")

while True:
    try:
        percentageOfRecycledWasteInTotal = float(input("Qual a porcentagem de resíduos reciclados no total? (em %) "))

        if percentageOfRecycledWasteInTotal > 50:
            wasteClassification = '🟢 Alta sustentabilidade'
        elif percentageOfRecycledWasteInTotal >= 20 and percentageOfRecycledWasteInTotal <= 50:
            wasteClassification = '🟡 Moderada sustentabilidade'
        else:
            wasteClassification = '🔴 Baixa sustentabilidade'
        break
    except ValueError:
        print("Digite apenas números para dizer a porcentagem de resíduos reciclados no total!!")

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

1. seu consumo de água está em {waterConsumption}

2. seu consumo de energia está em {energyConsumption}

3. sua reciclagem está classficada como {wasteClassification}

4. o transporte que você utilizou hoje está classificado como {transportClassification}
""")
