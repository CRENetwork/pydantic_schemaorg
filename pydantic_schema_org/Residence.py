from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.Place import Place


class Residence(Place):
    """The place where a person lives.

    See https://schema.org/Residence.

    """

    accommodationFloorPlan: Any = Field(
        None,
        description="A floorplan of some [[Accommodation]].",
    )
    locals().update({"@type": Field("Residence", const=True)})


Residence.update_forward_refs()
