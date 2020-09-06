from CreateCharSequences.py import load_doc, save_doc

file_read_path = './CocktailRecipes/AllLiquors.txt'

raw_text = load_doc(file_read_path)
recipes = raw_text.split('_')

liquors = ['Gin', 'Rum', 'Tequila', 'Whiskey', 'Vodka']

for recipe in recipes:
    sorted = False
    for liquor in liquors:
        if (recipe.find(' '+liquor+'\n') > -1 or
           recipe.find(' '+liquor.lower()+'\n') > -1 or
           recipe.find(' '+liquor+' ') > -1 or
           recipe.find(' '+liquor.lower()+' ') > -1):
            file_write_path = './CocktailRecipes/{}.txt'.format(liquor)
            sorted = True
            save_doc(recipe, file_write_path)

    if not sorted:
        file_write_path = './CocktailRecipes/Other.txt'
        save_doc(recipe, file_write_path)
