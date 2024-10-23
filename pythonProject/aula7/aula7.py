"""
F strings
"""


nome = 'Alan Henrique'
print(nome, type(nome))
idade = 30
altura = 1.83
e_maior = idade > 18
peso = 143
imc = peso/(altura * altura)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('E maior:', e_maior)

print(idade * altura)
print(nome, ' tem ', idade, ' anos de idade e seu IMC e de:', imc)  ##sem F STRINGS
print(f'{nome} tem {idade} anos de idade e seu IMC e de {imc:.2f}') ##com F STRINGS, formatando casa decimais
print ('{} tem {} anos de idade e seu IMC e de {:.2f}'. format(nome, idade, imc)) # utilizando a funcao format, variaveis executadas em ordem
print ('{0} tem {2} anos de idade e seu IMC e de {2:.2f}'. format(nome, idade, imc)) # format com parametros numerados
print ('{n} tem {i} anos de idade e seu IMC e de {im:.2f}'. format(n=nome, i=idade, im=imc)) #format com parametros nomeados
