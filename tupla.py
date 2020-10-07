tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

while True:
    numero = int(input('Digite um número entre 0 e 9: '))
    if 0 <= numero <= 9:
        print('O Numero {} está dentro da tupla.'.format(tupla[numero]))
        break
    else:
        print('O numero digitado está fora do intervalo permitido')
        continue
