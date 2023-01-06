import sys 
from sys import platform

# print(sys.platform) - verifica a plataforma

if sys.platform == 'windows':
    print('windows')
else:
    print('linux')
