from pydantic import Field
from pydantic_schema_org.QuantitativeValue import QuantitativeValue
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schema_org.ListItem import ListItem


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to to achieve"
     "a result.

    See https://schema.org/HowToItem.

    """

    requiredQuantity: Optional[Union[List[Union[Decimal, str, QuantitativeValue]], Union[Decimal, str, QuantitativeValue]]] = Field(
        None,
        description="The required quantity of the item(s).",
    )
    locals().update({"@type": Field("HowToItem", const=True)})


HowToItem.update_forward_refs()
