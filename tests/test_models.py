import unittest
from app.models import IngredientsModel, StepsModel, RecipesModel
from app.models import Ingredient, Recipe, Step

class TestRecipesModel(unittest.TestCase):
    model = RecipesModel()

    def setUp(self):
        pass

    def test_create(self):
        pass

    def test_read(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass

    def test_load(self):
        pass

class TestIngredientsModel(unittest.TestCase):
    model = IngredientsModel()

    def setUp(self):
        pass

    def test_create(self):
        pass

    def test_read(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass

    def test_load(self):
        pass

class TestStepsModel(unittest.TestCase):
    model = StepsModel()

    def setUp(self):
        pass

    def test_create(self):
        pass

    def test_read(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass

    def test_load(self):
        pass

if __name__ == "__main__":
    unittest.main()
