from random import randint
from time import sleep
pc = randint(0, 5)
v1 = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(2)
if v1 == pc:
    print('Voce ganhou!')
else:
    print('Computador ganhou pensou no numero \033[1;34;44m{} e nao no numero \033[m{}'.format(pc, v1))