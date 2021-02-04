# Utilizando Módulos
# Formas de utilizar:
# 1 - import <nome da biblioteca>
# exemplo: import math
# 2 - from <nome da biblioteca> import <nome da função>
# exemplo: from math import sqrt
# exemplo: from math import sqrt, pow 

import math
import random
numero = random.randint(1, 100)
raiz = math.sqrt(numero)
print('A raiz de {} é aproximadamente {:.2f}'.format(numero, raiz))