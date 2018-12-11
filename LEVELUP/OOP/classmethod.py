class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
        
        """
        class methods  allow you to define alternative constructors for your classes.
        
      >>> Pizza.margherita()
      Pizza(['mozzarella', 'tomatoes'])

      >>> Pizza.prosciutto()
       Pizza(['mozzarella', 'tomatoes', 'ham'])
        """
