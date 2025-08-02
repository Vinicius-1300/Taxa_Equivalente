def taxa_equivalente(ip, n):      #Formula da taxa equivalente
    taxa_periodo = (1 + (ip / 100)) ** n  
    ia = (taxa_periodo - 1) * 100
    return ia

def validacao(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO, por favor digite um tempo de forma correta')
        else:
            return num

periodos = {'1 - Anual': 12, '2 - Semestre': 6, '3 - Trimestre': 3}

print('=' * 10 + ' |TAXA EQUIVALENTE| ' + 10 * '=')
print(periodos)
taxa_desejada = validacao('Taxa desejada R: ')
tempo_dec = validacao('Qual o tempo desejado? (Digite 1, 2 ou 3) R: ')
match tempo_dec:
    case 1:
        tempo_dec = 12
    case 2:
        tempo_dec = 6
    case 3:
        tempo_dec = 3
result = taxa_equivalente(taxa_desejada, tempo_dec)
print(f'O resultado da operação será: {result:.2f}%')

'''
ia: taxa anual
ip: taxa período
n: tempo decorrido
'''