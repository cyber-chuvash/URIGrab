import encodings.idna
import re
from datetime import datetime
from dataclasses import dataclass

from typing import List, Tuple, Iterable, Iterator

from urigrab.tld_manager.tld_page_parser.abc import AbstractTLDPageParser, AbstractParsedTLDPage
from urigrab.tld_manager.tld_page_parser.exceptions import IANAMetadataParsingError


class IANATLDPageParser(AbstractTLDPageParser):
    _METADATA_REGEX: re.Pattern = re.compile(r"# Version (?P<ver>\d+), Last Updated (?P<date>.*)")

    def parse_tld_page(self, tld_page: str) -> 'ParsedIANATLDPage':
        page_lines: List[str] = tld_page.splitlines()
        version, last_updated = self._get_metadata(page_lines[0])
        tld_list = tuple(self._prep_tld_list(page_lines[1:]))

        return ParsedIANATLDPage(version=version, last_updated=last_updated, tld_list=tld_list)

    def _get_metadata(self, metadata_line: str) -> Tuple[str, datetime]:
        match: re.Match = self._METADATA_REGEX.match(metadata_line)
        if not match:
            raise IANAMetadataParsingError(f"Could not get metadata from IANA metadata line: '{metadata_line}'")
        version: str = match.group('ver')
        date: datetime = datetime.strptime(match.group('date'), '%a %b %d %H:%M:%S %Y UTC')
        return version, date

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
