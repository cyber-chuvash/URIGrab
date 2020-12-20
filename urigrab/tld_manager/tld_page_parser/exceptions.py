
class BaseTLDPageParserError(Exception):
    pass


class IANATLDParserError(BaseTLDPageParserError):
    pass


class IANAMetadataParsingError(IANATLDParserError):
    pass
