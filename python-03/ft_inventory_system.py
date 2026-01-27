import sys


def analyze_inventory(inventory: dict) -> int:
    print("=== Inventory System Analysis ===")
    total = 0
    for key in inventory:
        total += inventory[key]
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")
    return total


def show_inventory(inventory: dict, total: int) -> None:
    print("\n=== Current Inventory ===")
    for key in inventory:
        print(f"{key}: {inventory[key]} units (\
{(inventory[key] / total) * 100 :.1f}%)")


def get_item(item: str) -> int:
    return inventory[item]


def inventory_statistic(inventory: dict) -> None:
    most = max(inventory, key=get_item)
    least = min(inventory, key=get_item)
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most} ({inventory.get(most)} units)")
    print(f"Least abundant: {least} ({inventory.get(least)} unit)")


def classify_inv(inventory: dict) -> None:
    moderate = dict()
    scarce = dict()
    abundant = dict()
    print("\n=== Item Categories ===")
    for key, value in inventory.items():
        if inventory[key] > 10:
            abundant[key] = value
        elif inventory[key] >= 5:
            moderate[key] = value
        else:
            scarce[key] = value
    print(f"Abundant: {abundant}") if abundant else None
    print(f"Moderate: {moderate}") if moderate else None
    print(f"Scarce: {scarce}") if scarce else None


def manage_inventory(inventory: dict) -> None:
    restock = [key for key in inventory.keys() if inventory[key] < 2]
    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock}") if restock else print("")


def inventory_properties(inventory: dict, item: str):
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {str(inventory.keys())[10:-1]}")
    print(f"Dictionary values: {str(inventory.values())[12:-1]}")
    print(f"Sample lookup - '{item}' in inventory: {item in inventory}")


if __name__ == "__main__":
    inventory = dict()
    for arg in sys.argv:
        pair = arg.split(":")
        if len(pair) == 2:
            try:
                if not pair[0]:
                    raise ValueError
                inventory.update({pair[0]: int(pair[1])})
                if inventory[pair[0]] < 0:
                    inventory[pair[0]]
                    print("cannot have negative number of something")
            except ValueError:
                print("invalid item detected!! could not add item \
to inventory")
    total = analyze_inventory(inventory)
    show_inventory(inventory, total)
    try:
        inventory_statistic(inventory)
    except ValueError:
        print("empty inventory")
    classify_inv(inventory)
    manage_inventory(inventory)
    inventory_properties(inventory, "coffee")
