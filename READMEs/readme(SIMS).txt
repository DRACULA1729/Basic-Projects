This project is a simple inventory management system implemented in Python. The system allows users to manage a collection of items, including adding new items, updating the quantity of existing items, and displaying the current inventory.

Key Components:
Items Class:

This class represents an individual item in the inventory.
It has three attributes: name, price, and quantity.
The displayItems method prints the details of the item in a formatted manner.
Inventory Class:

This class manages a collection of Items.
It has a list called items to store all the items in the inventory.
The addItems method allows adding new items to the inventory. It checks if an item with the same name already exists to prevent duplicates.
The update_quantity method allows updating the quantity of an existing item. It checks if the item exists and modifies its quantity accordingly.
The displayItems method iterates over the list of items and prints each item’s details.
Usage:

An instance of the Inventory class is created.
Several items (like pencil, pen, etc.) are added to the inventory using the addItems method.
Finally, the displayItems method is called to print out all items currently in the inventory.
Potential Improvements:
The addItems method has a bug where it does not correctly check for item existence. The comparison if item == item.name should be corrected to check against item.name.
The update_quantity method uses the wrong indexing to access items. It should directly modify the quantity attribute of the found item instead of trying to index into the list with name.
Additional features could include removing items, searching for specific items, or saving/loading the inventory to/from a file.
Overall, this project serves as a foundational example of how to manage an inventory system programmatically, providing basic functionalities that can be expanded upon.