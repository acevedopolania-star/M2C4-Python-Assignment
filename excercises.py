from decimal import Decimal
import math

#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

#List
fruits = ['Apple', 'Grape', 'Orange', 'Banana', 'Watermelon']
print(fruits)

#Tuple
ingredients = ('Oats', 'Eggs', 'Milk', 'Sugar', 'Vanilla')
print(ingredients)

#Float
price = 19.99
print(price)

#Integer
age = 10
print(age)

#Decimal
cost = Decimal('88.40')
print(cost)

#Dictionary
user = {
    'name': 'Manuela',
    'score': 100,
    'status': 'Active'
}
print(user)

#Exercise 2: Round your float up.
price_rounded = math.ceil(price)
print(price_rounded)

#Exercise 3: Get the square root of your float.
price_square_root = math.sqrt(price)
print(price_square_root)

#Exercise 4: Select the first element from your dictionary.
first_element_user = user ['name']
print(first_element_user)

#Exercise 5: Select the second element from your tuple.
second_ingredient = ingredients[1]
print(second_ingredient)

#Exercise 6: Add an element to the end of your list.
fruits.append('Strawberry')
print(fruits)

#Exercise 7: Replace the first element in your list.
fruits[0] = 'Pineapple'
print(fruits)

#Exercise 8: Sort your list alphabetically.
fruits.sort()
print(fruits)

#Exercise 9: Use reassignment to add an element to your tuple.
ingredients += ('Salt',)
print(ingredients)
