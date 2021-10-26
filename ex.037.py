numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] - Binário
[ 2 ] - Octal
[ 3 ] - Hexadecimal''')
resp = int(input('Qual a opção desejada? '))

if resp == 1:
    print('{} em Binário será: {}'.format(numero, bin(numero)))
elif resp == 2:
    print('{} em Decimal será: {}'.format(numero, oct(numero)))
elif resp ==3:
    print('{} em Hexadecimal será: {}'.format(numero, hex(numero)))