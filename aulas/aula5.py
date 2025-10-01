velocidade = 61
local_carro = 100

RADAR_1 = 60 #velocidade maxima
LOCAL_1 = 100 # onde esta o radar
RADAR_RANGE = 1 # ate range que pega o radar
radar_passou_1 = velocidade > RADAR_1
carro_multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
if radar_passou_1:
    print('Velocidade do Carro passou do radar 1')

if carro_multado_radar1:
    print('Carro passou do radar 1 ')

if carro_multado_radar1 \
      and radar_passou_1:
    print('O carro foi multado!')