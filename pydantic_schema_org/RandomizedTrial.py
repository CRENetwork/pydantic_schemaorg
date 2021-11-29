from pydantic import Field
from pydantic_schema_org.MedicalTrialDesign import MedicalTrialDesign


class RandomizedTrial(MedicalTrialDesign):
    """A randomized trial design.

    See https://schema.org/RandomizedTrial.

    """

    locals().update({"@type": Field("RandomizedTrial", const=True)})


RandomizedTrial.update_forward_refs()
