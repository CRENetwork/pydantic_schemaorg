from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import datetime


from pydantic import Field
from pydantic_schemaorg.Trip import Trip


class Flight(Trip):
    """An airline flight.

    See: https://schema.org/Flight
    Model depth: 4
    """

    type_: str = Field(default="Flight", alias="@type", const=True)
    seller: Optional[
        Union[List[Union["Organization", "Person", str]], "Organization", "Person", str]
    ] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
        "also be a provider.",
    )
    boardingPolicy: Optional[
        Union[List[Union["BoardingPolicyType", str]], "BoardingPolicyType", str]
    ] = Field(
        default=None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",
    )
    webCheckinTime: Optional[
        Union[List[Union[datetime, "DateTime", str]], datetime, "DateTime", str]
    ] = Field(
        default=None,
        description="The time when a passenger can check into the flight online.",
    )
    arrivalAirport: Optional[
        Union[List[Union["Airport", str]], "Airport", str]
    ] = Field(
        default=None,
        description="The airport where the flight terminates.",
    )
    estimatedFlightDuration: Optional[
        Union[List[Union[str, "Text", "Duration"]], str, "Text", "Duration"]
    ] = Field(
        default=None,
        description="The estimated time the flight will take.",
    )
    carrier: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    departureAirport: Optional[
        Union[List[Union["Airport", str]], "Airport", str]
    ] = Field(
        default=None,
        description="The airport where the flight originates.",
    )
    mealService: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Description of the meals that will be provided or available for purchase.",
    )
    flightDistance: Optional[
        Union[List[Union[str, "Text", "Distance"]], str, "Text", "Distance"]
    ] = Field(
        default=None,
        description="The distance of the flight.",
    )
    departureGate: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Identifier of the flight's departure gate.",
    )
    departureTerminal: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Identifier of the flight's departure terminal.",
    )
    arrivalTerminal: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Identifier of the flight's arrival terminal.",
    )
    flightNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The unique identifier for a flight including the airline IATA code. For example, if describing"
        "United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.",
    )
    arrivalGate: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Identifier of the flight's arrival gate.",
    )
    aircraft: Optional[
        Union[List[Union[str, "Text", "Vehicle"]], str, "Text", "Vehicle"]
    ] = Field(
        default=None,
        description='The kind of aircraft (e.g., "Boeing 747").',
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Airport import Airport
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.Vehicle import Vehicle
