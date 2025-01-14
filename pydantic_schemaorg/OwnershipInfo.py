from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person"
     "owned a certain product.

    See: https://schema.org/OwnershipInfo
    Model depth: 4
    """

    type_: str = Field(default="OwnershipInfo", alias="@type", const=True)
    ownedThrough: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The date and time of giving up ownership on the product.",
    )
    ownedFrom: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The date and time of obtaining the product.",
    )
    acquiredFrom: Optional[
        Union[List[Union["Organization", "Person", str]], "Organization", "Person", str]
    ] = Field(
        default=None,
        description="The organization or person from which the product was acquired.",
    )
    typeOfGood: Optional[
        Union[List[Union["Product", "Service", str]], "Product", "Service", str]
    ] = Field(
        default=None,
        description="The product that this structured value is referring to.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Service import Service
