from typing import (
    Iterator,
    Optional,
    Tuple,
    Type,
)

from urigrab.tld_manager import TLDManager
from urigrab.tld_manager.abc import AbstractTLDManager
from urigrab.uri_parser import RegexURIParser
from urigrab.uri_parser.abc import AbstractURIParser


class URIGrabber:
    _DEFAULT_TLD_MANAGER_CLASS: Type[AbstractTLDManager] = TLDManager
    _DEFAULT_PARSER_CLASS: Type[AbstractURIParser] = RegexURIParser

    def __init__(self, *,
                 tld_manager: Optional[AbstractTLDManager] = None,
                 parser: Optional[AbstractURIParser] = None):

        self._tld_manager = tld_manager or self._DEFAULT_TLD_MANAGER_CLASS()
        self._parser = parser or self._DEFAULT_PARSER_CLASS()

        self._tld_manager.update()
        self._parser.update_tld_list(self._tld_manager.get_tld_list())

    def get_uris(self, text: str) -> Tuple[str, ...]:
        return self._parser.get_uris(text)

    def has_uris(self, text: str) -> bool:
        return self._parser.has_uris(text)

    def iter_uris(self, text: str) -> Iterator[str]:
        return self._parser.iter_uris(text)
