from pydantic import Field
from pydantic_schema_org.FoodEstablishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """An ice cream shop.

    See https://schema.org/IceCreamShop.

    """

    locals().update({"@type": Field("IceCreamShop", const=True)})


IceCreamShop.update_forward_refs()
