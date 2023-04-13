from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("manteiga")

    assert hash(ingredient1) == hash(ingredient1)
    assert hash(ingredient1) != hash(ingredient2)

    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2

    assert repr(ingredient1) == "Ingredient('bacon')"

    assert ingredient1.name == "bacon"

    assert ingredient1.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
