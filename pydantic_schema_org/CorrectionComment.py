from pydantic import Field
from pydantic_schema_org.Comment import Comment


class CorrectionComment(Comment):
    """A [[comment]] that corrects [[CreativeWork]].

    See https://schema.org/CorrectionComment.

    """

    locals().update({"@type": Field("CorrectionComment", const=True)})


CorrectionComment.update_forward_refs()
