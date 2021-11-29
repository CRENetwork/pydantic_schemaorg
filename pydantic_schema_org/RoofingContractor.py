from pydantic import Field
from pydantic_schema_org.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """A roofing contractor.

    See https://schema.org/RoofingContractor.

    """

    locals().update({"@type": Field("RoofingContractor", const=True)})


RoofingContractor.update_forward_refs()
