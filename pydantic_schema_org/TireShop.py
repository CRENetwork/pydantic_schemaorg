from pydantic import Field
from pydantic_schema_org.Store import Store


class TireShop(Store):
    """A tire shop.

    See https://schema.org/TireShop.

    """

    locals().update({"@type": Field("TireShop", const=True)})


TireShop.update_forward_refs()
