from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.MedicalIntangible import MedicalIntangible
from pydantic_schema_org.CategoryCode import CategoryCode


class MedicalCode(MedicalIntangible, CategoryCode):
    """A code for a medical entity.

    See https://schema.org/MedicalCode.

    """

    codeValue: Optional[Union[List[str], str]] = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    codingSystem: Optional[Union[List[str], str]] = Field(
        None,
        description="The coding system, e.g. 'ICD-10'.",
    )
    locals().update({"@type": Field("MedicalCode", const=True)})


MedicalCode.update_forward_refs()
