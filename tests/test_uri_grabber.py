from collections.abc import Iterator
from typing import Tuple

import pytest

from urigrab import URIGrabber
from .data import valid_uris


@pytest.fixture(scope='module')
def uri_grabber() -> URIGrabber:
    return URIGrabber()


def test_uri_grabber_properly_inited(uri_grabber: URIGrabber):
    assert uri_grabber._tld_manager is not None
    assert uri_grabber._parser is not None

    assert uri_grabber._tld_manager.last_update is not None
    assert uri_grabber._tld_manager.tld_version is not None
    assert uri_grabber._parser._uri_regex is not None


@pytest.mark.parametrize('valid_uri', valid_uris)
def test_uri_grabber_get_uris(valid_uri: str, uri_grabber: URIGrabber):
    text = f"test text with a URI somewhere... ({valid_uri})! oh wow there it was! How unexpected."
    found_uris: Tuple[str] = uri_grabber.get_uris(text)
    assert len(found_uris) == 1
    assert found_uris[0] == valid_uri


@pytest.mark.parametrize('valid_uri', valid_uris)
def test_uri_grabber_has_uris(valid_uri: str, uri_grabber: URIGrabber):
    text = f"Would you look at that. Another text that should contain a URI... but whe-{valid_uri} Woah! There it is."
    has_uris: bool = uri_grabber.has_uris(text)
    assert has_uris is True


def test_uri_grabber_iter_uris(uri_grabber: URIGrabber):
    text: str = ""
    for uri in valid_uris:
        text += f"I feel like my test is in a loop. " \
                f"Iterating over URIs like [this]({uri}) one in text is fun, isn't it? " \
                f"A little Markdown also doesn't hurt.\n"

    uri_iter = uri_grabber.iter_uris(text)
    assert isinstance(uri_iter, Iterator)
    assert sorted(valid_uris) == sorted(uri_iter)
