from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Nerve(AnatomicalStructure):
    """A common pathway for the electrochemical nerve impulses that are transmitted along"
     "each of the axons.

    See: https://schema.org/Nerve
    Model depth: 4
    """

    type_: str = Field(default="Nerve", alias="@type", const=True)
    nerveMotor: Optional[Union[List[Union["Muscle", str]], "Muscle", str]] = Field(
        default=None,
        description="The neurological pathway extension that involves muscle control.",
    )
    branch: Optional[
        Union[List[Union["AnatomicalStructure", str]], "AnatomicalStructure", str]
    ] = Field(
        default=None,
        description="The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].",
    )
    sourcedFrom: Optional[
        Union[List[Union["BrainStructure", str]], "BrainStructure", str]
    ] = Field(
        default=None,
        description="The neurological pathway that originates the neurons.",
    )
    sensoryUnit: Optional[
        Union[
            List[Union["AnatomicalStructure", "SuperficialAnatomy", str]],
            "AnatomicalStructure",
            "SuperficialAnatomy",
            str,
        ]
    ] = Field(
        default=None,
        description="The neurological pathway extension that inputs and sends information to the brain or"
        "spinal cord.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.Muscle import Muscle
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.BrainStructure import BrainStructure
    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
