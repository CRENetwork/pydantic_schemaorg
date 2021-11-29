from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class EventVenue(CivicStructure):
    """An event venue.

    See https://schema.org/EventVenue.

    """

    locals().update({"@type": Field("EventVenue", const=True)})


EventVenue.update_forward_refs()
