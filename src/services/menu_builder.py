import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        df = pd.read_csv(DATA_PATH)
        dish_menu = dict()
        ingredients = list()

        dishes = df[
            ["dish", "price", "ingredient", "recipe_amount"]
        ].itertuples(index=False)

        for dish in dishes:
            ingredients.append(dish.ingredient)
            if restriction is None:
                dish_menu = {
                    "dish_name": dish.dish,
                    "ingredients": ingredients,
                    "price": dish.price,
                    "restrictions": restriction,
                }
            else:
                dish_menu = {
                    "dish_name": dish.dish,
                    "ingredients": ingredients,
                    "price": dish.price,
                    "restrictions": restriction,
                }
        return pd.DataFrame(dish_menu)


menu = MenuBuilder()
print(menu.get_main_menu())
