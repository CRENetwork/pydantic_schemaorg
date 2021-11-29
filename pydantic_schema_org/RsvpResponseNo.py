from pydantic import Field
from pydantic_schema_org.RsvpResponseType import RsvpResponseType


class RsvpResponseNo(RsvpResponseType):
    """The invitee will not attend.

    See https://schema.org/RsvpResponseNo.

    """

    locals().update({"@type": Field("RsvpResponseNo", const=True)})


RsvpResponseNo.update_forward_refs()
