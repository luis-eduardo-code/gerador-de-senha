import pytest
from main import Main
from unittest.mock import patch, Mock



class TestMain:
    
    @patch('dicLoader.DicioLeitor')
    @patch('gerarSenha.GeradorSenha')
    def test_init(self, mock_gerador_class, mock_dicio_class):
        """Testa a inicialização da classe Main."""
        # Configura os mocks
        mock_dicio_instance = Mock()
        mock_gerador_instance = Mock()
        mock_dicio_class.return_value = mock_dicio_instance
        mock_gerador_class.return_value = mock_gerador_instance
        
        # Instancia a classe Main
        main = Main()
        
        # Verifica se as classes foram instanciadas corretamente
        assert main.dicionario == mock_dicio_instance
        assert main.gerador == mock_gerador_instance
        
        # Verifica se o método load_dictionary foi chamado
        mock_dicio_instance.load_dictionary.assert_called_once()
    
    @patch('builtins.print')
    def test_executar(self, mock_print):
        """Testa o método executar da classe Main."""
        # Cria mocks para as dependências
        mock_dicionario = Mock()
        mock_gerador = Mock()
        mock_gerador.gerador_senha.return_value = "SenhaTesteMock123!"
        
        # Cria a instância de Main com os mocks
        main = Main()
        main.dicionario = mock_dicionario
        main.gerador = mock_gerador
        
        # Executa o método
        main.executar()
        
        # Verifica se gerador_senha foi chamado com o dicionário
        mock_gerador.gerador_senha.assert_called_once_with(mock_dicionario)
        
        # Verifica se a senha foi impressa
        mock_print.assert_called_once_with("Senha gerada:", "SenhaTesteMock123!")