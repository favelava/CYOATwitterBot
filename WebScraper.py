import requests
from bs4 import BeautifulSoup

URL = 'https://www.liquor.com/recipes/bourbon-old-fashioned/'
className = 'simple-list__item js-checkbox-trigger ingredient'
dataToUse = './CocktailRecipes/AllLiquors.txt'

dataset = open(dataToUse, 'a+')
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')

cocktailName = soup.find('h1', class_='heading__title')
cocktailName = cocktailName.text.strip()
dataset.write(cocktailName)
dataset.write('\n')

ingredients = soup.find_all('li', class_=className)

for ingredient in ingredients:
    ingredient = ingredient.text.strip()
    dataset.write(ingredient)
    dataset.write('\n')

dataset.write('end')
