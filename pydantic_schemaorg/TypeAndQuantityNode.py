from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class TypeAndQuantityNode(StructuredValue):
    """A structured value indicating the quantity, unit of measurement, and business function"
     "of goods included in a bundle offer.

    See: https://schema.org/TypeAndQuantityNode
    Model depth: 4
    """
    type_: str = Field("TypeAndQuantityNode", alias='@type')
    businessFunction: Optional[Union[List[Union['BusinessFunction', str]], 'BusinessFunction', str]] = Field(
        default=None,
        description="The business function (e.g. sell, lease, repair, dispose) of the offer or component"
     "of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.",
    )
    typeOfGood: Optional[Union[List[Union['Product', 'Service', str]], 'Product', 'Service', str]] = Field(
        default=None,
        description="The product that this structured value is referring to.",
    )
    unitText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",
    )
    unitCode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    amountOfThisGood: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        default=None,
        description="The quantity of the goods included in the offer.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.BusinessFunction import BusinessFunction
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Number import Number
