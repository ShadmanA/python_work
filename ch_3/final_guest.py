guest_list = ['Jay-Z', 'Johnny Depp', 'Robert Downey Jr.', 'Natalie Portman']

guest_raincheck = guest_list.pop(0)
new_guest ='Snoop Dogg' 
guest_list.insert(0, new_guest)

print(f"Uh oh, it looks like {guest_raincheck} cannot make it.")
print(f"Do not worry, we will be joined by {new_guest}.")

for i in guest_list:
    print(f"Don't worry {i}, the dinner party is still happening.")

print("We're in luck! The diner has upgraded our table!")

guest_list.insert(0, 'Keanu Reeves')
guest_list.insert(2, 'Jason Momoa')
guest_list.insert(len(guest_list), 'Princess Diana')

for i in guest_list:
    print(f"Please provide a warm welcome to {i}!")

print("The restaurant found out my tax bracket, and demoted me to a table for three.")

popped_guest = guest_list.pop(0)
print(f"Sorry {popped_guest}, you were removed from the list.")
popped_guest = guest_list.pop(0)
print(f"Sorry {popped_guest}, you were removed from the list.")
popped_guest = guest_list.pop(0)
print(f"Sorry {popped_guest}, you were removed from the list.")
popped_guest = guest_list.pop(2)
print(f"Sorry {popped_guest}, you were removed from the list.")
popped_guest = guest_list.pop(2)
print(f"Sorry {popped_guest}, you were removed from the list.")

for e in guest_list:
    print(f"Congratulations {e}, the dinner party is still happening for you!")
del guest_list[0]
del guest_list[0]
print(f"{guest_list}")