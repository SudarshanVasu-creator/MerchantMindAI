from app.tools.inventory_loader import load_inventory

inventory = load_inventory()

print(len(inventory))
print(inventory[0])