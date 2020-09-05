file_read_path = './CocktailRecipes/AllLiquors.txt'
file_to_read = open(file_read_path, 'r')
raw_text = file_to_read.read()
file_to_read.close()

recipes = raw_text.split('_')

liquors = ['Gin', 'Rum', 'Tequila', 'Whiskey', 'Vodka']

for recipe in recipes:
    for liquor in liquors:
        if (recipe.find(' '+liquor+'\n') > -1 or
           recipe.find(' '+liquor.lower()+'\n') > -1 or
           recipe.find(' '+liquor+' ') > -1 or
           recipe.find(' '+liquor.lower()+' ') > -1):
            file_write_path = './CocktailRecipes/{}.txt'.format(liquor)
        else:
            file_write_path = './CocktailRecipes/Other.txt'

        file_to_write = open(file_write_path, 'a+')
        file_to_write.write(recipe+'_')
        file_to_write.close()
