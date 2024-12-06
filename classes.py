class Pessoa: 
    # Em python o self ta declarado então os parametros que vem dentros do parentesis no codigo principal vao para o lugar dos proximos argumentos da proxima linha excluindo o self
    def __init__(self, nome, idade): # Nunca é chamado so serve para construir as variaveis dentro da classe
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"O meu nome é {self.nome}, e tenho {self.idade} anos" # Resumindo esta classes so serve para returnar isto ...
    
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def infomacao_do_carro(self):
        return f"Este é um {self.marca} {self.modelo}"
    
class Jogador:
    def __init__(self, nome, pac, sho, pas, dri, df, phy, pos):
        self.nome = nome
        self.pac = pac
        self.sho = sho
        self.pas = pas
        self.dri = dri
        self.df = df
        self.phy = phy
        self.pos = pos


    def calcular_overall(self):
        if (self.pos == "Atacante"):
            self.overall = (self.pac + self.sho + self.pas + self.dri + self.phy) / 5 # Valoriza mais o ataque e nao valoriza defesa

        elif (self.pos == "Medio"):
            self.overall = (self.pac + self.sho + self.pas + self.dri + self.df + self.phy) / 6 # valoriza tudo

        elif (self.pos == "Defesa"):
            self.overall = (self.pac + self.pas + self.dri + self.df + self.phy) / 5 # Valoriza a defesa mas nao valoriza o ataque

        self.overall = round(self.overall)

        return self.overall
            