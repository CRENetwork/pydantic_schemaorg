from pydantic import Field
from pydantic_schema_org.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """A nail salon.

    See https://schema.org/NailSalon.

    """

    locals().update({"@type": Field("NailSalon", const=True)})


NailSalon.update_forward_refs()
