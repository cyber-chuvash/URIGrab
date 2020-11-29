import pathlib
from typing import Tuple

_parent_dir: pathlib.Path = pathlib.Path(__file__).parent


with open(_parent_dir / 'valid_uris.txt', 'r') as _valid_uris_file:
    valid_uris: Tuple[str] = tuple(_valid_uris_file.read().splitlines())

with open(_parent_dir / 'invalid_uris.txt', 'r') as _invalid_uris_file:
    invalid_uris: Tuple[str] = tuple(_invalid_uris_file.read().splitlines())
