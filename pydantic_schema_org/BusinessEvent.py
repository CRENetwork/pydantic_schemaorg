from pydantic import Field
from pydantic_schema_org.Event import Event


class BusinessEvent(Event):
    """Event type: Business event.

    See https://schema.org/BusinessEvent.

    """

    locals().update({"@type": Field("BusinessEvent", const=True)})


BusinessEvent.update_forward_refs()
