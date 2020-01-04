import random 

a = 1
j = 11
q = 12
k = 13

baralho = [a,2,3,4,5,6,7,8,9,10,j,q,k,]

jogar = "S"

jog1 = []
jog2 = []

total1 = 0
total2 = 0

def Iniciar():
  pegarCarta(jog1, baralho)
  pegarCarta(jog2, baralho)
  pegarCarta(jog2, baralho)

def pegarCarta(jogador, baralho):

  carta = random.choice(baralho)
  total = 0
  global jogar

  jogador.append(carta)
  baralho.remove(carta)

  for i in range(len(jogador)):
    total += jogador[i]

  print(jogador,"pegou carta", carta, ", soma total de cartas: ", total)

  if total > 21:
    print(jogador, " perdeu")
    jogar = "N"

Iniciar()

print(jogar)

while jogar.upper() == "S":
  
  jogar = input("desejar pegar mais uma carta? [s/n]")
  
  pegarCarta(jog1,baralho)

  
for i in range(len(jog1)):
    total1 += jog1[i]

for i in range(len(jog2)):
    total2 += jog2[i] 

if total1 > total2 and total1 <= 21:
  print(jog1, " venceu")
else:
  print(jog2, " venceu")
