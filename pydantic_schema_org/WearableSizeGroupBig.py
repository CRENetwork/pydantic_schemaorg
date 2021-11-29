from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupBig(WearableSizeGroupEnumeration):
    """Size group \"Big\" for wearables.

    See https://schema.org/WearableSizeGroupBig.

    """

    locals().update({"@type": Field("WearableSizeGroupBig", const=True)})


WearableSizeGroupBig.update_forward_refs()
