from http import HTTPStatus

from jwt import decode

from fast_zero.security import ALGORITHM, create_access_token
from fast_zero.settings import Settings

settings = Settings()


def test_jwt():
    data = {'sub': 'teste@teste.com'}
    token = create_access_token(data)

    result = decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])

    assert result['sub'] == data['sub']
    assert result['exp'] > 0


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
