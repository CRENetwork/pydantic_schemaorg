from pydantic import Field
from pydantic_schema_org.StatusEnumeration import StatusEnumeration


class ActionStatusType(StatusEnumeration):
    """The status of an Action.

    See https://schema.org/ActionStatusType.

    """

    locals().update({"@type": Field("ActionStatusType", const=True)})


ActionStatusType.update_forward_refs()
