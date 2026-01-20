import os
import hashlib
from typing import List
from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str

@dataclass
class Ingredient:
    pk: int
    name: str
    size: float

@dataclass
class Step:
    pk: int
    count: int
    details: str

@dataclass
class Recipe:
    pk: int
    summary: str
    category: str
    steps: List[int]
    ingredients: List[int]

class Model:
    def save(self):
        pass

    def load(self):
        pass

class UsersModel(Model):
    Users = {}

    def hash_password(self,password):
    # 1. Generate a random salt
        salt = os.urandom(16)
    # 2. Hash the password with PBKDF2
        hash_bytes = hashlib.pbkdf2_hmac(
            'sha256',              # hash algorithm
            password.encode(),     # convert to bytes
            salt,                  # salt
            100_000                # iterations (minimum recommended)
        )
    # 3. Store salt + hash (not the password)
        password_hash = salt + hash_bytes
        return password_hash

    def create(self,pk,username,password):
        hashed = hash_password(password)
        new_user = User(pk,username,hashed)
        self.Users[pk] = new_user
        return new_user

    def read(self,pk):
        if pk not in self.Users:
            print("No such ingredient")
        else:
            return self.Users[pk]

    def update(self,pk,new_pk,username,password):
        if pk not in Users:
            print("No such ingredient")
        else:
            self.Users[pk].username = username
            self.Users[pk].password = password
            self.Users[pk].pk = new_pk
            return self.Users[new_pk]

    def delete(self,pk):
        if pk not in self.Users:
            print("No such User")
        else:
            del Users[pk]
            return True


class StepsModel(Model):
    Steps = {}

    def create(self,pk,count,details):
        new_step = Step(pk,count,details)
        self.Steps[pk] = new_step
        return new_step

    def read(self,pk):
        if pk not in self.Steps:
            print("No such ingredient")
        else:
            return self.Steps[pk]

    def update(self,pk,new_pk,count,details):
        if pk not in self.Steps:
            print("No such cooking step")
        else:
            self.Steps[pk].count = count
            self.Steps[pk].details = details
            self.Steps[pk].pk = new_pk
            return self.Steps[pk]

    def delete(self,pk):
        if pk not in self.Steps:
            print("No such ingredient")
        else:
            del self.Steps[pk]
            return True


class IngredientsModel(Model):
    Ingredients = {}

    def create(self,pk,name,size):
        new_ing = Ingredient(pk,name,size)
        self.Ingredients[pk] = new_ing
        return new_ing

    def read(self,pk):
        if pk not in self.Ingredients:
            print("No such ingredient")
        else:
            return self.Ingredients[pk]

    def update(self,pk,new_pk,name,size):
        if pk not in self.Ingredients:
            print("No such ingredient")
        else:
            self.Ingredients[pk].name = name
            self.Ingredients[pk].size = size
            self.Ingredients[pk].pk = new_pk
            return self.Ingredients[new_pk]

    def delete(self,pk):
        if pk not in self.Ingredients:
            print("No such ingredient")
        else:
            del self.Ingredients[pk]
            return True

class RecipesModel(Model):
    Recipes = {}

    def create(self,pk,summary,category,steps,ingredients):
        new_recipe = Recipe(pk,summary,category,steps,ingredients)
        self.Recipes[pk] = new_recipe
        return new_recipe

    def read(self,pk):
        if pk not in self.Recipes:
            print("No such recipe")
        else:
            return self.Recipes[pk]

    def update(self,pk,new_pk,summary,category,steps,ingredients):
        if pk not in self.Recipes:
            print("No such recipe")
        else:
            self.Recipes[pk].category = category
            self.Recipes[pk].summary = summary
            self.Recipes[pk].steps = steps
            self.Recipes[pk].ingredients = ingredients
            self.Recipes[pk].pk = new_pk
            return self.Recipes[new_pk]

    def delete(self,pk):
        if pk not in self.Recipes:
            print("No such recipe")
        else:
            del self.Recipes[pk]
            return True

