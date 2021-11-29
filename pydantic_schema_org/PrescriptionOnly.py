from pydantic import Field
from pydantic_schema_org.DrugPrescriptionStatus import DrugPrescriptionStatus


class PrescriptionOnly(DrugPrescriptionStatus):
    """Available by prescription only.

    See https://schema.org/PrescriptionOnly.

    """

    locals().update({"@type": Field("PrescriptionOnly", const=True)})


PrescriptionOnly.update_forward_refs()
