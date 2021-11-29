from pydantic import Field
from pydantic_schema_org.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """A moving company.

    See https://schema.org/MovingCompany.

    """

    locals().update({"@type": Field("MovingCompany", const=True)})


MovingCompany.update_forward_refs()
