from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class TravelAgency(LocalBusiness):
    """A travel agency.

    See https://schema.org/TravelAgency.

    """

    locals().update({"@type": Field("TravelAgency", const=True)})


TravelAgency.update_forward_refs()
