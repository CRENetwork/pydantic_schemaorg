from pydantic import Field
from pydantic_schema_org.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schema_org.AchieveAction import AchieveAction


class LoseAction(AchieveAction):
    """The act of being defeated in a competitive activity.

    See https://schema.org/LoseAction.

    """

    winner: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A sub property of participant. The winner of the action.",
    )
    locals().update({"@type": Field("LoseAction", const=True)})


LoseAction.update_forward_refs()
