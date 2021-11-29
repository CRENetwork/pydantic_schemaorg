from pydantic import Field
from pydantic_schema_org.StatusEnumeration import StatusEnumeration


class ReservationStatusType(StatusEnumeration):
    """Enumerated status values for Reservation.

    See https://schema.org/ReservationStatusType.

    """

    locals().update({"@type": Field("ReservationStatusType", const=True)})


ReservationStatusType.update_forward_refs()
