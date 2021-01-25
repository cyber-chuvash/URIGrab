import pytest

from tests.data import (
    iana_tld_count,
    iana_tld_page,
    iana_tld_page_last_updated,
    iana_tld_page_version,
)
from urigrab.tld_manager.tld_page_parser import (
    IANATLDPageParser,
    ParsedIANATLDPage,
)
from urigrab.tld_manager.tld_page_parser.exceptions import IANAMetadataParsingError


@pytest.fixture
def iana_page_parser() -> IANATLDPageParser:
    return IANATLDPageParser()


def test_iana_page_parser(iana_page_parser: IANATLDPageParser) -> None:
    parsed_tld_page: ParsedIANATLDPage = iana_page_parser.parse_tld_page(iana_tld_page)

    assert parsed_tld_page.version == iana_tld_page_version
    assert parsed_tld_page.last_updated == iana_tld_page_last_updated
    assert len(parsed_tld_page.tld_list) == iana_tld_count


def test_iana_page_parser_bad_metadata(iana_page_parser: IANATLDPageParser) -> None:
    corrupted_page = iana_tld_page[3:]
    with pytest.raises(IANAMetadataParsingError):
        iana_page_parser.parse_tld_page(corrupted_page)
