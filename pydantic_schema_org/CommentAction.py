from pydantic import Field
from pydantic_schema_org.Comment import Comment
from typing import Any, Optional, Union, List
from pydantic_schema_org.CommunicateAction import CommunicateAction


class CommentAction(CommunicateAction):
    """The act of generating a comment about a subject.

    See https://schema.org/CommentAction.

    """

    resultComment: Optional[Union[List[Comment], Comment]] = Field(
        None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )
    locals().update({"@type": Field("CommentAction", const=True)})


CommentAction.update_forward_refs()
