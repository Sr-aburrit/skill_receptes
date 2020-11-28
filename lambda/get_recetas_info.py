'''
IMPORTS
'''

import json

'''
FUNCIONES
'''

'''
Nombre: get_recipes_names
Funcion: Da los nombres de las recetas que hay guardadas en el fichero .json
Parametros: -
Retorno: Una cadena en formato String con los nombres concatenados
'''

def get_recipes_names():
    with open('recetas.json') as f:
        data = json.load(f)
        recipes_names = ""
        for recipe in data['recetas']:
            recipes_names += recipe['nombre'] + ', '
        
        recipes_names = recipes_names[:-2]
        
        f.close()
    return recipes_names

'''
Nombre: get_calories_of_recipe
Funcion: Da las calorias de una receta
Parametros: name_recipe: nombre de la receta de la que se quiere saber las calorias
Retorno: Una cadena en formato String con las calorias de la receta si la encuantra, si no, el String está vacio
'''

def get_calories_of_recipe(name_recipe):
    with open('recetas.json') as f:
        data = json.load(f)
        for recipe in data['recetas']:
            if recipe['nombre'].lower() == name_recipe.lower():
                calories = recipe['calorias']
                f.close()
                return str(calories)
        
        f.close()
    
    return ""

'''
Nombre: get_name_recipe_with_more_calories
Funcion: Da el nombre de la receta con mas calorias. En caso de haber coincidencia, devuelve la primera que encuentra
Parametros: -
Retorno: Una cadena en formato String con el nombre de la receta con mayor numero de calorias y sus calorias
'''

def get_name_recipe_with_more_calories():
    with open('recetas.json') as f:
        data = json.load(f)
        calories_max = data['recetas'][0]['calorias']
        name_calories_max = data['recetas'][0]['nombre']
        for recipe in data['recetas']:
            if recipe['calorias'] > calories_max:
                calories_max = recipe['calorias']
                name_calories_max = recipe['nombre']
        f.close()
    
    return name_calories_max + ", con " + str(calories_max) + " calorías"

'''
Nombre: get_ingredients_of_recipe
Funcion: Dar los ingredientes de una receta
Parametros: name_recipe: nombre de la receta de la que se quiere saber los ingredientes
Retorno: Una cadena en formato String con los ingredientes
'''

def get_ingredients_of_recipe(name_recipe):
    with open('recetas.json') as f:
        data = json.load(f)
        ingredients = ""
        for recipe in data['recetas']:
            if name_recipe.lower() == recipe['nombre'].lower():
                for ingredient in recipe['ingredientes']:
                    ingredients += ingredient + ', '
                
                f.close()
                
                ingredients = ingredients[:-2]
                
                return ingredients
        
        f.close()
        return ingredients

'''
Nombre: get_recipes_with_specific_diet
Funcion: Dar los nombres de las recetas que tienen una dieta concreta
Parametros: diet: dieta
Retorno: Una cadena en formato String con los nombres de las recetas
'''

def get_recipes_with_specific_diet(diet):
    with open('recetas.json') as f:
        data = json.load(f)
        recipes = ""
        for recipe in data['recetas']:
            for diet_json in recipe['dietas']:
                if diet == diet_json:
                    recipes += recipe['nombre'] + ', '
        
        recipes = recipes[:-2]
        f.close()
    return recipes
