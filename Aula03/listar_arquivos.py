import os 

os.system("cls")

lt = (os.listdir("c:/"))

ps =1

for i in lt:
    print(str(ps)+"º - "+i)
    ps+=1
    
esc = input("Digite o número correspondente a pasta que deseja ver: ")

match esc: 
    case "1":
        print(os.listdir("c:/$Recycle.Bin"))
    case "2":
        print(os.listdir("c:/$$WinREAgent"))
    case "3":
        print(os.listdir("c:/.GamingRoot"))
    case "4":
        print(os.listdir("c:/1AC6EEBC1791"))
    case "5":
        print(os.listdir("c:/Arquivos de Programas"))
    case "6":
        print(os.listdir("c:/Documents and Settings"))
    case "7":
        print(os.listdir("c:/DumpStack.log.tmp "))
    case "8":
        print(os.listdir("c:/eclipse"))
    case "9":
        print(os.listdir("c:/HashiCorp"))
    case "10":
        print(os.listdir("c:/hiberfil.sys"))
    case "11":
        print(os.listdir("c:/Intel"))
    case "12":
        print(os.listdir("c:/npm"))
    case _:
        print("Diretório não localizado")