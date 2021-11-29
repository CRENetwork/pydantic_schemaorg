from pydantic import Field
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class PublicHealth(MedicalBusiness, MedicalSpecialty):
    """Branch of medicine that pertains to the health services to improve and protect community"
     "health, especially epidemiology, sanitation, immunization, and preventive medicine.

    See https://schema.org/PublicHealth.

    """

    locals().update({"@type": Field("PublicHealth", const=True)})


PublicHealth.update_forward_refs()
