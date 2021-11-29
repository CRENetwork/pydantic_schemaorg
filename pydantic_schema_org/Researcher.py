from pydantic import Field
from pydantic_schema_org.Audience import Audience


class Researcher(Audience):
    """Researchers.

    See https://schema.org/Researcher.

    """

    locals().update({"@type": Field("Researcher", const=True)})


Researcher.update_forward_refs()
