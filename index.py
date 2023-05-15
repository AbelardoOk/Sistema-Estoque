import pandas as pd


# Adicionar produto
def addProduto(df):

    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$"))
    quant = int(input("Quantidade de produtos: "))

    novoProd = {'Nome': nome, 'Preco': preco, 'Quantidade': quant}
    df = df._append(novoProd, ignore_index=True)

    print(" ")
    return df


# Remover produto
def remProduto(df):

    nome = input("Nome do produto a ser removido: ")

    if nome in df['Nome'].values:
        df = df[df['Nome'] != nome]
        print("Produto removido com sucesso")

    else:
        print("Produto não encontrado.")

    print(" ")
    return df


# Verificar estoque
def verProduto(df):
    nome = input("Nome do produto: ")

    if nome in df['Nome'].values:
        quantidade = df.loc[df['Nome'] == nome, 'Quantidade'].values[0]
        print("Há {} unidades de {} no estoque".format( quantidade , nome ))

    else:
        print("Produto não encontrado.")
    
    print(" ")


# Relatório do estoque
def gerarRelatorio(df, limiar):

    prod = df[df['Quantidade'] < limiar]

    if prod.empty:
        print("Não há produtos em baixa estoque")
    else:
        print("Produtos em baixa:")
        print(prod.to_string(index=False))

    print(" ")
    return df


# Configuração da DataFrame
df = pd.DataFrame(columns=['Nome','Preco','Quantidade'])

df = addProduto(df)
print(df.to_string(index=False), '\n')

df = gerarRelatorio(df, 5)


# Imprimir dataFrame final
if not df.empty:
    print("Produtos em estoque:")
    print(df.to_string(index=False))

else:
    print("Não há produtos em estoque")