Ex="Exercise No : "
Line="--------------------------------------"
# Exercise 3-1: Names
names = ["Alice", "Bob", "Charlie"]
print({Ex} 3-1 )
print(names[0])
print(names[1])
print(names[2])
print({Line})
# Exercise 3-2: Greetings
print({Ex} 3-2 )
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}! How are you today?")
print({Line})
# Exercise 3-3: Your Own List
print({Ex} 3-3 )
transportation_modes = ["motorcycle", "car", "bicycle", "train"]
for mode in transportation_modes:
    print(f"I would like to own a {mode}.")
print({Line})
# Exercise 3-4: Guest List
print({Ex} 3-4 )
guests = ["Albert Einstein", "Isaac Newton", "Marie Curie"]
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")
print({Line})
# Exercise 3-5: Changing Guest List
print({Ex} 3-5 )
guests = ["Albert Einstein", "Isaac Newton", "Marie Curie"]
# One guest can't make it
cannot_make = guests[1]
guests.remove(cannot_make)
print(f"Sorry, {cannot_make} can't make it to the dinner.")
guests.append("Nikola Tesla")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")
print({Line})
# Exercise 3-6: More Guests
print({Ex} 3-6 )
guests = ["Albert Einstein", "Isaac Newton", "Marie Curie"]
print("\nI found a bigger table, so now I can invite more people!")
guests.insert(0, "Charles Darwin")
guests.insert(2, "Ada Lovelace")
guests.append("Alan Turing")
for guest in guests:
    print(f"Dear {guest}, I would like to invite you to dinner.")
print({Line})
# Exercise 3-7: Shrinking Guest List
print({Ex} 3-7 )
guests = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin", "Ada Lovelace", "Alan Turing"]
print("\nUnfortunately, I can only invite two people to dinner now.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can no longer invite you.")
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Empty the guest list
del guests[:]
print("\nMy guest list is now empty:", guests)
print({Line})
# Exercise 3-8: Seeing the World
print({Ex} 3-8 )
places = ["Paris", "Tokyo", "New York", "Sydney", "Rio de Janeiro"]
print("\nOriginal list:", places)

# Sorted (alphabetical order)
print("\nAlphabetical order:", sorted(places))

# Show the list is still in its original order
print("Original list again:", places)

# Sorted (reverse-alphabetical order)
print("\nReverse-alphabetical order:", sorted(places, reverse=True))

# Show the list is still in its original order
print("Original list again:", places)

# Reverse the list
places.reverse()
print("\nReversed list:", places)

# Reverse back to the original order
places.reverse()
print("\nReversed back to original:", places)

# Sort alphabetically and reverse-alphabetically
places.sort()
print("\nSorted in alphabetical order:", places)

places.sort(reverse=True)
print("\nSorted in reverse-alphabetical order:", places)
print({Line})
# Exercise 3-9: Dinner Guests
print({Ex} 3-9 )
guests = ["Albert Einstein", "Isaac Newton", "Marie Curie"]
print(f"\nNumber of guests invited: {len(guests)}")
print({Line})
# Exercise 3-10: Every Function
print({Ex} 3-10 )
things = ["mountain", "river", "country", "city", "language"]
print("\nList of things:", things)
print({Line})
# Using functions from the list
print(f"First item: {things[0]}")
print(f"Last item: {things[-1]}")
things.append("ocean")
print("After appending 'ocean':", things)

things.sort()
print("After sorting alphabetically:", things)

things.reverse()
print("After reversing:", things)

# Exercise 3-11: Intentional Error
print({Ex} 3-11 )
# Let's create an index error
# Example: Accessing an index that doesn't exist
try:
    print(things[10])  # This will cause an IndexError because there aren't 11 elements
except IndexError:
    print("IndexError: Tried to access an index that doesn't exist.")

# Correcting the error
print("Correct index:", things[0])  # Now we're accessing a valid index
print({Line})