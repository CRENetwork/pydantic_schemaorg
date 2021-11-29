from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.PriceSpecification import PriceSpecification
from decimal import Decimal
from pydantic_schema_org.Intangible import Intangible


class HealthPlanCostSharingSpecification(Intangible):
    """A description of costs to the patient under a given network or formulary.

    See https://schema.org/HealthPlanCostSharingSpecification.

    """

    healthPlanCoinsuranceOption: Optional[Union[List[str], str]] = Field(
        None,
        description="Whether the coinsurance applies before or after deductible, etc. TODO: Is this a closed"
     "set?",
    )
    healthPlanPharmacyCategory: Optional[Union[List[str], str]] = Field(
        None,
        description="The category or type of pharmacy associated with this cost sharing.",
    )
    healthPlanCopay: Optional[Union[List[PriceSpecification], PriceSpecification]] = Field(
        None,
        description="Whether The copay amount.",
    )
    healthPlanCopayOption: Optional[Union[List[str], str]] = Field(
        None,
        description="Whether the copay is before or after deductible, etc. TODO: Is this a closed set?",
    )
    healthPlanCoinsuranceRate: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Whether The rate of coinsurance expressed as a number between 0.0 and 1.0.",
    )
    locals().update({"@type": Field("HealthPlanCostSharingSpecification", const=True)})


HealthPlanCostSharingSpecification.update_forward_refs()
