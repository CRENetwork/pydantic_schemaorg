from pydantic import AnyUrl, Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.LocalBusiness import LocalBusiness


class FinancialService(LocalBusiness):
    """Financial services business.

    See https://schema.org/FinancialService.

    """

    feesAndCommissionsSpecification: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
     "product, or by a financial service organization.",
    )
    locals().update({"@type": Field("FinancialService", const=True)})


FinancialService.update_forward_refs()
