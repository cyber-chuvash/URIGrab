from dataclasses import dataclass
from datetime import datetime

from typing import Tuple

from urigrab.tld_manager.parser.abc import AbstractTLDPageParser, AbstractParsedTLDPage


class IANATLDPageParser(AbstractTLDPageParser):
    def parse_tld_page(self, tld_page: str) -> 'ParsedIANATLDPage':
        # TODO do properly
        tld_list = tuple(tld_page.splitlines()[1:])
        return ParsedIANATLDPage(version='test', last_updated=datetime.now(), tld_list=tld_list)


@dataclass(frozen=True)
class ParsedIANATLDPage(AbstractParsedTLDPage):
    version: str
    last_updated: datetime
    tld_list: Tuple[str, ...]
