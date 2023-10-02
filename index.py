#biblioteca Ramdom
import random
from tkinter import *

#pedra, papel tesoura

gab = {
    1 : 'pedra',
    2 : 'papel',
    3 : 'tesoura'
}
#print(gab) gab = gabarito
print('gabarito:\npedra = 1\npapel = 2\ntesoura = 3')
print('-'*50)

i = True
while i:
    numero = int(random.uniform(1,4)) #aqui não será mostrado o numero 4 no resultado. apenas valores abaixo (1 a 3)
    while i:
        desafio = int(input('insira o um valor entre 1 e 3. tente vençer o pedra, papel tesoura: '))
        if desafio > 3 or desafio < 1:
            print('apenas números entre 1 e 3')
        else:
            break
    
    print('-'*50)
    #resultados

    #cenário em que pedra vence tesoura
    if (desafio == 1 and numero >2):
        print(f'{gab.get(desafio)} venceu {gab.get(numero)}')

    #cenario em que pedra perde para papel
    if desafio == 1 and numero ==2:
        print(f'{gab.get(desafio)} perdeu para {gab.get(numero)}')

    #cenario em que papel vence
    if (desafio == 2 and numero < 2 ):
        print(f'{gab.get(desafio)} venceu {gab.get(numero)}')


    #cenário em que tesoura vence papel
    if (desafio == 2 and numero > 2):
        print(f'{gab.get(desafio)} perdeu para {gab.get(numero)}')
    else:
        print('nada acontece')
        
    print(f'numero da rodada {numero}')

    quest = int(input('deseja jogar novamente ? [sim = 1, não = 2] '))
    
    if quest == 1:
        pass
    else:
        i= False
        break
    print('-'*50)

print('fim do jogo')


#estrutura visual no tkinter

'''tela = Tk()
tela.title('pedra,papel e tesoura')

instrucao = Label(tela, text='bem vindo ao nosso jogo\nconsegue nos vencer ?')
instrucao.grid(column=0, row=0)

inst = Label(tela, text='insira um valor entre 1 e 3')
inst.grid(column=0,  row=1)
entrada = Entry(tela, width=15)
entrada.grid(column=1,row=1)

botao_jogar = Button(tela, text="jogar") #"command=#)
botao_jogar.grid(column=0,row=2)



tela.mainloop()'''