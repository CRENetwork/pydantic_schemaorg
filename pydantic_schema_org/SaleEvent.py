from pydantic import Field
from pydantic_schema_org.Event import Event


class SaleEvent(Event):
    """Event type: Sales event.

    See https://schema.org/SaleEvent.

    """

    locals().update({"@type": Field("SaleEvent", const=True)})


SaleEvent.update_forward_refs()
