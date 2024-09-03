#Listas 
lstCompras = []
sublstProdutos = []

print('\nLISTA DE COMPRAS!\n','-'*40)
print('Insira a seguir o PRODUTO, VALOR e MERCADO...\n','-'*40)

#Adicionando os valores a lista inicial.
while True: 
    #Solicitando para que o usuario insira os valores.
    valueProduto = input('Insira o PRODUTO, VALOR, MERCADO: ').split(',')
    lstCompras.append(valueProduto)

    #Se usuario desejar sair    
    saida = input('Deseja adicionar mais algo? (s/n) : ')

    if  'N' == saida.upper():
        break


'''
#Retirando VALOR da LISTA DE COMPRAS.
ret_valor = input('Deseja retirar algum valor da sua LISTA DE COMPRAS? (S/N) : ')
if 'S' == ret_valor.upper():
    qual_valor = input('Insira o produto que deseja retirar: ')
    lstCompras.remove(qual_valor)
    print('ITEM RETIRADO COM SUCESSO!')
    print(lstCompras)

elif 'N' == ret_valor.upper():
    print(lstCompras)
    '''

#Calculando valor final.

    #Ordenando os valores da LSTCOMPRAS
lstvalores = [float(valor[1]) for valor in lstCompras]
    
vf = 0
for preco in lstvalores:
    vf += preco
print(f'O valor final da compra é de: RS{vf}')