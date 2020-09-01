import requests
import re
import unidecode
from bs4 import BeautifulSoup

# To train the NN on your own cocktail preferences, add URLs to a
# RecipesToAdd.txt or directly add recipes to the relevant Liquor.txt
# in the CocktailRecipes folder

# We assume that the URLs in RecipesToAdd.txt are each on different lines

# WebScraper currently only accepts URLs from Liquor.com


# Remove accented characters and replace them with closest ASCII substitute
def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass

    text = unidecode.unidecode(text)
    return str(text)


# Replace path if training on different data
URLListFile = open("./CocktailRecipes/RecipesToAdd.txt", 'r')
URLList = URLListFile.readlines()
URLListFile.close()

for URL in URLList:
    URL = URL.strip('\n')

    if re.match(r'https://www.liquor.com', URL):
        # Relevant HTML names for Liquor.com
        ingClassName = 'simple-list__item js-checkbox-trigger ingredient'
        titleClassName = 'heading__title'
        dataToUse = './CocktailRecipes/AllLiquors.txt'

    dataset = open(dataToUse, 'a+')
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, 'html.parser')

    cocktailName = soup.find('h1', class_=titleClassName)

    # Remove any trailing white space and accented characters
    cocktailName = cocktailName.text.strip()
    cocktailName = strip_accents(cocktailName)

    # Write to data file
    dataset.write(cocktailName)
    dataset.write('\n')

    # Find all ingredients in current cocktail
    ingredients = soup.find_all('li', class_=ingClassName)

    for ingredient in ingredients:
        # Remove trailing white space and accented characters
        ingredient = ingredient.text.strip()
        ingredient = strip_accents(ingredient)

        # Replace ounce and ounces with oz for grammar reasons
        ingredient = re.sub(r'\bounce\b|\bounces\b', 'oz', ingredient)
        # Remove any asterisks in the ingredients list
        ingredient = ingredient.replace('*', '')

        # Write ingredient to data file and add a newline character
        dataset.write(ingredient)
        dataset.write('\n')

    # Write end at end of recipe
    dataset.write('end\n')
