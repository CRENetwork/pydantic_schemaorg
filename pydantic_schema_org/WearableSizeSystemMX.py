from pydantic import Field
from pydantic_schema_org.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemMX(WearableSizeSystemEnumeration):
    """Mexican size system for wearables.

    See https://schema.org/WearableSizeSystemMX.

    """

    locals().update({"@type": Field("WearableSizeSystemMX", const=True)})


WearableSizeSystemMX.update_forward_refs()
