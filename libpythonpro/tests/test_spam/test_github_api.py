from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'renzon', 'id': 3457115, 'node_id': 'MDQ6VXNlcjM0NTcxMTU=',
        'avatar_url': 'https://avatars.githubusercontent.com/u/3457115?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
