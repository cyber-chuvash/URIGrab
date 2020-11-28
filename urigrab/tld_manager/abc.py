from abc import ABC, abstractmethod
from datetime import datetime
from typing import Sequence


class AbstractTLDManager(ABC):
    @property
    @abstractmethod
    def last_update(self) -> datetime: ...

    @property
    @abstractmethod
    def tld_version(self) -> str: ...

    def update(self) -> None: ...

    def get_tld_list(self) -> Sequence[str]: ...


class AbstractAsyncTLDManager(ABC):
    async def update(self) -> None: ...
