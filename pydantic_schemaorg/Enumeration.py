from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class Enumeration(Intangible):
    """Lists or enumerations—for example, a list of cuisines or music genres, etc.

    See: https://schema.org/Enumeration
    Model depth: 3
    """

    type_: str = Field("Enumeration", const=True, alias="@type")
    supersededBy: "Optional[Union[List[Union[Class, 'Enumeration', Property, str]], Union[Class, 'Enumeration', Property, str]]]" = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Class import Class

    from pydantic_schemaorg.Property import Property

    Enumeration.update_forward_refs()
