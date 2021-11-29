from pydantic import Field
from pydantic_schema_org.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemJP(WearableSizeSystemEnumeration):
    """Japanese size system for wearables.

    See https://schema.org/WearableSizeSystemJP.

    """

    locals().update({"@type": Field("WearableSizeSystemJP", const=True)})


WearableSizeSystemJP.update_forward_refs()
