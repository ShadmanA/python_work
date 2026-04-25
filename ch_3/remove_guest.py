guest_list = ['Jay-Z', 'Johnny Depp', 'Robert Downey Jr.', 'Natalie Portman']

guest_raincheck = guest_list.pop(0)
new_guest ='Snoop Dogg' 
guest_list.insert(0, new_guest)

print(f"Uh oh, it looks like {guest_raincheck} cannot make it.")
print(f"Do not worry, we will be joined by {new_guest}.")

for i in guest_list:
    print(f"Don't worry {i}, the dinner party is still happening.")