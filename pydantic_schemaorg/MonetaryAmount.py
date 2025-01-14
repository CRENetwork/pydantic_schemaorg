from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class MonetaryAmount(StructuredValue):
    """A monetary value or range. This type can be used to describe an amount of money such as $50"
     "USD, or a range as in describing a bank account being suitable for a balance between £1,000"
     "and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]]"
     "Types to describe the price of an Offer, Invoice, etc.

    See: https://schema.org/MonetaryAmount
    Model depth: 4
    """

    type_: str = Field(default="MonetaryAmount", alias="@type", const=True)
    value: Optional[
        Union[
            List[
                Union[
                    StrictInt,
                    StrictFloat,
                    "Number",
                    str,
                    "Text",
                    StrictBool,
                    "Boolean",
                    "StructuredValue",
                ]
            ],
            StrictInt,
            StrictFloat,
            "Number",
            str,
            "Text",
            StrictBool,
            "Boolean",
            "StructuredValue",
        ]
    ] = Field(
        default=None,
        description="The value of the quantitative value or property value node. * For [[QuantitativeValue]]"
        "and [[MonetaryAmount]], the recommended type for values is 'Number'. * For [[PropertyValue]],"
        "it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. * Use values from 0123456789"
        "(Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
        "similar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to"
        "indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    currency: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
        'currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker'
        "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies,"
        'e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'
        '(LETS) and other currency types, e.g. "Ithaca HOUR".',
    )
    validThrough: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
        "or a period of opening hours.",
    )
    maxValue: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The upper value of some characteristic or property.",
    )
    validFrom: Optional[
        Union[
            List[Union[datetime, "DateTime", date, "Date", str]],
            datetime,
            "DateTime",
            date,
            "Date",
            str,
        ]
    ] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    minValue: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The lower value of some characteristic or property.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
