from pydantic import Field
from pydantic_schema_org.Store import Store


class ToyStore(Store):
    """A toy store.

    See https://schema.org/ToyStore.

    """

    locals().update({"@type": Field("ToyStore", const=True)})


ToyStore.update_forward_refs()
