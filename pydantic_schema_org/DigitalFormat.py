from pydantic import Field
from pydantic_schema_org.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalFormat(MusicReleaseFormatType):
    """DigitalFormat.

    See https://schema.org/DigitalFormat.

    """

    locals().update({"@type": Field("DigitalFormat", const=True)})


DigitalFormat.update_forward_refs()
