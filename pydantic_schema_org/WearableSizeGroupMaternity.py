from pydantic import Field
from pydantic_schema_org.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMaternity(WearableSizeGroupEnumeration):
    """Size group \"Maternity\" for wearables.

    See https://schema.org/WearableSizeGroupMaternity.

    """

    locals().update({"@type": Field("WearableSizeGroupMaternity", const=True)})


WearableSizeGroupMaternity.update_forward_refs()
