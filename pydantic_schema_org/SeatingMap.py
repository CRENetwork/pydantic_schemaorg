from pydantic import Field
from pydantic_schema_org.MapCategoryType import MapCategoryType


class SeatingMap(MapCategoryType):
    """A seating map.

    See https://schema.org/SeatingMap.

    """

    locals().update({"@type": Field("SeatingMap", const=True)})


SeatingMap.update_forward_refs()
