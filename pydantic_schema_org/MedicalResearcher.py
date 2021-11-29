from pydantic import Field
from pydantic_schema_org.MedicalAudienceType import MedicalAudienceType


class MedicalResearcher(MedicalAudienceType):
    """Medical researchers.

    See https://schema.org/MedicalResearcher.

    """

    locals().update({"@type": Field("MedicalResearcher", const=True)})


MedicalResearcher.update_forward_refs()
