import secrets
import string
from dicLoader import DicioLeitor

class GeradorSenha:
    def __init__(self):
        # Inicializa o dicionário
        self.dicionario = DicioLeitor()
        

        
        
    def listas(self):
        # Lista de números aleatórios
        list_numero = list(string.digits)

        # Lista alfabeto maiúsculo (sem vogais)
        vogais_maiusculas = ['A', 'E', 'I', 'O', 'U']
        list_maiuscula = list(string.ascii_uppercase)
        alfa_maiuscula = [
            letra for letra in list_maiuscula 
            if letra not in vogais_maiusculas
        ]
        
        # Lista alfabeto minúsculo (sem vogais)
        vogais_minusculas = ['a', 'e', 'i', 'o', 'u']
        list_minuscula = list(string.ascii_lowercase)
        alfa_minuscula = [
            letra for letra in list_minuscula 
            if letra not in vogais_minusculas
        ]
        
        # Lista de símbolos
        list_simbolos = list(string.punctuation)

        return list_numero, alfa_maiuscula, alfa_minuscula, list_simbolos
        
    def gerador_senha(self, dicionario, tamanho=17):
        # Importando dados
        list_numero, alfa_maiuscula, alfa_minuscula, list_simbolos = self.listas()

        # Código para gerar a senha
        senha_certa = False

        # Pelo menos 1 letra maiúscula, 1 letra minúscula, 1 símbolo e 1 número
        senha_formada = [
            secrets.choice(alfa_maiuscula),  # letra maiúscula
            secrets.choice(alfa_minuscula),  # letra minúscula
            secrets.choice(list_simbolos),   # símbolo
            secrets.choice(list_numero)      # número
        ]

        while not senha_certa:
            # Gerando a senha só com letras minúsculas e maiúsculas
            senha_formada_letra = []

            for _ in range(tamanho - 3):
                caractere = secrets.choice(alfa_maiuscula + alfa_minuscula + list_simbolos)
                senha_formada_letra.append(caractere)
                
            # Verificando se a senha gerada contém palavras do dicionário
            senha_texto = ''.join(senha_formada_letra).lower()
            
            if not any(palavra in senha_texto for palavra in dicionario.load_dictionary()):
                senha_formada.extend(senha_formada_letra)
                senha_certa = True
                
                # Adicionando mais 2 números à senha
                for _ in range(2):
                    while True:
                        numero = secrets.choice(list_numero)
                        if senha_formada.count(numero) < 3:
                            senha_formada.append(numero)
                            break
                
                # Embaralhando a senha final
                secrets.SystemRandom().shuffle(senha_formada)
                return ''.join(senha_formada)