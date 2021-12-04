# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+" "+k+"(s)")
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):

    for l in addedItems:
        if l in inventory:
            inventory[l] += 1
        else:
            inventory[l] = 1

    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(addToInventory(stuff, dragonLoot))

