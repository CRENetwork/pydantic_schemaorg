from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class SelfStorage(LocalBusiness):
    """A self-storage facility.

    See https://schema.org/SelfStorage.

    """

    locals().update({"@type": Field("SelfStorage", const=True)})


SelfStorage.update_forward_refs()
