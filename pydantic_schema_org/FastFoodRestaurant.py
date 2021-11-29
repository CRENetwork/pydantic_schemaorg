from pydantic import Field
from pydantic_schema_org.FoodEstablishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """A fast-food restaurant.

    See https://schema.org/FastFoodRestaurant.

    """

    locals().update({"@type": Field("FastFoodRestaurant", const=True)})


FastFoodRestaurant.update_forward_refs()
