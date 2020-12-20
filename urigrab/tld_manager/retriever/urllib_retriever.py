import urllib.request
from typing import Optional, Dict, Type

from urigrab.tld_manager.tld_page_parser import IANATLDPageParser
from urigrab.tld_manager.tld_page_parser.abc import AbstractTLDPageParser, AbstractParsedTLDPage
from urigrab.tld_manager.retriever.abc import AbstractTLDRetriever


class URLLibTLDRetriever(AbstractTLDRetriever):
    _DEFAULT_IANA_URL: str = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
    _DEFAULT_PAGE_PARSER_CLASS: Type[AbstractTLDPageParser] = IANATLDPageParser
    _DEFAULT_REQ_HEADERS: Dict[str, str] = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.67 Safari/537.36'
    }

    def __init__(self, *,
                 tld_url: str = _DEFAULT_IANA_URL,
                 request_headers: Optional[Dict[str, str]] = None,
                 page_parser: Optional[AbstractTLDPageParser] = None) -> None:
        self._tld_url = tld_url
        self._req_headers = request_headers or self._DEFAULT_REQ_HEADERS.copy()
        if page_parser is not None:
            self._page_parser = page_parser
        else:
            self._page_parser = self._DEFAULT_PAGE_PARSER_CLASS()

    def get_top_level_domains(self) -> AbstractParsedTLDPage:
        tld_page: str = self._fetch()
        return self._page_parser.parse_tld_page(tld_page)

    def _fetch(self) -> str:
        req = urllib.request.Request(self._tld_url)
        for name, val in self._req_headers.items():
            req.add_header(name, val)

        with urllib.request.urlopen(req) as res:
            return res.read().decode('utf-8')
