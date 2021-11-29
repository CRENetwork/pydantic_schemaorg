from pydantic import Field
from pydantic_schema_org.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemEurope(WearableSizeSystemEnumeration):
    """European size system for wearables.

    See https://schema.org/WearableSizeSystemEurope.

    """

    locals().update({"@type": Field("WearableSizeSystemEurope", const=True)})


WearableSizeSystemEurope.update_forward_refs()
