from abc import ABC
from typing import (
    Iterator,
    Tuple,
)


class AbstractURIParser(ABC):
    def update_tld_list(self, tld_list: Tuple[str, ...]) -> None: ...

    def get_uris(self, text: str) -> Tuple[str, ...]: ...

    def has_uris(self, text: str) -> bool: ...

    def iter_uris(self, text: str) -> Iterator[str]: ...
