import re
from typing import Tuple, Optional, Iterator

from urigrab.uri_parser.abc import AbstractURIParser


class RegexURIParser(AbstractURIParser):
    """
        Useful for early development and testing, probably won't ever be production-ready
    """
    _REGEX_TEMPLATE: str = r"(?:https?://)?(?:[\w\d\-_]+\.)+(?:%(tld_rgx)s)[\w\d\-_\?\&\#\$\./=]*"

    def __init__(self):
        self._uri_regex: Optional[re.Pattern] = None

    def update_tld_list(self, tld_list: Tuple[str, ...]) -> None:
        self._uri_regex = self._compile_uri_regex(tld_list)

    def _compile_uri_regex(self, tld_list: Tuple[str, ...]) -> re.Pattern:
        tld_regex: str = "|".join(tld_list)
        return re.compile(self._REGEX_TEMPLATE % {"tld_rgx": tld_regex})

    def get_uris(self, text: str) -> Tuple[str, ...]:
        uris = self._uri_regex.findall(text)
        return tuple(uris)

    def has_uris(self, text: str) -> bool:
        return self._uri_regex.search(text) is not None

    def iter_uris(self, text: str) -> Iterator[str]:
        return map(lambda m: m.group(0), self._uri_regex.finditer(text))
