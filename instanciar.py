from classes import Pessoa, Carro, Jogador # Importa as classes do ficheiro classes e cria, para depois enviar a variavel cridada da classe para o ficheiro main
from main import nome, pac, sho, pas, dri, df, phy, pos # Importa do ficheiro main algumas variaveis necessarias para o uso da classe Jogador, para depois enviar a a variavel com tudo criado para o main


pessoa_1 = Pessoa("Gustavo", "17") # Pega o return da classe e mete na variavel pessoa_1, com os seguintes parametros
# A pessoa_1 por dizendo fica com as funções dentro então para dar print em alguma coisa precisas de meter o nome .(...())


carro_1 = Carro("BMW", "I8")


overall = Jogador(nome, pac, sho, pas, dri, df, phy, pos)