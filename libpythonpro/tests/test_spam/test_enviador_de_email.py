import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['eduardo.bazler@unesp.br', 'foo@bar.com.br']
)
def test_remetente(destinatario):  #utiliza o parametro destinatio pra ada elemento da lista à cima
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'edubazler@gmail.com',
        'Cursos Python Pro',
        'Turmas abertas'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['eduardo.bazler_unesp.br', '']
)
def test_remetente_invado(remetente):  #utiliza o parametro destinatio pra ada elemento da lista à cima
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'edubazler@gmail.com',
            'Cursos Python Pro',
            'Turmas abertas'
        )

