from models import IngredientsModel, RecipesModel, StepsModel

class Controller:
    steps = StepsModel()
    recipes = RecipesModel()
    ingredients = IngredientsModel()

    def search(self):
        pass

    def category_filter(self):
        pass

    def create_recipe(self):
        pass

    def get_recipes(self):
        pass

    def get_recipe(self):
        pass

    def sign_up(self):
        pass

    def sign_in(self):
        pass 

    def sign_out(self):
        pass

cnt = Controller()
cnt.search()
