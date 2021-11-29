from pydantic import Field
from pydantic_schema_org.MenuSection import MenuSection
from typing import Any, Optional, Union, List
from pydantic_schema_org.MenuItem import MenuItem
from pydantic_schema_org.CreativeWork import CreativeWork


class Menu(CreativeWork):
    """A structured representation of food or drink items available from a FoodEstablishment.

    See https://schema.org/Menu.

    """

    hasMenuSection: Optional[Union[List[MenuSection], MenuSection]] = Field(
        None,
        description="A subgrouping of the menu (by dishes, course, serving time period, etc.).",
    )
    hasMenuItem: Optional[Union[List[MenuItem], MenuItem]] = Field(
        None,
        description="A food or drink item contained in a menu or menu section.",
    )
    locals().update({"@type": Field("Menu", const=True)})


Menu.update_forward_refs()
