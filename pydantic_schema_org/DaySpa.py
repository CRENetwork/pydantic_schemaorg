from pydantic import Field
from pydantic_schema_org.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """A day spa.

    See https://schema.org/DaySpa.

    """

    locals().update({"@type": Field("DaySpa", const=True)})


DaySpa.update_forward_refs()
