#Declaração da classe Cliente. Esta classe permite que sejam criados novos objetos do tipo cliente
class Cliente:
    #A impleentação do método __init__ representa a construção do método construtor da classe,
    # responsavel po inicializar o objeto que será criado. 

    #Este método possui um argumento self que faz referencia a propria classe. Quando for criar um metodo de classe a qual ele pertence.

    #Note que no método __init__(construtor) foram iniciados os atributos da classe, representando as cracterísticas do cliente,
    #todos eles foram criados usando o comando self, que indica que eles pertencem a classe Cliente, os atributos foram declarados como privados.
    #Para isso utilizamos 2 underscores.

    '''
    A classe Cliente gera novos clientes e pede alguns
    dados pessoais e é capaz de salvar o cliente
    '''

    def __init__(self):
        self.__nome = ""
        self.__idade = 0
        self.__genero = ""
        self.__email = ""

    #O método dados é utilizado pra realizar a passagem dos dados do cliente para dentro da classe Cliente.

    def dados(self,nome="",idade=0,genero="",email=""):

        '''
        O método dados pede algumas informações do cliente para ele
        seja salvo no sistema.
        '''

        self.__nome = nome
        self.__idade = idade
        self.__genero = genero
        self.__email = email

    #O método gravar exibir uma mensagem com o do cliente dznd q foi salvo com sucesso.

    def gravar(self):

        '''
        O método gravar exibe uma mensagem com o nome cliente e 
        gravação realizada com sucesso.
        '''

        print("O cliente "+self.__nome+" foi gravado com sucesso!")