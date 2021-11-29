from pydantic import Field
from pydantic_schema_org.MedicalTrialDesign import MedicalTrialDesign


class InternationalTrial(MedicalTrialDesign):
    """An international trial.

    See https://schema.org/InternationalTrial.

    """

    locals().update({"@type": Field("InternationalTrial", const=True)})


InternationalTrial.update_forward_refs()
