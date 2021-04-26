from unittest.mock import Mock
import pytest
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.moedelos import Usuario


@pytest.mark.parametrize('usuarios',
                         [
                             [
                                 Usuario(nome='Eduardo', email='eduardo.bazler@unesp.br'),
                                 Usuario(nome='Renzo', email='eduardo.bazler@unesp.br')
                             ],
                             [
                                 Usuario(nome='Eduardo', email='eduardo.bazler@unesp.br')
                             ]
                         ]
                         )
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'eduardo.bazler@unesp.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Eduardo', email='edubazler@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'eduardo.bazler@unesp.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'eduardo.bazler@unesp.br',
        'edubazler@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
