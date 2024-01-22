from class_cliente import Cliente

nome = input("Digite o NOME do cliente: ")
email = input("Digite o EMAIL do cliente: ")
cpf = input("Digite o CPF do cliente: ")
idade = input("Digite o IDADE do cliente: ")
telefone = input("Digite o TELEFONE do cliente: ")

#vamos instanciar a classe Cliente. Gerar um objt a partir da classe cliente passando
#as propriedades para o objeto criado

cli = Cliente()
cli.gravarCliente(nome,email,cpf,idade,telefone)