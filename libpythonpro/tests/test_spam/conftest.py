import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()  # defina que sessão é um objeto da clase Sessao
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
