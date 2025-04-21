import os
from typing import Set

dicinario= r"c:\Users\music\OneDrive\Desktop\prejetos git\Projeto Gerador de Senha\testes\arguivoDicionario\dicionario.txt"

class DicioLeitor:
    def __init__(self):
        self._common_words = set()
    
    def load_dictionary(self, ):
        """Carrega um dicionário a partir de um arquivo."""
        if not os.path.exists(dicinario):
             raise FileNotFoundError(f"Arquivo de dicionário não encontrado: {dicinario}")
            
        with open(dicinario, 'r', encoding='utf-8') as file:
            self._common_words = {line.strip().lower() for line in file if line.strip()}

        return self._common_words
    
    def get_common_words(self) -> Set[str]:
        """Retorna o conjunto de palavras comuns do dicionário."""
        return self._common_words
    
    def is_common_word(self, word: str) -> bool:
        """Verifica se uma palavra é comum no dicionário."""
        return word.lower() in self._common_words
    
    


    
 