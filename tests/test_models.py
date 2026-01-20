import unittest
from app.models import IngredientsModel, StepsModel, RecipesModel
from app.models import Ingredient, Recipe, Step

class TestRecipesModel(unittest.TestCase):
    model = RecipesModel()

    def setUp(self):
        self.model.create(0,"Pork pie","pie",[1,2,3],[1,2,3])
        self.model.create(1,"Cottage pie","pie",[1,2,3],[1,2,3])
        self.model.create(2,"Beef pie","pie",[1,2,3],[1,2,3])

    def test_create(self):
        self.assertEqual(self.model.create(3,"Beef stew","stew",[1,2],[1,2]),Recipe(3,"Beef stew","stew",[1,2],[1,2]))

    def test_read(self):
        self.assertEqual(self.model.read(2),Recipe(2,"Beef pie","pie",[1,2,3],[1,2,3]))
        self.assertEqual(self.model.read(3),Recipe(3,"Beef stew","stew",[1,2],[1,2]))

    def test_update(self):
        self.assertEqual(self.model.update(0,0,"Pork pie","pies",[1,2],[1,2]),Recipe(0,"Pork pie","pies",[1,2],[1,2]))

    def test_delete(self):
        self.assertEqual(self.model.delete(0),True)

class TestIngredientsModel(unittest.TestCase):
    model = IngredientsModel()

    def setUp(self):
        self.model.create(0,"onion",20)
        self.model.create(1,"carrot",20)
        self.model.create(2,"cellery",20)

    def test_create(self):
        self.assertEqual(self.model.create(3,"sweet corn",20),Ingredient(3,"sweet corn",20))

    def test_read(self):
        self.assertEqual(self.model.read(0),Ingredient(0,"onion",20))
        self.assertEqual(self.model.read(1),Ingredient(1,"carrot",20))
        self.assertEqual(self.model.read(2),Ingredient(2,"cellery",20))
        self.assertEqual(self.model.read(3),Ingredient(3,"sweet corn",20))

    def test_update(self):
        self.assertEqual(self.model.update(1,1,"sweet corn",10),Ingredient(1,"sweet corn",10))

    def test_delete(self):
        self.assertEqual(self.model.delete(2),True)

class TestStepsModel(unittest.TestCase):
    model = StepsModel()

    def setUp(self):
        self.model.create(0,1,"step details")
        self.model.create(1,2,"step details")
        self.model.create(2,3,"step details")

    def test_create(self):
        self.assertEqual(self.model.create(3,4,"steps details"),Step(3,4,"steps details"))

    def test_read(self):
        self.assertEqual(self.model.read(1),Step(1,2,"step details"))
        self.assertEqual(self.model.read(3),Step(3,4,"steps details"))

    def test_update(self):
        self.assertEqual(self.model.update(1,1,1,"step details (changed)"),Step(1,1,"step details (changed)"))

    def test_delete(self):
        self.assertEqual(self.model.delete(0),True)

if __name__ == "__main__":
    unittest.main()
