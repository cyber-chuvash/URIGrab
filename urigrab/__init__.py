from typing import (
    Iterator,
    Optional,
    Tuple,
)

from urigrab.grabber import URIGrabber
from urigrab.tld_manager import TLDManager

__all__ = (
    "URIGrabber", "get_uris", "has_uris", "iter_uris"
)

_default_grabber: Optional[URIGrabber] = None


def _init_default_grabber() -> None:
    global _default_grabber
    if not _default_grabber:
        _default_grabber = URIGrabber()


def get_uris(text: str) -> Tuple[str, ...]:
    _init_default_grabber()
    return _default_grabber.get_uris(text)


def has_uris(text: str) -> bool:
    _init_default_grabber()
    return _default_grabber.has_uris(text)


def iter_uris(text: str) -> Iterator[str]:
    _init_default_grabber()
    return _default_grabber.iter_uris(text)
