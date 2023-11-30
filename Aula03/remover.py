import os

os.system("cls")
print(" Temos dois arquivos: bloco_texto.txt e uvinha.txt ")
print("Qual deles você deseja apagar?")
es = input("Digite: \n - 1 para bloco_texto\n - 2 para uvinha:\n")

if es == "1":
    os.remove("bloco_texto.txt")
else:
    os.remove("uvinha.txt")
print("O arquivo foi apagado com sucesso!")        