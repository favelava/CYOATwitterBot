# CocktailGenerator

This repo holds the source code for a Cocktail Generator which creates a cocktail recipe for a given cocktail name. The NN will eventually be hosted on Twitter for easy use.

If you want to download and play with the generator in the meantime, the python requirements are captured in requirements.txt. In additon, the project was built using
tensorflow-gpu. If you'd like to configure your system to run Tensorflow with GPU support, a tutorial on how to do so can be found here: 
https://towardsdatascience.com/installing-tensorflow-with-cuda-cudnn-and-gpu-support-on-windows-10-60693e46e781

An ever-expanding corpus of recipes can be found in the CocktailRecipes folder, sorted by their liquor type. Recipes can be added manually or taken from Liquor.com with
WebScraper.py. It is recommended to only modify AllLiquors.txt, then run SortRecipes.py to automatically populate all other recipe lists.

The network can be trained by pointing line 8 of CreateCharSequences.py to the txt file you wish to train the network on. Run TrainCocktailGenerator.py to produce a 
mapping and a model file. Point line 6 and line 9 of CocktailGenerator.py to the model and mapping files you wish to use, then, still in CocktailGenerator.py, modify 
seed_text of generate_seq to whatever you'd like to name your cocktail. Run CocktailGenerator.py to generate your cocktail. CocktailGenerator.py will generate ingredients
until the end character "_" is generated or until the character limit specified (n_chars) is reached.
