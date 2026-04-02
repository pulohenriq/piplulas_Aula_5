def verficarValore():
    anterior = float(input('Leitura 1: '))
    crescente = True
    
    for i in range(4):
        atual = float(input(f'Leitura {i+2}: '))
        if atual <= anterior:
            return False
        anterior = atual
    return True

#main  
if verficarValore():
    print('Crecentes')
else:
    print('Intável')