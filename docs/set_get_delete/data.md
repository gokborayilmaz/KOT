---
layout: default
title: Data Operations
nav_order: 3
has_children: false
parent: SET GET DELETE
---

# Set, Get and Delete Data
Previously section we created a database. Now we will learn how to set and get data from database. Let's set a data to database.

```python
from kot import KOT

# Create a database
my_location_db = KOT("locations_of_team_members")
my_image_db = KOT("images_of_team_members")

# Set data
my_location_db.set("Onur", "Sivas")
#my_image_db.set("Onur", file="onur.jpg", dont_remove_original_file=True)

# Get data
print(my_location_db.get("Onur"))
#print(my_image_db.get("Onur"))

# Delete data
my_location_db.delete("Onur")
#my_image_db.delete("Onur")
```

def my_function():
    print("Hi how are you")

my_location_db.active(my_function)

my_location_db.get("my_function")()


Output:

```console
Sivas
Hi how are you
```
