"""
* Criar variaveis para nome (str), idade (int),
* altura (float) e peso (float)
* Criar uma variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa
* Obter o IMC da pessoa com 2 casa decimais
* Exibir um texto com todos os valores na tela usando F-Strings (Com as chaves)
"""

nome = 'Alan'
idade = 30
altura = 1.83
peso = 143
current_year = 2024
imc = peso / (altura * altura)

print('O nome da pessoa e {n}, a idade e {i} anos, com {a}cm de altura, e {p} kg, o ano de nascimento e {ci} e o imc e {im:.2f}'.format(n=nome, i= idade, a=altura, p= peso, ci=current_year -idade, im=imc ))