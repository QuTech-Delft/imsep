class ShoppingCart:

    def __init__(self) -> None:
        self._items = {
            "shoes": {"cost": 10, "count": 0},
            "fancy_shoes": {"cost": 15, "count": 0},
            "dress": {"cost": 18, "count": 0},
            "hat": {"cost": 6, "count": 0},
            "t_shirt": {"cost": 8, "count": 0}
        }

    def add_item(self, item: str) -> None:
        try:
            self._items[item]["count"] += 1
        except KeyError:
            print("Item is not available.")

    def remove_item(self, item: str) -> None:
        try:
            if self._items[item]["count"]:
                self._items[item]["count"] -= 1
        except KeyError:
            print("Item is not in the shopping cart.")

    def calculate_total(self) -> int:
        return sum([item["cost"] * item["count"] for item in self._items.values()])
