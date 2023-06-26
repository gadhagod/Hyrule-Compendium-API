from flask import Response
from rockset.query import FieldEqQuery
from typing import (
    Literal, 
    TypedDict, 
    Optional,
    Union,
    Set,
    Dict
)

Where = FieldEqQuery
VersionString = Literal['v1', 'v2', 'v3']
StandardCategoryName = Literal['creatures', 'equipment', 'materials', 'monsters', 'treasure']
DlcCategoryName = Literal['master_mode']
BaseEntrySelect = Literal['drops', 'cooking_effect', 'hearts_recovered', 'attack', 'defense']
EntrySelectsOptions = Dict[StandardCategoryName, Set[BaseEntrySelect]]
EntrySelects = Set[BaseEntrySelect]
EntryImage = Response

class EntryData(TypedDict, total=False):
    category: Union[StandardCategoryName, DlcCategoryName]
    common_locations: list[str]
    description: str
    id: int
    name: str
    image: str
    drops: Optional[list[str]]
    hearts_recovered: Optional[float]
    cooking_effect: Optional[str]
    attack: Optional[int]
    defense: Optional[int]

class CreaturesCategoryData(TypedDict, total=False):
    food: list[EntryData]
    non_food: list[EntryData] 

CategoryData = Union[list[EntryData], CreaturesCategoryData]