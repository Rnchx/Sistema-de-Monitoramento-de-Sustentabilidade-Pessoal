# Monitoramento de Sustentabilidade Pessoal

Este programa tem como objetivo monitorar a sustentabilidade pessoal com base em quatro parâmetros: consumo de água, consumo de energia elétrica, quantidade de resíduos não recicláveis gerados e tipo de transporte utilizado. O usuário insere informações sobre essas variáveis, e o programa fornece uma avaliação do impacto ambiental de suas ações diárias, categorizando-as em diferentes níveis de sustentabilidade.

## Funcionalidades

1. *Consumo de Água*: O programa solicita o número de litros de água consumidos no dia e classifica o consumo em alta, moderada ou baixa sustentabilidade.
2. *Consumo de Energia*: O programa solicita o número de kWh de energia elétrica consumidos no dia e classifica o consumo em alta, moderada ou baixa sustentabilidade.
3. *Resíduos Não Recicláveis*: O programa solicita a quantidade de resíduos não recicláveis gerados no dia e calcula o impacto com base na porcentagem de resíduos reciclados em relação ao total.
4. *Meio de Transporte*: O programa solicita o meio de transporte utilizado no dia e classifica sua sustentabilidade de acordo com o tipo de transporte.


## Como Executar

1. *Instale o Python*:
   - Este programa foi desenvolvido em Python. Se você não tiver o Python instalado, pode baixá-lo e instalá-lo em [python.org](https://www.python.org/).

2. *Execute o Código*:
   - Abra um terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo Python (programa_sustentabilidade.py) está salvo.
   - Execute o programa com o comando:
     bash
     python programa_sustentabilidade.py


     ## Como Funciona

### 1. Solicitação de Data:
O programa solicita que o usuário insira a data no formato *DD/MM/AAAA*. Caso o formato seja incorreto, o programa pedirá para tentar novamente até que uma data válida seja informada.

### 2. Consumo de Água:
O programa solicita a quantidade de água consumida no dia (em litros). Com base no valor inserido, o programa classifica o consumo como:
- *🟢 Alta sustentabilidade*: Menos de 150 litros.
- *🟡 Moderada sustentabilidade*: Entre 150 e 200 litros.
- *🔴 Baixa sustentabilidade*: Acima de 200 litros.

### 3. Consumo de Energia:
O programa solicita o consumo de energia elétrica em *kWh* e classifica da seguinte forma:
- *🟢 Alta sustentabilidade*: Menos de 5 kWh.
- *🟡 Moderada sustentabilidade*: Entre 5 e 10 kWh.
- *🔴 Baixa sustentabilidade*: Acima de 10 kWh.

### 4. Resíduos Não Recicláveis:
O programa solicita a quantidade de resíduos não recicláveis gerados (em kg) e também solicita a porcentagem de resíduos reciclados no total. Com base nisso, a classificação de sustentabilidade será:
- *🟢 Alta sustentabilidade*: Mais de 50% de resíduos reciclados.
- *🟡 Moderada sustentabilidade*: Entre 20% e 50% de resíduos reciclados.
- *🔴 Baixa sustentabilidade*: Menos de 20% de resíduos reciclados.

### 5. Meio de Transporte:
O programa apresenta uma lista de opções de transporte para o usuário escolher:
- *1. Transporte público (ônibus, metrô, trem)* → *🟢 Alta sustentabilidade*
- *2. Bicicleta* → *🟢 Alta sustentabilidade*
- *3. Caminhada* → *🟢 Alta sustentabilidade*
- *4. Carro (combustível fóssil)* → *🔴 Baixa sustentabilidade*
- *5. Carro elétrico* → *🟡 Moderada sustentabilidade*
- *6. Carona compartilhada* → *🟡 Moderada sustentabilidade*

## Exemplo de Execução

```bash
Programa para monitoramento de sustentabilidade pessoal
Qual a data de hoje? (formato DD/MM/AAAA) 28/03/2025
Quantos litros de água você consumiu hoje? 'aproximadamente' 120
Quantos kWh de energia elétrica você consumiu hoje? 'aproximadamente' 8
Quantos kg de resíduos não recicláveis você gerou hoje? 'aproximadamente' 0.5
Qual a porcentagem de resíduos reciclados no total? (em %) 30
Qual o meio de transporte você usou hoje?
1. Transporte público (ônibus, metrô, trem).
2. Bicicleta.
3. Caminhada.
4. Carro (combustível fósseis).
5. Carro elétrico.
6. Carona compartilhada.
Escolha uma opção (1-6): 3

Quadro de monitoramento de sustentabilidade pessoal:

1. seu consumo de água está em 🟢 Alta sustentabilidade
2. seu consumo de energia está em 🟡 Moderada sustentabilidade
3. sua reciclagem está classficada como 🟡 Moderada sustentabilidade
4. o transporte que você utilizou hoje está classificado como 🟢 Alta sustentabilidade
     