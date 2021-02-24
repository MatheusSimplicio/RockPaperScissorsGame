from time import sleep
import random
print('\033[1m{:=^100}\033[m'.format('\033[1;3;4;34mVamos Jogar Pedra, Papel e Tesoura?\033[m'))
sleep(1)
print('Se você não sabe as regras, elas são bem simples:'
      '\nVocê deve escolher entre pedra papel e tesoura, para tentar vencer a minha escolha.'
      '\n\033[1;3;33mLembre-se que:\033[m'
      '\n\033[30mPedra\033[m \033[1;31mperde\033[m para o papel e \033[1;32mganha\033[m da tesoura;'
      '\n\033[30mPapel\033[m \033[1;31mperde\033[m para a tesoura e \033[1;32mganha\033[m da pedra;'
      '\n\033[30mTesoura\033[m \033[1;31mperde\033[m para a pedra e \033[1;32mganha\033[m do papel')
print('\033[1m=\033[m'*87)
opcoespc = ['PEDRA', 'PAPEL', 'TESOURA']  # Opções de jogada do computador
escolhapc = random.choice(opcoespc)  # Faz o computador escolher um item da lista opcoespc
escolhajogador = str(input('Faça a sua escolha:')).strip().upper()
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOURA')
print(f'\033[1;3;4;32;40mVocê escolheu {escolhajogador}.\033[m')
print(f'\033[1;3;4;31;40mEu escolhi {escolhapc}\033[m')
if escolhajogador == escolhapc:
    print('\033[1;;33mNós empatamos!\033[m Que tal mais uma partida...para eu poder te derrotar! ;) ')
elif escolhajogador == 'PEDRA' and escolhapc == 'PAPEL':
    print('\033[1;31mVOCÊ PERDEU!\033[m Eu sabia que iria te vencer!')
elif escolhajogador == 'PAPEL' and escolhapc == 'PEDRA':
    print('\033[1;32mVOCÊ ME VENCEU!\033[m Bem, eu não esperava por isso...quer jogar mais uma vez?')
elif escolhajogador == 'PEDRA' and escolhapc == 'TESOURA':
    print('VOCÊ ME VENCEU! Bem, eu não esperava por isso...quer jogar mais uma vez?')
elif escolhajogador == 'PAPEL' and escolhapc == 'TESOURA':
    print('\033[1;31mVOCÊ PERDEU!\033[m Eu sabia que iria te vencer!')
elif escolhajogador == 'TESOURA' and escolhapc == 'PAPEL':
    print('\033[1;32mVOCÊ ME VENCEU!\033[m Bem, eu não esperava por isso...quer jogar mais uma vez?')
elif escolhajogador == 'TESOURA' and escolhapc == 'PEDRA':
    print('\033[1;31mVOCÊ PERDEU!\033[m Eu sabia que iria te vencer!')
else:
    print('\033[1;4;31mVocê não escolheu uma opção válida!\033[m'
          '\nTente novamente e escolhe entre "Pedra", "Papel" e "Tesoura" ')
