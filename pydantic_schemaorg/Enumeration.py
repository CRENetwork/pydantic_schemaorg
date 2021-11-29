from pydantic import Field
from typing import List, Optional, Union, Any
from pydantic_schemaorg.Intangible import Intangible


class Enumeration(Intangible):
    """Lists or enumerations—for example, a list of cuisines or music genres, etc.

    See https://schema.org/Enumeration.

    """

    supersededBy: Any = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    locals().update({"@type": Field("Enumeration", const=True)})


Enumeration.update_forward_refs()
