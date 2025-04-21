# -*- coding: utf-8 -*-
import pytest
from gerarSenha import GeradorSenha


class TestPasswordPolicy:
    
    def test(self):
        policy = GeradorSenha.gerador_senha()
        assert policy.min_length == 12
        assert policy.max_length == 32
        assert policy.require_uppercase is True
        assert policy.require_lowercase is True
        assert policy.require_digits is True
        assert policy.require_special_chars is True
        assert policy.max_repeated_chars == 3
        assert policy.avoid_dictionary_words is True
        assert policy.min_strength == 0.