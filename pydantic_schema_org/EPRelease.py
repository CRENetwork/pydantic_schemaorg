from pydantic import Field
from pydantic_schema_org.MusicAlbumReleaseType import MusicAlbumReleaseType


class EPRelease(MusicAlbumReleaseType):
    """EPRelease.

    See https://schema.org/EPRelease.

    """

    locals().update({"@type": Field("EPRelease", const=True)})


EPRelease.update_forward_refs()
