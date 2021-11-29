from pydantic import Field
from pydantic_schema_org.LegalService import LegalService


class Notary(LegalService):
    """A notary.

    See https://schema.org/Notary.

    """

    locals().update({"@type": Field("Notary", const=True)})


Notary.update_forward_refs()
