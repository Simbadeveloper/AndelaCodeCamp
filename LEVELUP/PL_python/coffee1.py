"""Instruction for coffee machine
    1. make and serve me, you and Gibbs a cup of coffee(add coffee, and hot water, stir)
    2. change how the mix is stirred
    3. A  better way to make cofee with less repetition
    4. Make you coffe with milk and suger (add suger, and milk)
    5. Make Gibbs coffe with milk, sugar and something else (add sugar, milk'...)
    6. Refactor
"""

def make_coffee(*options):
    """makes coffee
       Args:
       options: 0 or more extra ingredients


    """
    #Get ingredients
    ingredients = ['coffee', 'hot water']

    if options:
        for option in options:
            ingredients.append(option)

    #print the number of items in ingredients
    print(len(ingredients))

    #Do the steps
    print ('started making coffee...\n Getting cup')
    print('Adding {}'.format(', '.join(ingredients)))
    print('Stir the mix 6 sec\n Finished making coffee...')

    if options:
      coffee = "Tasty coffee with {}".format(', '.join(options))
    else:
      coffee = 'Tasty coffee'
    return coffee

def serve_coffee(coffee, person_name):
    """serve coffee to a speccified person"""
    print("--Here' your {} {}. Enjoy !!!! --\n".format(coffee, person_name))



#make you coffee
you_coffee = make_coffee('milk')
serve_coffee(you_coffee, 'You')

#make Gibbs coffee
gibbs_coffee = make_coffee('cream')
serve_coffee(gibbs_coffee, 'Gibbs')

#make you coffee
your_coffee = make_coffee()
serve_coffee(your_coffee, 'silas')
