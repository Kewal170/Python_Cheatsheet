# List manipulation
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print("After appending 6:", my_list)

# Remove an element from the list
my_list.remove(3)
print("After removing 3:", my_list)

# Access elements by index
print("Element at index 2:", my_list[2])

# String manipulation
my_string = "Hello, World!"

# Split the string into a list of words
words = my_string.split()
print("Split string into words:", words)

# Join elements of a list into a single string
new_string = "-".join(words)
print("Joined words with '-':", new_string)

# Convert string to uppercase
upper_string = my_string.upper()
print("Uppercase string:", upper_string)

# Replace a substring
replaced_string = my_string.replace("World", "Universe")
print("After replacing 'World' with 'Universe':", replaced_string)
