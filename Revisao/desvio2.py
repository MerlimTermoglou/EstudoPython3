#esse programa exibe uma mensagem para
#Os motoristas que estão com
#O seu veículo em dia de rodízio

final_placa = input("Digite o n° final da placa do seu carro: ")
if(final_placa == "1" or final_placa == "2"):
    print("Seu carro está no dia de rodizio - Segunda-Feira")
elif(final_placa == "3" or final_placa == "4"):
    print("Seu carro está no dia de rodizio - Terça-Feira")
elif(final_placa == "5" or final_placa == "6"):
    print("Seu carro está no dia de rodizio - Quarta-Feira")
elif(final_placa == "7" or final_placa == "8"):
    print("Seu carro está no dia de rodizio - Quinta-Feira")
elif(final_placa == "9" or final_placa == "0"):
    print("Seu carro está no dia de rodizio - Sexta-Feira")

else:
    print("Final de placa incorreto")