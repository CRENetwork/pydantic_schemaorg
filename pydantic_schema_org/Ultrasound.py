from pydantic import Field
from pydantic_schema_org.MedicalImagingTechnique import MedicalImagingTechnique


class Ultrasound(MedicalImagingTechnique):
    """Ultrasound imaging.

    See https://schema.org/Ultrasound.

    """

    locals().update({"@type": Field("Ultrasound", const=True)})


Ultrasound.update_forward_refs()
