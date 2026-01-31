import os
import sqlite3
import hashlib
from typing import List
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    size: int
    recipe_pk: int

@dataclass
class Step:
    count: int
    details: str
    recipe_pk: int

@dataclass
class Recipe:
    name: str
    summary: str
    category: str

class Model:
    def __init__(self):
        self.data = {}
        self.connection = sqlite3.connect("app.db")
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

    def initDatabase(self):
        self.cursor.execute("""
            CREATE TABLE Recipes(
                id INTEGER PRIMARY KEY,
                name TEXT,
                summary TEXT,
                category TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE Steps(
                id INTEGER PRIMARY KEY,
                count INTEGER,
                details TEXT,
                recipe_pk INTEGER NOT NULL,
                FOREIGN KEY (recipe_pk) REFERENCES Recipes(pk)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE Ingredients(
                id INTEGER PRIMARY KEY,
                name TEXT,
                size INTEGER,
                recipe_pk INTEGER NOT NULL,
                FOREIGN KEY (recipe_pk) REFERENCES Recipes(pk)
            )
        """)

class StepsModel(Model):
    def __init__(self):
        super().__init__();

    def load(self):
        self.cursor.execute(
            "SELECT * FROM Steps"
        )
        rows = self.cursor.fetchall()
        for row in rows:
            self.data[row[0]] = Step(row[1],row[2],row[3])

    def save(self,step_obj):
        self.cursor.execute(
            "INSERT INTO Steps (count,details,recipe_pk) VALUES(?,?,?)",
            (step_obj.count,step_obj.details,step_obj.recipe_pk)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def create(self,count,details,recipe_pk):
        new_step = Step(count,details,recipe_pk)
        pk = self.save(self,new_step)
        self.data[pk] = new_step
        return new_step

    def read(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            return self.data[pk]

    def read_all(self):
        return list(self.data.values())

    def update(self,pk,count,details,recipe_pk):
        if pk not in self.data:
            print("No such cooking step")
        else:
            self.data[pk].count = count
            self.data[pk].details = details
            self.data[pk].recipe_pk = recipe_pk
            return self.data[pk]

    def delete(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            del self.data[pk]
            return True


class IngredientsModel(Model):
    def __init__(self):
        super().__init__();

    def load(self):
        self.cursor.execute(
            "SELECT * FROM Ingredients"
        )
        rows = self.cursor.fetchall()
        for row in rows:
            self.data[row[0]] = Ingredient(row[1],row[2],row[3])

    def save(self,ingre_obj):
        self.cursor.execute(
            "INSERT INTO Ingredients (name,size,recipe_pk) VALUES(?,?,?)",
            (ingre_obj.name,ingre_obj.size,ingre_obj.recipe_pk)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def create(self,name,size,recipe_pk):
        new_ing = Ingredient(name,size,recipe_pk)
        pk = self.save(new_ing)
        self.data[pk] = new_ing
        return new_ing

    def read(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            return self.data[pk]

    def read_all(self):
        return list(self.data.values())

    def update(self,pk,name,size,recipe_pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            self.data[pk].name = name
            self.data[pk].size = size
            self.data[pk].recipe_pk = recipe_pk
            return self.data[pk]

    def delete(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            del self.data[pk]
            return True

class RecipesModel(Model):
    def __init__(self):
        super().__init__()

    def load(self):
        self.cursor.execute(
            "SELECT * FROM Recipes"
        )
        rows = self.cursor.fetchall()
        for row in rows:
            self.data[row[0]] = Recipe(row[1],row[2],row[3])

    def saveNew(self,recipe_obj):
        self.cursor.execute(
            "INSERT INTO Recipes (name,summary,category) VALUES(?,?,?)",
            (recipe_obj.name,recipe_obj.summary,recipe_obj.category)
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def save(self,pk,recipe_obj):
        self.cursor.execute(
            "UPDATE Recipes SET name=?, sumary=?, category=?, WHERE id=?",
            (recipe_obj.name,recipe_obj.summary,recipe_obj.category,pk)
        )
        self.connection.commit()

    def create(self,name,summary,category):
        new_recipe = Recipe(name,summary,category)
        pk = self.saveNew(new_recipe)
        self.data[pk] = new_recipe
        return new_recipe

    def read(self,pk):
        if pk not in self.data:
            print("No such recipe")
        else:
            return self.data[pk]

    def read_all(self):
        return list(self.data.values())

    def update(self,pk,name,summary,category):
        if pk not in self.data:
            print("No such recipe")
        else:
            self.data[pk].name = name
            self.data[pk].summary = summary
            self.data[pk].category = category
            self.save(pk,Recipe(name,summary,category))
            return self.data[pk]

    def delete(self,pk):
        if pk not in self.data:
            print("No such recipe")
        else:
            del self.data[pk]
            return True
