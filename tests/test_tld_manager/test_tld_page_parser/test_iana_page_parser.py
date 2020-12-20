import pytest

from urigrab.tld_manager.tld_page_parser import IANATLDPageParser, ParsedIANATLDPage
from tests.data import (
    iana_tld_page,
    iana_tld_page_version,
    iana_tld_page_last_updated,
    iana_tld_count
)


@pytest.fixture
def iana_page_parser() -> IANATLDPageParser:
    return IANATLDPageParser()


def test_iana_page_parser(iana_page_parser: IANATLDPageParser):
    parsed_tld_page: ParsedIANATLDPage = iana_page_parser.parse_tld_page(iana_tld_page)

    assert parsed_tld_page.version == iana_tld_page_version
    assert parsed_tld_page.last_updated == iana_tld_page_last_updated
    assert len(parsed_tld_page.tld_list) == iana_tld_count
