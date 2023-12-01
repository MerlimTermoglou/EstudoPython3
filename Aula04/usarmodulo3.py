# para importar apenas uma função dentro de 
# um módulo, usamos o comando from para indicar 
# o nome do módulo e o comando importa para
# usar apenas uma função. Você também pode
# aplicar um alias para a função importada
from colecao import soma as s

n = [4,12,8,5,18]
print(s(n))
