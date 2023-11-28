#!/usr/bin/python3

nome = input("Digite o seu nome: ")
anoanas = input ("Digite o ano do seu nascimento: ")
#Para realizar o cálculo da idade, foi necessário converter
#a variável anonas paara inteiro, pois o comando input
#sempre retorna o valor como texto.
idade = 2023 - int(anoanas)
#para converter um valor númerico em texto, usamos o str
print("Olá sr(a). "+nome+" Você tem ou terá este ano: "+str(idade)+" anos")
