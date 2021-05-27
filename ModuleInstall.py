import os

with open('Modulos_instalar.txt', 'r') as file:
    for linea in file:
        linea =  linea.replace('\n', '').strip()
        try:
            os.system(f'pip install {linea}')
        except:
            print('No se pudo instalar el modulo: ', linea)

