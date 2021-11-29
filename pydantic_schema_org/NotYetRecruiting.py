from pydantic import Field
from pydantic_schema_org.MedicalStudyStatus import MedicalStudyStatus


class NotYetRecruiting(MedicalStudyStatus):
    """Not yet recruiting.

    See https://schema.org/NotYetRecruiting.

    """

    locals().update({"@type": Field("NotYetRecruiting", const=True)})


NotYetRecruiting.update_forward_refs()
