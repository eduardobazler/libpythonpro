from libpythonpro.spam.moedelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Eduardo', email= 'eduardo.bazler@unesp.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(conexao, sessao):
    usuarios = [Usuario(nome='Eduardo', email= 'eduardo.bazler@unesp.br'),
                Usuario(nome='Renzo', email= 'eduardo.bazler@unesp.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()