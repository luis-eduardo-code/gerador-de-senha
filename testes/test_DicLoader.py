# -*- coding: utf-8 -*-
# Teste unitário para a classe DicioLeitor
import pytest
from dicLoader import DicioLeitor

class TestDicioLeitor:
    
    @pytest.fixture
    def test_temp_dictionary_file(self, tmp_path):
        """Cria um arquivo de dicionário temporário para testes."""
        file_path = tmp_path / "test_dictionary.txt"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("senha\npassword\n123456\nqwerty\nadmin\nletmein\n")
        return file_path
    
    def test_init(self):
        """Testa a inicialização da classe DicioLeitor."""
        loader = DicioLeitor()
        assert loader._common_words == set()
    
    def test_load_dictionary(self):
        """Testa o carregamento de um dicionário de arquivo."""
        loader = DicioLeitor()
        loader.load_dictionary()
        
        # Verifica se todas as palavras foram carregadas
        assert len(loader._common_words) > 0
        assert "senha" in loader._common_words
        assert "password" in loader._common_words
        assert "123456" in loader._common_words
        
    def test_load_dictionary_file_not_found(self,tmp_path):
        """Testa o comportamento quando o arquivo não existe."""
        loader = DicioLeitor()
        with pytest.raises(FileNotFoundError):
            loader.load_dictionary()
    
    def test_get_common_words(self, tmp_path):
        """Testa o método get_common_words."""
        loader = DicioLeitor()
        loader.load_dictionary(tmp_path)
        
        words = loader.get_common_words(tmp_path)
        assert isinstance(words, set)
        assert len(words) > 0
        assert "senha" in words
    
    def test_is_common_word(self, tmp_path):
        """Testa o método is_common_word."""
        loader = DicioLeitor()
        loader.load_dictionary(tmp_path)
        
        # Palavras que estão no dicionário, futuramente cada senha criada vem para cá afim de evitar que o usuário crie senhas iguais
        assert loader.is_common_word("janeiro") is True
        assert loader.is_common_word("senhA123marc") is True  # Verifica case-insensitive
        assert loader.is_common_word("dia45ano78") is True
        
        