"""
CONSTANTE = "Variáveis que não vão mudar
Muitas condições no mesmo if (ruim)
    <-- contagem de complexidade ruim
"""

velocidade = 59
local_carro = 101

RADAR_1 = 61
LOCAL_1 = 100
RADAR_RANGE = 1

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')
if carro_passou_radar_1:
    print('Carro passou radar 1')
if carro_multado_radar_1:
    print('carro multado em radar 1')