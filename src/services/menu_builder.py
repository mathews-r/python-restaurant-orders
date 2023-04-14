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
        list_menu = list()

        for dish in self.menu_data.dishes:
            dish_menu = dict()

            if restriction not in dish.get_restrictions():
                dish_menu["dish_name"] = dish.name
                dish_menu["ingredients"] = [
                    ingredient for ingredient in dish.get_ingredients()
                ]
                dish_menu["price"] = dish.price
                dish_menu["restrictions"] = dish.get_restrictions()
                list_menu.append(dish_menu)

        return pd.DataFrame(list_menu)
