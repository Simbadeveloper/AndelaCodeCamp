"""Instruction for coffee machine
    1. make and serve me, you and Gibbs a cup of coffee(add coffee, and hot water, stir)
    2. change how the mix is stirred
    3. A  better way to make cofee with less repetition
    4. Make you coffe with milk and suger (add suger, and milk)
    5. Make Gibbs coffe with milk, sugar and something else (add sugar, milk'...)
    6. Refactor
"""

# make my coffee
ingredients = ['coffee', 'hot water']
print ('started making coffee...')
print('Getting cup')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix 6 sec')
print('Finished making coffee...')
my_coffee = 'Tasty coffee'
print("--Here' your {} {}. Enjoy !!!! --\n".format(my_coffee, 'silas'))

#make you coffee
print ('started making coffee...')
print('Getting cup')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix for 6 sec')
print('Finished making coffee...')
your_coffee = 'Tasty coffee'
print("--Here' your {} {}. Enjoy !!!! --\n".format(your_coffee, 'You'))

#make Gibbs coffee
print ('started making coffee...')
print('Getting cup')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix for 6 sec')
print('Finished making coffee...')
gibbs_coffee = 'Tasty coffee'
print("--Here' your {} {}. Enjoy !!!! --\n".format(gibbs_coffee, 'Gibbs'))