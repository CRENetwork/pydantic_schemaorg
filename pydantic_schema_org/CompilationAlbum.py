from pydantic import Field
from pydantic_schema_org.MusicAlbumProductionType import MusicAlbumProductionType


class CompilationAlbum(MusicAlbumProductionType):
    """CompilationAlbum.

    See https://schema.org/CompilationAlbum.

    """

    locals().update({"@type": Field("CompilationAlbum", const=True)})


CompilationAlbum.update_forward_refs()
