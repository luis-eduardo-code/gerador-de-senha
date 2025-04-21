from gerarSenha import GeradorSenha
from dicLoader import DicioLeitor

class Main:
    def __init__(self):
        # Inicializa o dicionário e o gerador de senhas
        self.dicionario = DicioLeitor()
        self.dicionario.load_dictionary()  
        self.gerador = GeradorSenha()

    def executar(self):
        senha = self.gerador.gerador_senha(self.dicionario)
        print("Senha gerada:", senha)

if __name__ == "__main__":
    app = Main()
    app.executar()

