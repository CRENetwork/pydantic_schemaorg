from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """A business providing entertainment.

    See https://schema.org/EntertainmentBusiness.

    """

    locals().update({"@type": Field("EntertainmentBusiness", const=True)})


EntertainmentBusiness.update_forward_refs()
