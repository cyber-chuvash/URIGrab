from abc import ABC
from datetime import datetime

from typing import Tuple


class AbstractTLDPageParser(ABC):
    def parse_tld_page(self, tld_page: str) -> 'AbstractParsedTLDPage': ...


class AbstractParsedTLDPage(ABC):
    version: str
    last_updated: datetime
    tld_list: Tuple[str, ...]
