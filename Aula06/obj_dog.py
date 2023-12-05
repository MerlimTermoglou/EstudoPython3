from classe_dog import Dog


# Para criar o objeto, utilizamos a variável golden e realizamos o 
# processo dde instanciação da classe Dog.
#foi passado o nome e a idade

golden = Dog("Luke",1)
# acessamos o método data_dog que mostra os dados do cachorro 
# 
golden.data_dog()
golden.sit()
golden.roll_over()
print(golden.__class__)
print(golden.__dict__)