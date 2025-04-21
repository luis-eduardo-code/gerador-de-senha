# test_gerarSenha.py
import pytest
import string
from unittest.mock import Mock, patch
from gerarSenha import GeradorSenha

class TestGeradorSenha:
    
    @pytest.fixture
    def mock_dicionario(self):
        """Cria um mock do objeto DicioLeitor."""
        mock = Mock()
        mock.get_common_words.return_value = {"senha", "password", "123456", "qwerty", "admin"}
        return mock
    
    def test_init(self):
        """Testa a inicialização da classe GeradorSenha."""
        gerador = GeradorSenha()
        assert isinstance(gerador, GeradorSenha)
    
    def test_listas(self):
        """Testa o método listas que prepara os conjuntos de caracteres."""
        gerador = GeradorSenha()
        list_numero, alfa_maiuscula, alfa_minuscula, list_simbolos = gerador.listas()
        
        # Verifica se as listas contêm os caracteres esperados
        assert set(list_numero) == set(string.digits)
        
        # Verifica se as vogais maiúsculas foram removidas
        assert not set(['A', 'E', 'I', 'O', 'U']).issubset(set(alfa_maiuscula))
        
        # Verifica se as vogais minúsculas foram removidas
        assert not set(['a', 'e', 'i', 'o', 'u']).issubset(set(alfa_minuscula))
        
        # Verifica se os símbolos estão presentes
        assert set(list_simbolos) == set(string.punctuation)
    
    @patch('secrets.choice')
    @patch('secrets.SystemRandom')
    def test_gerador_senha_comprimento(self, mock_system_random, mock_choice, mock_dicionario):
        """Testa se a senha gerada tem o comprimento correto."""
        # Configura o mock para retornar valores específicos
        mock_choice.side_effect = lambda x: x[0] if x else 'a'
        mock_shuffle = Mock()
        mock_system_random.return_value.shuffle = mock_shuffle
        
        gerador = GeradorSenha()
        
        # Testa com diferentes tamanhos
        for tamanho in [10, 15, 20]:
            senha = gerador.gerador_senha(mock_dicionario, tamanho)
            assert len(senha) == tamanho + 2  # +2 por causa dos números extras
    
    def test_gerador_senha_caracteres(self, mock_dicionario):
        """Testa se a senha gerada contém os tipos de caracteres exigidos."""
        gerador = GeradorSenha()
        tamanho = 19
        
        # Gera a senha
        senha = gerador.gerador_senha(mock_dicionario, tamanho)
        
        # Verifica se a senha contém pelo menos uma letra maiúscula
        assert any(c.isupper() for c in senha)
        
        # Verifica se a senha contém pelo menos uma letra minúscula
        assert any(c.islower() for c in senha)
        
        # Verifica se a senha contém pelo menos um dígito
        assert any(c.isdigit() for c in senha)
        
        # Verifica se a senha contém pelo menos um caractere especial
        assert any(c in string.punctuation for c in senha)
    
    def test_gerador_senha_evita_palavras_dicionario(self, mock_dicionario):
        """Testa se a senha gerada evita palavras comuns do dicionário."""
        gerador = GeradorSenha()
        
        # Gera várias senhas para aumentar a probabilidade de testar bem
        for _ in range(5):
            senha = gerador.gerador_senha(mock_dicionario)
            
            # Verifica se nenhuma das palavras do dicionário está na senha

            
            senha_lower = senha.lower()
            for palavra in mock_dicionario.get_common_words():
                assert palavra not in senha_lower
    
    def test_gerador_senha_max_repeticoes(self, mock_dicionario):
        """Testa se a senha gerada respeita o limite máximo de repetições de caracteres."""
        gerador = GeradorSenha()
        
        for _ in range(5):  # Gera várias senhas para aumentar cobertura
            senha = gerador.gerador_senha(mock_dicionario)
            
            # Conta a frequência de cada caractere
            char_count = {}
            for char in senha:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            
            # Verifica se nenhum caractere se repete mais de 3 vezes
            for char, count in char_count.items():
                assert count <= 3, f"O caractere '{char}' aparece {count} vezes na senha"