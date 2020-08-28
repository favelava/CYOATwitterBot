import requests
from bs4 import BeautifulSoup

# To train the NN on your own cocktail preferences, add URLs to a
# RecipesToAdd.txt or directly add recipes to the relevant Liquor.txt
# in the CocktailRecipes folder

# We assume that the URLs in RecipesToAdd.txt are each on different lines

# WebScraper currently only accepts URLs from Liquor.com

URLListFile = open("./CocktailRecipes/RecipesToAdd.txt", 'r')
URLList = URLListFile.readlines()
URLListFile.close()

for URL in URLList:
    URL = URL.strip('\n')
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

    dataset.write('end\n')
