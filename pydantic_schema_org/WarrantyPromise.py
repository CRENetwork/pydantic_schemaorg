from pydantic import Field
from pydantic_schema_org.WarrantyScope import WarrantyScope
from typing import Any, Optional, Union, List
from pydantic_schema_org.QuantitativeValue import QuantitativeValue
from pydantic_schema_org.StructuredValue import StructuredValue


class WarrantyPromise(StructuredValue):
    """A structured value representing the duration and scope of services that will be provided"
     "to a customer free of charge in case of a defect or malfunction of a product.

    See https://schema.org/WarrantyPromise.

    """

    warrantyScope: Optional[Union[List[WarrantyScope], WarrantyScope]] = Field(
        None,
        description="The scope of the warranty promise.",
    )
    durationOfWarranty: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="The duration of the warranty promise. Common unitCode values are ANN for year, MON for"
     "months, or DAY for days.",
    )
    locals().update({"@type": Field("WarrantyPromise", const=True)})


WarrantyPromise.update_forward_refs()
