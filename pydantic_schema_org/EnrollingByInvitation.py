from pydantic import Field
from pydantic_schema_org.MedicalStudyStatus import MedicalStudyStatus


class EnrollingByInvitation(MedicalStudyStatus):
    """Enrolling participants by invitation only.

    See https://schema.org/EnrollingByInvitation.

    """

    locals().update({"@type": Field("EnrollingByInvitation", const=True)})


EnrollingByInvitation.update_forward_refs()
