from random import shuffle,sample
from time import sleep
jogadores = [] # onde os nomes dos jogadores ficaram
campeoes = ['Voli','Zac','Mundo','Sion','Chogat',
           'Vayne','Xayah','Jhin','Nilah','Samira',
           'Xinzao','Khazix','Lee','Jarvan','Noc'] # lista de campeôes LOL
for p in range(0,10):
    jogadores.append(str(input('Nome jogador:'))) 
print('*'*30)
shuffle(jogadores) # embaralhar os jogadores
champs = sample(campeoes,10) # embaralhar a lista de campeões
print('Sorteando os times')
sleep(1)
print('.')
sleep(1)
print('..')
print('TIME 1')
print(f'{jogadores[0]} com {champs[0]}.'
      f'\n{jogadores[1]} com {champs[1]}.'
      f'\n{jogadores[2]} com {champs[2]}.'
      f'\n{jogadores[3]} com {champs[3]}.'
      f'\n{jogadores[4]} com {champs[4]}.')
print()
print('TIME 2')
print()
print(f'{jogadores[5]} com {champs[5]}.'
      f'\n{jogadores[6]} com {champs[6]}.'
      f'\n{jogadores[7]} com {champs[7]}.'
      f'\n{jogadores[8]} com {champs[8]}.'
      f'\n{jogadores[9]} com {champs[9]}.')
