from pydantic import Field
from pydantic_schema_org.CreativeWork import CreativeWork


class Photograph(CreativeWork):
    """A photograph.

    See https://schema.org/Photograph.

    """

    locals().update({"@type": Field("Photograph", const=True)})


Photograph.update_forward_refs()
