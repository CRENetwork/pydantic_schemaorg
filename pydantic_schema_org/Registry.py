from pydantic import Field
from pydantic_schema_org.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Registry(MedicalObservationalStudyDesign):
    """A registry-based study design.

    See https://schema.org/Registry.

    """

    locals().update({"@type": Field("Registry", const=True)})


Registry.update_forward_refs()
