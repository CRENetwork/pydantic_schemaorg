from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.Product import Product


class SomeProducts(Product):
    """A placeholder for multiple similar products of the same kind.

    See https://schema.org/SomeProducts.

    """

    inventoryLevel: Any = Field(
        None,
        description="The current approximate inventory level for the item or items.",
    )
    locals().update({"@type": Field("SomeProducts", const=True)})


SomeProducts.update_forward_refs()
