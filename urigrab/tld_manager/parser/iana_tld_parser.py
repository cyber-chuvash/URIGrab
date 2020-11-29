import encodings.idna
from dataclasses import dataclass
from datetime import datetime

from typing import Tuple, Iterable, Iterator

from urigrab.tld_manager.parser.abc import AbstractTLDPageParser, AbstractParsedTLDPage


class IANATLDPageParser(AbstractTLDPageParser):
    def parse_tld_page(self, tld_page: str) -> 'ParsedIANATLDPage':
        # TODO do properly
        tld_list = tuple(self._prep_tld_list(tld_page.splitlines()[1:]))
        return ParsedIANATLDPage(version='test', last_updated=datetime.now(), tld_list=tld_list)

    @staticmethod
    def _prep_tld_list(tld_list: Iterable[str]) -> Iterator[str]:
        for l_tld in tld_list:
            l_tld = l_tld.lower()
            unicode_tld = encodings.idna.ToUnicode(l_tld)
            yield unicode_tld
            if l_tld != unicode_tld:
                yield l_tld


@dataclass(frozen=True)
class ParsedIANATLDPage(AbstractParsedTLDPage):
    version: str
    last_updated: datetime
    tld_list: Tuple[str, ...]
