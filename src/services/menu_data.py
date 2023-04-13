import csv
from models.dish import Dish

from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, mode="r") as file:
            csv_file = list(csv.DictReader(file, delimiter=","))

            current_dish = Dish(
                csv_file[0]["dish"], float(csv_file[0]["price"])
            )

            current_dish.add_ingredient_dependency(
                Ingredient(csv_file[0]["ingredient"]),
                int(csv_file[0]["recipe_amount"]),
            )

        for row_menu in csv_file[1:]:
            new_dish = Dish(row_menu["dish"], float(row_menu["price"]))
            new_ingredients = Ingredient(row_menu["ingredient"])

            if new_dish == current_dish:
                print(self.dishes, 'if')
                current_dish.add_ingredient_dependency(
                    new_ingredients, int(row_menu["recipe_amount"])
                )
            else:
                print(self.dishes, 'else')
                self.dishes.add(new_dish)
                new_dish.add_ingredient_dependency(
                    new_ingredients, int(row_menu["recipe_amount"])
                )


menu_data = MenuData("data/menu_base_data.csv")

print(menu_data.dishes)
