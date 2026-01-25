import os
import sqlite3
import hashlib
from typing import List
from dataclasses import dataclass


@dataclass
class User:
    pk : int
    username: str
    password: str

@dataclass
class Ingredient:
    pk: int
    name: str
    size: int
    recipe_pk: int

@dataclass
class Step:
    pk: int
    count: int
    details: str
    recipe_pk: int

@dataclass
class Recipe:
    pk: int
    name: str
    summary: str
    category: str

class Model:
    table = ""

    def __init__(self):
        self.data = {}
        self.connection = sqlite3.connect("app.db")
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

    def load(self):
        print(self.cursor.fetchall())

    def initDatabase(self):
        self.cursor.execute("""
            CREATE TABLE Recipes(
                pk INTEGER PRIMARY KEY,
                name TEXT,
                summary TEXT,
                category TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE Steps(
                pk INTEGER PRIMARY KEY,
                count INTEGER,
                details TEXT,
                recipe_pk INTEGER NOT NULL,
                FOREIGN KEY (recipe_pk) REFERENCES Recipes(pk)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE Ingredients(
                pk INTEGER PRIMARY KEY,
                name TEXT,
                size INTEGER,
                recipe_pk INTEGER NOT NULL,
                FOREIGN KEY (recipe_pk) REFERENCES Recipes(pk)
            )
        """)

class StepsModel(Model):
    table = "Steps"
    def __init__(self):
        super().__init__();

    def save(self,steps_obj):
        self.cursor.execute(
            "INSERT INTO Steps (count,details,recipe_pk) VALUES(?,?,?)",
            (steps_obj.count,steps_obj.details,steps_obj.recipe_pk)
        )
        self.connection.commit()

    def create(self,pk,count,details,recipe_pk):
        new_step = Step(pk,count,details,recipe_pk)
        self.data[pk] = new_step
        return new_step

    def read(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            return self.data[pk]

    def read_all(self):
        return list(self.data.values())

    def update(self,pk,new_pk,count,details,recipe_pk):
        if pk not in self.data:
            print("No such cooking step")
        else:
            self.data[pk].count = count
            self.data[pk].details = details
            self.data[pk].recipe_pk = recipe_pk
            self.data[pk].pk = new_pk
            return self.data[pk]

    def delete(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            del self.data[pk]
            return True


class IngredientsModel(Model):
    table = "Ingredients"

    def __init__(self):
        super().__init__();

    def save(self,ingre_obj):
        self.cursor.execute(
            "INSERT INTO Ingredients (name,size,recipe_pk) VALUES(?,?,?)",
            (ingre_obj.name,ingre_obj.size,ingre_obj.recipe_pk)
        )
        self.connection.commit()

    def create(self,pk,name,size,recipe_pk):
        new_ing = Ingredient(pk,name,size,recipe_pk)
        self.data[pk] = new_ing
        return new_ing

    def read(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            return self.data[pk]

    def read_all(self):
        return list(self.data.values())

    def update(self,pk,new_pk,name,size,recipe_pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            self.data[pk].name = name
            self.data[pk].size = size
            self.data[pk].recipe_pk = recipe_pk
            self.data[pk].pk = new_pk
            return self.data[new_pk]

    def delete(self,pk):
        if pk not in self.data:
            print("No such ingredient")
        else:
            del self.data[pk]
            return True

class RecipesModel(Model):
    table = "Recipes"

    def __init__(self):
        super().__init__();

    def save(self,recipe_obj):
        self.cursor.execute(
            "INSERT INTO Recipes (name,summary,category) VALUES(?,?,?)",
            (recipe_obj.name,recipe_obj.summary,recipe_obj.category)
        )
        self.connection.commit()

    def create(self,pk,name,summary,category,steps,ingredients):
        new_recipe = Recipe(pk,name,summary,category,steps,ingredients)
        self.data[pk] = new_recipe
        return new_recipe

    def read(self,pk):
        if pk not in self.data:
            print("No such recipe")
        else:
            return self.data[pk]

    def read_all(self):
        return list(self.data.values())

    def update(self,pk,new_pk,summary,category,steps,ingredients):
        if pk not in self.data:
            print("No such recipe")
        else:
            self.data[pk].category = category
            self.data[pk].summary = summary
            self.data[pk].steps = steps
            self.data[pk].ingredients = ingredients
            self.data[pk].pk = new_pk
            return self.data[new_pk]

    def delete(self,pk):
        if pk not in self.data:
            print("No such recipe")
        else:
            del self.data[pk]
            return True
