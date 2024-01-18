#Este programa tem o nome do aluno e a nota media 
#Se o aluno tiver uma nota > ou = a 6 esta Aprovado
#Caso contrario Reprovado

nome = input("Digite o nome do Aluno: ")
media = input("Digite a nota média do aluno: ")
media = float (media)

if(media>=6):
    print("Aprovado")
else:
    print("Reprovado")