from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

import urigrab
from urigrab import URIGrabber


def reset_default_grabber() -> None:
    urigrab._default_grabber = None


@pytest.fixture
def _resetting_default_grabber() -> None:
    try:
        reset_default_grabber()
        yield
    finally:
        reset_default_grabber()


def test_init_default_grabber(_resetting_default_grabber: None) -> None:
    assert urigrab._default_grabber is None
    urigrab._init_default_grabber()
    assert urigrab._default_grabber is not None
    assert isinstance(urigrab._default_grabber, URIGrabber)


def _reset_mocks(*mocks: Mock) -> None:
    for mock in mocks:
        mock.reset_mock()


def test_basic_api_methods(mocker: MockerFixture, _resetting_default_grabber: None) -> None:
    # Testing only the fact that they call to init default grabber and then call the required method on it

    test_text = 'test text'
    get_uri_val = ('test', )
    iter_uri_val = iter(('test', ))

    # Setting up mocks (we don't want to actually run any internal machinery
    urigrabber_mock = Mock()
    urigrabber_mock.get_uris.return_value = get_uri_val
    urigrabber_mock.has_uris.return_value = False
    urigrabber_mock.iter_uris.return_value = iter_uri_val

    init_default_mock: Mock = mocker.patch(
        'urigrab._init_default_grabber',
        new=Mock(wraps=lambda: setattr(urigrab, '_default_grabber', urigrabber_mock))
    )

    # Testing get_uris() method
    assert urigrab.get_uris(test_text) is get_uri_val
    init_default_mock.assert_called_once_with()
    urigrabber_mock.get_uris.assert_called_once_with(test_text)

    _reset_mocks(init_default_mock, urigrabber_mock)

    # Testing has_uris() method
    assert urigrab.has_uris(test_text) is False
    init_default_mock.assert_called_once_with()
    urigrabber_mock.has_uris.assert_called_once_with(test_text)

    _reset_mocks(init_default_mock, urigrabber_mock)

    # Testing iter_uris() method
    assert urigrab.iter_uris(test_text) is iter_uri_val
    init_default_mock.assert_called_once_with()
    urigrabber_mock.iter_uris.assert_called_once_with(test_text)
