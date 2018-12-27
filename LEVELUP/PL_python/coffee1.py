"""Instruction for coffee machine
    1. make and serve me, you and Gibbs a cup of coffee(add coffee, and hot water, stir)
    2. change how the mix is stirred
    3. A  better way to make cofee with less repetition
    4. Make you coffe with milk and suger (add suger, and milk)
    5. Make Gibbs coffe with milk, sugar and something else (add sugar, milk'...)
    6. Refactor
"""

def make_coffee():
    """makes coffee"""
    ingredients = ['coffee', 'hot water']
    print ('started making coffee...')
    print('Getting cup')
    print('Adding {}'.format(', '.join(ingredients)))
    print('Stir the mix 6 sec')
    print('Finished making coffee...')
    coffee = 'Tasty coffee'
    return coffee

def serve_coffee(coffee, person_name):
    """serve coffee to a speccified person"""
    print("--Here' your {} {}. Enjoy !!!! --\n".format(coffee, person_name))

#make my coffee
my_coffee = make_coffee()
serve_coffee(my_coffee, 'silas')

#make you coffee
you_coffee = make_coffee()
serve_coffee(you_coffee, 'You')

#make Gibbs coffee
gibbs_coffee = make_coffee()
serve_coffee(gibbs_coffee, 'Gibbs')
