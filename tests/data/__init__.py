import json
import pathlib
from datetime import datetime
from typing import Tuple

_parent_dir: pathlib.Path = pathlib.Path(__file__).parent


with open(_parent_dir / 'valid_uris.txt', 'r') as _valid_uris_file:
    valid_uris: Tuple[str, ...] = tuple(_valid_uris_file.read().splitlines())

with open(_parent_dir / 'invalid_uris.txt', 'r') as _invalid_uris_file:
    invalid_uris: Tuple[str, ...] = tuple(_invalid_uris_file.read().splitlines())

with open(_parent_dir / 'data_iana_tld_page.txt', 'r') as _tld_file:
    _data: dict = json.loads(_tld_file.readline())
    iana_tld_page_version: str = _data['version']
    iana_tld_page_last_updated: datetime = datetime.fromisoformat(_data['last_updated'])
    iana_tld_page: str = _tld_file.read()

    tld_list: list = iana_tld_page.splitlines()[1:]
    iana_tld_count: int = len(tld_list)
    # Add IDNA-encoded TLDs twice, because
    # for the parser's sake IDNA encoded and decoded versions are two different TLDs
    iana_tld_count += len(tuple(filter(lambda tld: tld.startswith('XN--'), tld_list)))
