from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schema_org.Comment import Comment
from pydantic_schema_org.RsvpResponseType import RsvpResponseType
from pydantic_schema_org.InformAction import InformAction


class RsvpAction(InformAction):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    See https://schema.org/RsvpAction.

    """

    additionalNumberOfGuests: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="If responding yes, the number of guests who will attend in addition to the invitee.",
    )
    comment: Optional[Union[List[Comment], Comment]] = Field(
        None,
        description="Comments, typically from users.",
    )
    rsvpResponse: Optional[Union[List[RsvpResponseType], RsvpResponseType]] = Field(
        None,
        description="The response (yes, no, maybe) to the RSVP.",
    )
    locals().update({"@type": Field("RsvpAction", const=True)})


RsvpAction.update_forward_refs()
