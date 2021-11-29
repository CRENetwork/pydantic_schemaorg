from pydantic import Field
from pydantic_schema_org.StatusEnumeration import StatusEnumeration


class GameServerStatus(StatusEnumeration):
    """Status of a game server.

    See https://schema.org/GameServerStatus.

    """

    locals().update({"@type": Field("GameServerStatus", const=True)})


GameServerStatus.update_forward_refs()
