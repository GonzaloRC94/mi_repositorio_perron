# LIST COMPREHENSION

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
even_numbers = [x for x in numbers if x%2 == 0]
odd_numbers = [x for x in numbers if x%2 != 0]


list_fruits = ["apple", "banana", "strawberry", "pineapple", "watermelon", "orange", "grapes", "pear", "melon", "mango", "avocado"]

newList_fruits = [fruit for fruit in list_fruits if fruit[0]=="a"]
print(newList_fruits)
