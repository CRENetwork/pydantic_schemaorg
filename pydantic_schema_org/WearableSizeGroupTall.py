from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupTall(WearableSizeGroupEnumeration):
    """Size group \"Tall\" for wearables.

    See https://schema.org/WearableSizeGroupTall.

    """

    locals().update({"@type": Field("WearableSizeGroupTall", const=True)})


WearableSizeGroupTall.update_forward_refs()
