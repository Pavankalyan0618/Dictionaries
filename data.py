#use this list of menu items
import random
menu_items = {
'D1': ['SODA', 3],
'D2': ['LEMONADE', 3],
'D3': ['TEA' ,2],
'D4': ['WATER', 0],
'A1': ['POTATO_CAKES', 7, random.randint(25, 50)],
'A2': ['SPINACH_DIP', 5, random.randint(25, 50)],
'A3': ['OYSTERS', 13, random.randint(25, 50)],
'A4': ['CHEESE_FRIES', 4, random.randint(25, 50)],
'A5': ['ONION_RINGS', 7, random.randint(25, 50)],
'S1': ['COBB', 14, random.randint(25, 50)],
'S2': ['CAESAR', 13, random.randint(25, 50)],
'S3': ['GREEK', 12, random.randint(25, 50)],
'E1': ['BURGER', 16, random.randint(25, 50)],
'E2': ['PASTA', 15, random.randint(25, 50)],
'E3': ['GNOCCHI',14, random.randint(25, 50)],
'E4': ['GRILLED_STEAK_SANDWICH',17, random.randint(25, 50)],
'T1': ['CARAMEL_CHEESECAKE',13, random.randint(25, 50)],
'T2': ['APPLE_COBBLER',12, random.randint(25, 50)],
'T3': ['BROWNIE_SUNDAE',9, random.randint(25, 50)],
'T4': ['FLAN', 8, random.randint(25, 50)]
}


drink_items = ['D1', 'D2',  'D3', 'D4']
appetizer_items = ['A1', 'A2',  'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2',  'E3', 'E4']
dessert_items =['T1', 'T2',  'T3', 'T4']
all_items = drink_items + appetizer_items + salad_items + entree_items + dessert_items