from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupGirls(WearableSizeGroupEnumeration):
    """Size group \"Girls\" for wearables.

    See https://schema.org/WearableSizeGroupGirls.

    """

    locals().update({"@type": Field("WearableSizeGroupGirls", const=True)})


WearableSizeGroupGirls.update_forward_refs()
