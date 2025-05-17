from datetime import datetime
import mysql.connector

print("Programa para monitoramento de sustentabilidade pessoal")

# Conexão com o banco de dados MySQL

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="6807",
#     database="sustentabilidade"
# )
# cursor = conn.cursor()

# conexão com o banco de dados MYSQL -- TESTE

conn = mysql.connector.connect(
    host="172.16.12.14",
    user="BD240225246",
    password="Gcgts5",
    database="BD240225246"
)
cursor = conn.cursor()

# Nome do usuário
while True:
    try:
        nome = input("Digite seu nome: ").strip()
    except ValueError:
        print("Por favor digite apenas valores válidos!")
    if nome == '':
        print("Por favor digite algo no campo de inserir o nome!")   
    else:
        break


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
        AmountOfWaterConsumed = float(input("Quantos litros de água você consumiu hoje? "))

        if AmountOfWaterConsumed < 0:
            print("O consumo de água não pode ser negativo!")

        if AmountOfWaterConsumed > 3000:
            print("Digite um valor que seja coerente/verdadeiro de consumo de água!")

        if AmountOfWaterConsumed < 150:
            waterConsumption = '🟢 Alta sustentabilidade'
        elif AmountOfWaterConsumed <= 200:
            waterConsumption = '🟡 Moderada sustentabilidade'
        else:
            waterConsumption = '🔴 Baixa sustentabilidade'

        break
        
    except ValueError:    
        print("Digite valores que correspondam a quantidade de litros de água consumidos no seu dia!")

# Validar consumo de energia
while True:
    try:
        AmountOfEnergyConsumed = float(input("Quantos kWh de energia elétrica você consumiu hoje? "))
        if AmountOfEnergyConsumed < 0:
            print("Erro: O consumo de energia não pode ser negativo!")

        if AmountOfEnergyConsumed < 50:
            energyConsumption = '🟢 Alta sustentabilidade'
        elif AmountOfEnergyConsumed <= 100:
            energyConsumption = '🟡 Moderada sustentabilidade'
        else:
            energyConsumption = '🔴 Baixa sustentabilidade'

        break
    except ValueError:
        print("Digite valores que correspondam a quantidade de energia consumidos no seu dia!")

# Validar resíduos não recicláveis
while True:
    try:
        AmountOfNonRecyclabeWasteGenerated = float(input("Quantos kg de resíduos não recicláveis você gerou hoje? "))
        if AmountOfNonRecyclabeWasteGenerated < 0:
            print("Erro: O peso dos resíduos não pode ser negativo!")
            continue
        break
    except ValueError:
        print("Digite valores que correspondam a quantidade de kgs de resíduos não recicláveis gerados no seu dia!")

# Validar porcentagem reciclada
while True:
    try:
        percentageOfRecycledWasteInTotal = float(input("Qual a porcentagem de resíduos reciclados no total? "))
        if percentageOfRecycledWasteInTotal < 0 or percentageOfRecycledWasteInTotal > 100:
            print("Erro: A porcentagem deve estar entre 0 e 100.")
            continue

        if percentageOfRecycledWasteInTotal > 50:
            wasteClassification = '🟢 Alta sustentabilidade'
        elif percentageOfRecycledWasteInTotal >= 20:
            wasteClassification = '🟡 Moderada sustentabilidade'
        else:
            wasteClassification = '🔴 Baixa sustentabilidade'

        break
    except ValueError:
        print("Digite valores que correspondam a porcentagem de resíduos recicláveis no total gerados no seu dia!")

# Escolha do meio de transporte
print("""
Qual o meio de transporte você usou hoje?
1. Transporte público (ônibus, metrô, trem)
2. Bicicleta
3. Caminhada
4. Carro (combustível fóssil)
5. Carro elétrico
6. Carona compartilhada
""")

while True:
    try:
        transportOption = int(input("Escolha uma opção (1-6): "))
        if transportOption not in range(1, 7):
            print("Digite uma opção válida de 1 a 6.")
            continue

        if transportOption in [2, 3]:
            transportClassification = '🟢 Alta sustentabilidade'
        elif transportOption in [5, 6]:
            transportClassification = '🟡 Moderada sustentabilidade'
        else:
            transportClassification = '🔴 Baixa sustentabilidade'

        transportOptionsDict = {
            1: "Transporte público",
            2: "Bicicleta",
            3: "Caminhada",
            4: "Carro (combustível fóssil)",
            5: "Carro elétrico",
            6: "Carona compartilhada"
        }
        transporte = transportOptionsDict[transportOption]

        break
    except ValueError:
        print("Digite apenas números!")

# Mostrar resumo final
print(f"""
Quadro de monitoramento de sustentabilidade pessoal:

1. Seu consumo de água está em {waterConsumption}
2. Seu consumo de energia está em {energyConsumption}
3. Sua reciclagem está classificada como {wasteClassification}
4. O transporte que você utilizou hoje está classificado como {transportClassification}
""")

# Inserir dados no banco de dados
insert_query = """
INSERT INTO sustentabilidade_pessoal (
    data_registro,
    nome,
    consumo_agua,
    consumo_energia,
    residuos_nao_reciclaveis,
    percentual_reciclados,
    transporte
) VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

data = (
    formatedDate,
    nome,
    AmountOfWaterConsumed,
    AmountOfEnergyConsumed,
    AmountOfNonRecyclabeWasteGenerated,
    percentageOfRecycledWasteInTotal,
    transporte
)

cursor.execute(insert_query, data)
conn.commit()

print("✅ Dados inseridos com sucesso no banco de dados!")

# Fechar conexão
cursor.close()
conn.close()
