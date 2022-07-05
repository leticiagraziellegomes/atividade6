QuantidadeItens = float(input("quantidade de itens:"))
total = 0
Itens = []

i = 0
while i < QuantidadeItens:
     nomeItem = input("nome do item " + str(i+1) + ": ")
     quantidadeItem = float(input("quantidade de item " + str(i+1) + ": "))
     valorItem = float(input("valor desse produto: "))
     ValorTotalItens = float(quantidadeItem * valorItem)
     total += ValorTotalItens
     listaItens = {
         "nome": nomeItem,
         "quantidade": quantidadeItem,
         "valor": ValorTotalItens
     }
     Itens.append(listaItens)
     i += 1

print("=====================")
print("Recibo:")
print("Quantidade   |   Nome   |   Valor")

for item in Itens:
    print("{} | {} | R${}".format(item["quantidade"], item["nome"], item["valor"]))
    
print("")
print("total:R$" + str(total))
print("=====================")


