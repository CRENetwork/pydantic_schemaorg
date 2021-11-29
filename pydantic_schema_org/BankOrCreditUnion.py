from pydantic import Field
from pydantic_schema_org.FinancialService import FinancialService


class BankOrCreditUnion(FinancialService):
    """Bank or credit union.

    See https://schema.org/BankOrCreditUnion.

    """

    locals().update({"@type": Field("BankOrCreditUnion", const=True)})


BankOrCreditUnion.update_forward_refs()
