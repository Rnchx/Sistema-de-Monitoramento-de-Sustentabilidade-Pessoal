from datetime import datetime
import mysql.connector
import re

# Conexão correta com o banco de dados
def conectar():
    return mysql.connector.connect(
        host="172.16.12.14",
        user="BD240225246",
        password="Gcgts5",
        database="BD240225246"
    )

def classificar_agua(valor):
    if valor < 150:
        return '🟢 Alta sustentabilidade'
    elif valor <= 200:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

def classificar_energia(valor):
    if valor < 50:
        return '🟢 Alta sustentabilidade'
    elif valor <= 100:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

def classificar_residuos(valor):
    if valor > 50:
        return '🟢 Alta sustentabilidade'
    elif valor >= 20:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

def classificar_transporte(opcao):
    if opcao in [2, 3]:
        return '🟢 Alta sustentabilidade'
    elif opcao in [5, 6]:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

def inserir():
    conn = conectar()
    cursor = conn.cursor()

    padrao_de_nome = re.compile(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$')

    while True:
        usuario = input("Nome completo: ").strip()
        if not usuario:
            print("⚠️ Nome não pode ser vazio.")
            continue
        if padrao_de_nome.match(usuario):
            break
        else:
            print("⚠️ Nome inválido! Use apenas letras com iniciais maiúsculas (ex: João da Silva).")

    while True:
        try:
            data_input = input("Data do monitoramento (DD/MM/AAAA): ")
            hoje = datetime.strptime(data_input, "%d/%m/%Y").strftime('%Y-%m-%d')
            break
        except ValueError:
            print("⚠️ Data inválida! Use o formato DD/MM/AAAA.")

    while True:
        try:
            agua = float(input("Consumo de água (L): "))
            if agua < 0 or agua > 3000:
                print("⚠️ Valor de água incoerente.")
                continue
            break
        except ValueError:
            print("⚠️ Digite um valor numérico válido.")

    while True:
        try:
            energia = float(input("Consumo de energia (kWh): "))
            if energia < 0:
                print("⚠️ O consumo não pode ser negativo.")
                continue
            break
        except ValueError:
            print("⚠️ Digite um valor numérico válido.")

    while True:
        try:
            residuos = float(input("Resíduos não recicláveis (kg): "))
            if residuos < 0:
                print("⚠️ Valor não pode ser negativo.")
                continue
            break
        except ValueError:
            print("⚠️ Digite um valor numérico válido.")

    while True:
        try:
            reciclado = float(input("%  total de  resíduos reciclados: "))
            if not 0 <= reciclado <= 100:
                print("⚠️ Digite uma porcentagem válida (0 a 100).")
                continue
            break
        except ValueError:
            print("⚠️ Digite um valor numérico válido.")

    print("""
    Transporte:
    1. Transporte público
    2. Bicicleta
    3. Caminhada
    4. Carro (combustível fóssil)
    5. Carro elétrico
    6. Carona compartilhada
    """)

    while True:
        try:
            transporte_opcao = int(input("Escolha: "))
            if transporte_opcao not in range(1, 7):
                print("⚠️ Opção inválida.")
                continue
            break
        except ValueError:
            print("⚠️ Digite um número de 1 a 6.")

    transportes = {
        1: "Transporte público",
        2: "Bicicleta",
        3: "Caminhada",
        4: "Carro (combustível fóssil)",
        5: "Carro elétrico",
        6: "Carona compartilhada"
    }

    transporte = transportes.get(transporte_opcao, "Não informado")

    cursor.execute("""
        INSERT INTO sustentabilidade_pessoal (
            data_registro, nome, consumo_agua, consumo_energia,
            residuos_nao_reciclaveis, percentual_reciclados, transporte
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (hoje, usuario, agua, energia, residuos, reciclado, transporte))

    conn.commit()
    print("✅ Dados inseridos com sucesso!")
    cursor.close()
    conn.close()

def alterar():
    conn = conectar()
    cursor = conn.cursor()
    id_reg = input("ID do registro a alterar: ")
    cursor.execute("SELECT * FROM sustentabilidade_pessoal WHERE id = %s", (id_reg,))
    if cursor.fetchone():
        campo = input("Qual o campo que você deseja alterar: (nome, consumo_agua, consumo_energia, residuos_nao_reciclaveis, percentual_reciclados, transporte): ")
        novo_valor = input("Novo valor: ")
        try:
            cursor.execute(f"UPDATE sustentabilidade_pessoal SET {campo} = %s WHERE id = %s", (novo_valor, id_reg))
            conn.commit()
            print("✅ Registro alterado com sucesso!")
        except mysql.connector.Error as e:
            print(f"⚠️ Erro ao alterar registro: {e}")
    else:
        print("⚠️ Registro não encontrado para alteração.")
    cursor.close()
    conn.close()

def apagar():
    conn = conectar()
    cursor = conn.cursor()
    id_reg = input("ID do registro a excluir: ")
    cursor.execute("SELECT * FROM sustentabilidade_pessoal WHERE id = %s", (id_reg,))
    if cursor.fetchone():
        cursor.execute("DELETE FROM sustentabilidade_pessoal WHERE id = %s", (id_reg,))
        conn.commit()
        print("✅ Registro excluído com sucesso!")
    else:
        print("⚠️ Registro não encontrado para exclusão.")
    cursor.close()
    conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sustentabilidade_pessoal")
    registros = cursor.fetchall()
    if registros:
        colunas = [desc[0] for desc in cursor.description]
        print("\n" + " | ".join(colunas))
        print("-" * 80)
        for r in registros:
            print(" | ".join(str(c) for c in r))
    else:
        print("Nenhum monitoramento registrado.")
    cursor.close()
    conn.close()

def medias():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(consumo_agua), AVG(consumo_energia), AVG(residuos_nao_reciclaveis), AVG(percentual_reciclados) FROM sustentabilidade_pessoal")
    m = cursor.fetchone()
    if m and all(v is not None for v in m):
        print("\nMédias dos parâmetros:")
        print(f"Água: {m[0]:.2f} L - {classificar_agua(m[0])}")
        print(f"Energia: {m[1]:.2f} kWh - {classificar_energia(m[1])}")
        print(f"Resíduos: {m[2]:.2f} kg")
        print(f"Reciclado: {m[3]:.2f}% - {classificar_residuos(m[3])}")
    else:
        print("Não há dados suficientes para calcular as médias.")
    cursor.close()
    conn.close()

def menu():
    while True:
        print("""
======= MENU =======
1. Inserir dados
2. Alterar dados
3. Apagar dados
4. Listar monitoramentos
5. Médias e classificação
6. Sair
""")
        opc = input("Escolha: ")
        if opc == "1": inserir()
        elif opc == "2": alterar()
        elif opc == "3": apagar()
        elif opc == "4": listar()
        elif opc == "5": medias()
        elif opc == "6":
            print("Sistema encerrado. Até logo!")
            break
        else:
            print("⚠️ Opção inválida.")

menu()
