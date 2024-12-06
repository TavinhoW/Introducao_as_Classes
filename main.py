import os
from instanciar import pessoa_1, carro_1, overall # Importa do ficheiro instanciar a variavel criada da classe

# Classe Pessoa

print(pessoa_1.saudacao()) # print(nomevariavel.nomefuncaodaclasse())


# Classe Carro

print(carro_1.infomacao_do_carro())


# Classe Jogadores Overall

nome = str(input("Digite o nome do jogador: "))
pos = str(input("Digite a posição do jogador (1 - Atacante ; 2 - Medio ; 3 - Defesa): "))
pac = int(input("Digite a Velocidade do jogador: "))
sho = int(input("Digite o remate do jogador: "))
pas = int(input("Digite o passe do jogador: "))
dri = int(input("Digite o drible do jogador: "))
df = int(input("Digite a defesa do jogador: "))
phy = int(input("Digite o fisico do jogador: "))

os.system('cls')

if (pos == '1'):
    pos = "Atacante"

elif (pos == '2'):
    pos = "Medio"

elif (pos == '3'):
    pos = "Defesa"

print("Nome: ", nome, "\nPosição: ", pos, "\n\nOverall: ", overall.calcular_overall(), "\nPAC: ", pac, "\nSHO: ", sho, "\nPAS: ", pas, "\nDRI: ", dri, "\nDEF: ", df, "\nPHY: ", phy)

