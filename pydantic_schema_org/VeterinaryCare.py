from pydantic import Field
from pydantic_schema_org.MedicalOrganization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """A vet's office.

    See https://schema.org/VeterinaryCare.

    """

    locals().update({"@type": Field("VeterinaryCare", const=True)})


VeterinaryCare.update_forward_refs()
