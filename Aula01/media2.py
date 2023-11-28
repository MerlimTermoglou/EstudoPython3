nota = input ("Digite a nota do aluno: ")

nota = float(nota)
  
if nota >= 6:
    print("Aprovado")
elif nota <= 4:
    print("Reprovado") 
else:
    print("Recuperação")       
    
    recu = input("Digite a nota do trabalho de recuperação: ")
    recu = float(recu)
    if recu >= 6:
       print("Aprovado")
    else:
       print("Reprovado") 



