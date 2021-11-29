from pydantic import Field
from pydantic_schema_org.DigitalDocument import DigitalDocument


class SpreadsheetDigitalDocument(DigitalDocument):
    """A spreadsheet file.

    See https://schema.org/SpreadsheetDigitalDocument.

    """

    locals().update({"@type": Field("SpreadsheetDigitalDocument", const=True)})


SpreadsheetDigitalDocument.update_forward_refs()
