from pydantic import Field
from pydantic_schema_org.GovernmentOffice import GovernmentOffice


class PostOffice(GovernmentOffice):
    """A post office.

    See https://schema.org/PostOffice.

    """

    locals().update({"@type": Field("PostOffice", const=True)})


PostOffice.update_forward_refs()
