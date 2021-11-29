from pydantic import Field
from pydantic_schema_org.Store import Store


class FurnitureStore(Store):
    """A furniture store.

    See https://schema.org/FurnitureStore.

    """

    locals().update({"@type": Field("FurnitureStore", const=True)})


FurnitureStore.update_forward_refs()
