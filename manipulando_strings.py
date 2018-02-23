teste = "Isto é uma string"
print("Vamos ver qual o tamanho da String " + '"' + teste + '"')
print(len(teste))
print("")

print('Vamos trocar o "Isto" por "Isto aqui" usando o método replace')
teste = teste.replace('Isto','Isto aqui')
print(teste)
print("")

print('Vamos testar quantas vezes a letra "s" aparece na String ' + '"' + teste + '"')
print(teste.count('s'))
print("")

print('Vamos achar a posição da letra "q" na String')
print(teste.find('q'))
print("")

print("Vamos utilizar o split")
print(teste.split())
print("")

print("Para juntar nossa string separada, podemos usar o método join.")
print('é muito'.join(teste.split('é')))
print("")

print("Vamos deixar tudo maiúsculo")
print(teste.upper())
print("")

print("Vamos deixar tudo minúsculo")
print(teste.lower())
print("")

print("Vamos deixar apenas a primeira letra maiúscula de uma string minúscula")
print(teste.capitalize())
print("")

print("Método title, que deixa as letras de cada palavra da string maiúscula")
print(teste.title())
print("")

print("Uma troca também é possível.O que for maiúsculo vira minúsculo e vice-versa")
print(teste.swapcase())
print("")

print('Podemos rodar alguns testes numa string usando poucos métodos. Vamos ver se a string dada é totalmente maiúscula com o método "isupper()"')
print(teste.isupper())
print("")

print('Podemos checar se a string dada é minúscula com o método "islower()"')
print(teste.islower())
print("")

print('Checando se ela é um title com o método "istitle()", no caso, todas as palavras com a primeira letra maiúscula')
print(teste.istitle())
print("")

print('Podemos checar se a string é alfa-numérica com o método "isalnum()", ou seja, contém apenas letras e números, sem caracteres especiais')
print(teste.isalnum())
print("")

print('É possível checar se uma string contém apenas letras com o método "isalpha"')
print(teste.isalpha())
print("")

print('Agora checando se ela contém apenas números com o método "isdigit()"')
print(teste.isdigit())
print("")

print('Para mais informações http://wiki.python.org.br/ManipulandoStringsComPython')
