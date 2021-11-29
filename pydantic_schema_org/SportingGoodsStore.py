from pydantic import Field
from pydantic_schema_org.Store import Store


class SportingGoodsStore(Store):
    """A sporting goods store.

    See https://schema.org/SportingGoodsStore.

    """

    locals().update({"@type": Field("SportingGoodsStore", const=True)})


SportingGoodsStore.update_forward_refs()
