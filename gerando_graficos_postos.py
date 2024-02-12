import pandas as pd
import matplotlib.pyplot as plt

# Passo 1: Carregar os dados
data = pd.read_csv('arquivo.csv')

# Passo 2: Limpeza
data[['DATA INICIAL', 'DATA FINAL']] = data[['DATA INICIAL', 'DATA FINAL']].apply(pd.to_datetime)

atributos_limpar = ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO',
                    'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']

# Converter atributos para numérico e remover linhas com valores nulos
data[atributos_limpar] = data[atributos_limpar].apply(pd.to_numeric, errors='coerce')


def plotar_grafico_por_ano(data, estados, ano):
    # Plotar gráfico de linha para cada estado no ano específico
    plt.figure(figsize=(10, 6))
    for estado in estados:
        grupo = data.query('PRODUTO == "GASOLINA COMUM" and ESTADO == @estado and `DATA INICIAL`.dt.year == @ano')
        plt.plot(grupo['DATA INICIAL'], grupo['PREÇO MÉDIO REVENDA'], label=estado)

    # Configurações do gráfico
    plt.title(f'Comparação de Preço Médio de Revenda em {ano}')
    plt.xlabel('Data')
    plt.ylabel('Preço Médio de Revenda (R$/L)')
    plt.legend()
    plt.grid(True)
    plt.show()


def plotar_grafico_todos_periodos(data, estados):
    # Plotar gráfico de linha para cada estado em todos os períodos
    plt.figure(figsize=(10, 6))
    for estado in estados:
        grupo = data.query('PRODUTO == "GASOLINA COMUM" and ESTADO == @estado')
        plt.plot(grupo['DATA INICIAL'], grupo['PREÇO MÉDIO REVENDA'], label=estado)

    # Configurações do gráfico
    plt.title('Comparação de Preço Médio de Revenda em Todos os Períodos')
    plt.xlabel('Data')
    plt.ylabel('Preço Médio de Revenda (R$/L)')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    estados = []  # Lista de nomes que vão ser individuais ou coletivos

    while True:
        ano = int(input('Informe o ano de 2004 até 2022 ou digite 0 para pegar todos os períodos: '))

        if ano == 0:
            estados_input = input('Informe o nome do(s) estado(s), separados por vírgula: ').upper()

            # Separar os estados fornecidos pelo usuário
            estados_fornecidos = [estado.strip() for estado in estados_input.split(',')]

            # Verificar se todos os estados fornecidos estão na lista de estados disponíveis
            estados_nao_encontrados = [estado for estado in estados_fornecidos if estado not in data['ESTADO'].values]

            if estados_nao_encontrados:
                print(f"Os seguintes estados não foram encontrados: {', '.join(estados_nao_encontrados)}")
                continue

            estados.extend(estados_fornecidos)
            print("Estados adicionados:", estados)

            plotar_grafico_todos_periodos(data, estados)
            break

        elif 2004 <= ano <= 2022:
            estados_input = input('Informe o nome do(s) estado(s), separados por vírgula: ').upper()

            # Separar os estados fornecidos pelo usuário
            estados_fornecidos = [estado.strip() for estado in estados_input.split(',')]

            # Verificar se todos os estados fornecidos estão na lista de estados disponíveis
            estados_nao_encontrados = [estado for estado in estados_fornecidos if estado not in data['ESTADO'].values]

            if estados_nao_encontrados:
                print(f"Os seguintes estados não foram encontrados: {', '.join(estados_nao_encontrados)}")
                continue

            estados.extend(estados_fornecidos)
            print("Estados adicionados:", estados)

            plotar_grafico_por_ano(data, estados, ano)
            break

        else:
            print('Somente valores entre 2004 até 2022 serão permitidos')
            continue


if __name__ == '__main__':
    main()