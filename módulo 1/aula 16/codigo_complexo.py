'''
CONSTANTE_1 -> Constantes não devem ser mudadas;
Evistar muitas condições dentro do IF;
Evitar muitas identações -> margens a squerda demais é "feio"
'''

velocidade_carro = 60
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

#if velocidade_carro > RADAR_1:
#  print('Velocidade ultrapassada!')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE) and \
   velocidade_carro > RADAR_1:
    print('Velocidade ultrapassada!')
