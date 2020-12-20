from abc import ABC

from urigrab.tld_manager.tld_page_parser.abc import AbstractParsedTLDPage


class AbstractTLDRetriever(ABC):
    def get_top_level_domains(self) -> AbstractParsedTLDPage: ...


class AbstractAsyncTLDRetriever(ABC):
    async def get_top_level_domains(self) -> AbstractParsedTLDPage: ...
