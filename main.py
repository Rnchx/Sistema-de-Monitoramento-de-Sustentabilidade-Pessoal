import re
from datetime import datetime
import mysql.connector

# Conexão com Banco de Dados
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="6807",
        database="sustentabilidade"
    )

# Classificação de água
def classificar_agua(valor):
    if valor < 150:
        return '🟢 Alta sustentabilidade'
    elif valor <= 200:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de energia 
def classificar_energia(valor):
    if valor < 5:
        return '🟢 Alta sustentabilidade'
    elif valor <= 10:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de residuos
def classificar_residuos(valor):
    if valor > 50:
        return '🟢 Alta sustentabilidade'
    elif valor >= 20:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de reciclado
def classificar_reciclado(valor):
    if valor >= 80:
        return '🟢 Alta sustentabilidade'
    elif valor >= 50:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Classificação de transporte
def classificar_transporte(opcao):
    if opcao in [2, 3]:
        return '🟢 Alta sustentabilidade'
    elif opcao in [5, 6]:
        return '🟡 Moderada sustentabilidade'
    else:
        return '🔴 Baixa sustentabilidade'

# Inserção de dados
def inserir():
    conn = conectar()
    cursor = conn.cursor()

    import re

def inserir():
    conn = conectar()
    cursor = conn.cursor()

    while True:
        usuario = input("Nome: ").strip()
        if not usuario:
            print("❌ Nome não pode ser vazio.")
        elif not re.match(r"^[A-Za-zÀ-ÿ\s]+$", usuario):
            print("❌ Nome inválido. Use apenas letras e espaços, sem números.")
        else:
            break

    while True:
        try:
            data_input = input("Data do monitoramento (DD/MM/AAAA): ")
            hoje = datetime.strptime(data_input, "%d/%m/%Y").strftime('%Y-%m-%d')
            break
        except ValueError:
            print("❌ Data inválida! Use o formato DD/MM/AAAA.")

    while True:
        try:
            agua = float(input("Consumo de água (L): "))
            break
        except ValueError:
            print("❌ Digite um número válido para o consumo de água.")

    while True:
        try:
            energia = float(input("Consumo de energia (kWh): "))
            break
        except ValueError:
            print("❌ Digite um número válido para o consumo de energia.")

    while True:
        try:
            residuos = float(input("Resíduos não recicláveis (kg): "))
            break
        except ValueError:
            print("❌ Digite um número válido para resíduos.")

    while True:
        try:
            reciclado = float(input("% de reciclado: "))
            if 0 <= reciclado <= 100:
                break
            else:
                print("❌ Digite um valor entre 0 e 100 para o percentual.")
        except ValueError:
            print("❌ Digite um número válido para o percentual reciclado.")

    transportes = {
        1: "Transporte público",
        2: "Bicicleta",
        3: "Caminhada",
        4: "Carro (combustível fóssil)",
        5: "Carro elétrico",
        6: "Carona compartilhada"
    }

    while True:
        print("""
        Transporte:
        1. Transporte público
        2. Bicicleta
        3. Caminhada
        4. Carro (combustível fóssil)
        5. Carro elétrico
        6. Carona compartilhada
        """)
        try:
            transporte_opcao = int(input("Escolha: "))
            if transporte_opcao in transportes:
                transporte = transportes[transporte_opcao]
                break
            else:
                print("❌ Escolha uma opção de 1 a 6.")
        except ValueError:
            print("❌ Digite apenas números entre 1 e 6.")

    cursor.execute("""
        INSERT INTO sustentabilidade_pessoal (
            data_registro, usuario, consumo_agua, consumo_energia,
            residuos_nao_reciclaveis, percentual_reciclados, transporte
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (hoje, usuario, agua, energia, residuos, reciclado, transporte))

    conn.commit()
    print("✅ Dados inseridos com sucesso!")
    cursor.close()
    conn.close()

# Alteração de dados
def alterar():
    conn = conectar()
    cursor = conn.cursor()

    while True:
        id_reg = input("ID do registro a alterar: ")
        cursor.execute("SELECT * FROM sustentabilidade_pessoal WHERE id = %s", (id_reg,))
        registro = cursor.fetchone()
        if registro:
            break
        else:
            print("❌ ID não encontrado. Tente novamente.")

    campos_validos = ['consumo_agua', 'consumo_energia', 'residuos_nao_reciclaveis', 'percentual_reciclados', 'transporte']
    while True:
        campo = input(f"Campo a alterar {campos_validos}: ")
        if campo in campos_validos:
            break
        else:
            print("❌ Campo inválido.")

    while True:
        novo_valor = input("Novo valor: ")
        try:
            if campo != 'transporte':
                novo_valor = float(novo_valor)
            break
        except ValueError:
            print("❌ Digite um número válido para esse campo.")

    try:
        cursor.execute(f"UPDATE sustentabilidade_pessoal SET {campo} = %s WHERE id = %s", (novo_valor, id_reg))
        conn.commit()
        print("✅ Registro alterado com sucesso!")
    except mysql.connector.Error as e:
        print(f"❌ Erro ao alterar registro: {e}")

    cursor.close()
    conn.close()

# Exclusão de dados
def apagar():
    conn = conectar()
    cursor = conn.cursor()

    while True:
        id_reg = input("ID do registro a excluir: ")
        cursor.execute("SELECT * FROM sustentabilidade_pessoal WHERE id = %s", (id_reg,))
        registro = cursor.fetchone()
        if registro:
            print(f"Registro encontrado: {registro}")
            confirmar = input("Tem certeza que deseja excluir este registro? (s/n): ").lower()
            if confirmar == 's':
                cursor.execute("DELETE FROM sustentabilidade_pessoal WHERE id = %s", (id_reg,))
                conn.commit()
                print("✅ Registro excluído com sucesso!")
            else:
                print("❎ Exclusão cancelada.")
            break
        else:
            print("❌ ID não encontrado. Tente novamente.")

    cursor.close()
    conn.close()

# Listagem de dados
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

# Médias de dados
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
        print(f"Reciclado: {m[3]:.2f}% - {classificar_reciclado(m[3])}")

    else:
        print("Não há dados suficientes para calcular as médias.")
    cursor.close()
    conn.close()

# Menu de opções
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
            print("❌ Opção inválida. Escolha de 1 a 6.")

menu()