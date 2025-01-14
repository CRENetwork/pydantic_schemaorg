from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.HowTo import HowTo


class Recipe(HowTo):
    """A recipe. For dietary restrictions covered by the recipe, a few common restrictions"
     "are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used"
     "to add more detail.

    See: https://schema.org/Recipe
    Model depth: 4
    """

    type_: str = Field(default="Recipe", alias="@type", const=True)
    recipeYield: Optional[
        Union[
            List[Union[str, "Text", "QuantitativeValue"]],
            str,
            "Text",
            "QuantitativeValue",
        ]
    ] = Field(
        default=None,
        description="The quantity produced by the recipe (for example, number of people served, number of"
        "servings, etc).",
    )
    nutrition: Optional[
        Union[List[Union["NutritionInformation", str]], "NutritionInformation", str]
    ] = Field(
        default=None,
        description="Nutrition information about the recipe or menu item.",
    )
    cookingMethod: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The method of cooking, such as Frying, Steaming, ...",
    )
    suitableForDiet: Optional[
        Union[List[Union["RestrictedDiet", str]], "RestrictedDiet", str]
    ] = Field(
        default=None,
        description="Indicates a dietary restriction or guideline for which this recipe or menu item is suitable,"
        "e.g. diabetic, halal etc.",
    )
    cookTime: Optional[Union[List[Union["Duration", str]], "Duration", str]] = Field(
        default=None,
        description="The time it takes to actually cook the dish, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    ingredients: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A single ingredient used in the recipe, e.g. sugar, flour or garlic.",
    )
    recipeCuisine: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The cuisine of the recipe (for example, French or Ethiopian).",
    )
    recipeInstructions: Optional[
        Union[
            List[Union[str, "Text", "ItemList", "CreativeWork"]],
            str,
            "Text",
            "ItemList",
            "CreativeWork",
        ]
    ] = Field(
        default=None,
        description="A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered"
        "list with HowToStep and/or HowToSection items.",
    )
    recipeIngredient: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A single ingredient used in the recipe, e.g. sugar, flour or garlic.",
    )
    recipeCategory: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The category of the recipe—for example, appetizer, entree, etc.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.NutritionInformation import NutritionInformation
    from pydantic_schemaorg.RestrictedDiet import RestrictedDiet
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.CreativeWork import CreativeWork
