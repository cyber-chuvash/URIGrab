from datetime import datetime
from typing import Optional, Type, Tuple

from urigrab.tld_manager.abc import AbstractTLDManager
from urigrab.tld_manager.parser.abc import AbstractParsedTLDPage
from urigrab.tld_manager.retriever.abc import AbstractTLDRetriever
from urigrab.tld_manager.retriever.urllib_retriever import URLLibTLDRetriever


class TLDManager(AbstractTLDManager):
    _DEFAULT_TLD_RETRIEVER_CLASS: Type[AbstractTLDRetriever] = URLLibTLDRetriever

    def __init__(self, *,
                 tld_retriever: Optional[AbstractTLDRetriever] = None):

        self._last_update: Optional[datetime] = None
        self._list_version: Optional[str] = None
        self._tld_list: Optional[Tuple[str, ...]] = None

        if tld_retriever is not None:
            self._tld_retriever = tld_retriever
        else:
            self._tld_retriever = self._DEFAULT_TLD_RETRIEVER_CLASS()

    @property
    def last_update(self) -> datetime:
        return self._last_update

    @property
    def tld_version(self) -> str:
        return self._list_version

    def update(self) -> None:
        tld_data: AbstractParsedTLDPage = self._tld_retriever.get_top_level_domains()
        self._last_update = tld_data.last_updated
        self._list_version = tld_data.version
        self._tld_list = tld_data.tld_list

    def get_tld_list(self) -> Tuple[str, ...]:
        if self._last_update is None:
            self.update()
        return self._tld_list
