from pydantic import Field
from pydantic_schema_org.Comment import Comment
from typing import Any, Optional, Union, List
from pydantic_schema_org.CommunicateAction import CommunicateAction


class ReplyAction(CommunicateAction):
    """The act of responding to a question/message asked/sent by the object. Related to [[AskAction]]"
     "Related actions: * [[AskAction]]: Appears generally as an origin of a ReplyAction.

    See https://schema.org/ReplyAction.

    """

    resultComment: Optional[Union[List[Comment], Comment]] = Field(
        None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )
    locals().update({"@type": Field("ReplyAction", const=True)})


ReplyAction.update_forward_refs()
