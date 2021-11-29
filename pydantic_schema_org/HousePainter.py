from pydantic import Field
from pydantic_schema_org.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """A house painting service.

    See https://schema.org/HousePainter.

    """

    locals().update({"@type": Field("HousePainter", const=True)})


HousePainter.update_forward_refs()
