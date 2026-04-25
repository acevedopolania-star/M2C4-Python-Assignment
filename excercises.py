#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
from decimal import Decimal
import math

#List
fruits = ['Apple', 'Grape', 'Orange', 'Banana', 'Watermelon']

#Tuple
ingredients = ('Oats', 'Eggs', 'Milk', 'Sugar', 'Vanilla')

#Float
price = 19.99

#Integer
integer = 10

#Decial
cost = Decimal ('88.40')

#Dictionary
user = {
    'name': 'Manuela',
    'score': 100,
    'status': 'Active'
}

#Exercise 2: Round your float up.
price_rounded = math.ceil(price)

#Exercise 3: Get the square root of your float.
price_square_root = math.sqrt (price)

#Exercise 4: Select the first element from your dictionary.
first_element_user = list(user.values())[0]

#Exercise 5: Select the second element from your tuple.
second_ingredient = ingredients[1]

#Exercise 6: Add an element to the end of your list.
extra_fruit = fruits.('Strawberry')

#Exercise 7: Replace the first element in your list.
fruits[0] = 'Pineapple'

#Exercise 8: Sort your list alphabetically.
fruits.sort()

#Exercise 9: Use reassignment to add an element to your tuple.
ingredients += ('Salt',)
