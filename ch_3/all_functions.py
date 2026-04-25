menu = ['Butter Chicken', 'Palau', 'Mutton Chops', 'Paneer', 'Tempura']
for u in menu:
    print(f"{u}")

menu_alter = menu.pop()
new_item ='Cabbage Pakora' 
menu.insert(0, new_item)

print(f"We can't have {menu_alter}.")
print(f"Do not worry, we can have {new_item} instead.")
remove_item = "Mutton Chops"
menu.remove(remove_item)
print(f"Oops, the {remove_item} went bad.")
for u in menu:
    print(f"{u}")

print("Got room for Dessert?")

menu.insert(0, "Ice Cream")
menu.append("Vanilla Cake")
print(sorted(menu))
print(sorted(menu, reverse=True))
menu.reverse()
print(menu)
menu.reverse() #Function with no return value
print(menu)
menu.sort() #Function with no return value
print(menu)
menu.sort(reverse=True) #Function with no return value
print(menu)
print(f"I can have {len(menu)} items!")
eaten = menu.pop(0)
print(f"Mmm, that {eaten} was delicious!")
eaten = menu.pop(0)
print(f"Mmm, that {eaten} was delicious!")
eaten = menu.pop(0)
print(f"Mmm, that {eaten} was delicious!")
eaten = menu.pop(0)
print(f"Mmm, that {eaten} was delicious!")
eaten = menu.pop(0)
print(f"Mmm, that {eaten} was delicious!")
for u in menu:
    print(f"I have yet to try the {u}.")
del menu[0]
print("I'm stuffed, and it looks like they closed the restaurant for tonight.")
print(menu)