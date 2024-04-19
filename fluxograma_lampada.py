print('Lampada - Fluxograma')
lampada = input('Lâmpada (S)Plugada (N)Não Plugada: ')
if lampada == 'S':
    print('Lâmpada Plugada')
    bulbo = input('Bulbo Queimou (S)Sim (N)Não: ')
    if bulbo == 'S':
        print('Trocar o Bulbo.')
    else:
        print('Comprar nova Lâmpada')
else:
    print('Plugar a Lâmpada.')