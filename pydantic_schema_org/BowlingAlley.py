from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation


class BowlingAlley(SportsActivityLocation):
    """A bowling alley.

    See https://schema.org/BowlingAlley.

    """

    locals().update({"@type": Field("BowlingAlley", const=True)})


BowlingAlley.update_forward_refs()
