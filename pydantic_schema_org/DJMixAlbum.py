from pydantic import Field
from pydantic_schema_org.MusicAlbumProductionType import MusicAlbumProductionType


class DJMixAlbum(MusicAlbumProductionType):
    """DJMixAlbum.

    See https://schema.org/DJMixAlbum.

    """

    locals().update({"@type": Field("DJMixAlbum", const=True)})


DJMixAlbum.update_forward_refs()
