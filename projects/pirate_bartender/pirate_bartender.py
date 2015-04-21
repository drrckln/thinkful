import random

questions = {   "strong": "Do ye like yer drinks strong?", 
		"salty": "Do ye like it with a salty tang?", 
		"bitter": "Are ye a lubber who likes it bitter?", 
		"sweet": "Would ye like a bit of sweetness with yer poison?", 
		"fruity": "Are ye one for a fruity finish?" }  

ingredients = { "strong": ["glug of rum", "slug of whisky", "splash of gin"], 
		"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"], 
		"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"], 
		"sweet": ["sugar cube", "spoonful of honey", "spash of cola"], 
		"fruity": ["slice of orange", "dash of cassis", "cherry on top"] }

def ask():
    answers = {}
    for key in questions.keys():
        ans = raw_input(questions[key] + " ")
        if ans == 'y' or ans == 'yes':
            answers[key] = True
        else:
            answers[key] = False
    return answers

def construct(prefs):
    """ Takes a preferences dict, returned from 'ask' function """
    drink = []
    drink_str = "Your drink is made out of a "
    for key in prefs.keys():
        if prefs[key] == True:
            drink.append(random.choice(ingredients[key]))
    # this is all complicated junk for pretty printing
    counter = 1
    for ingredient in drink:
        if counter == len(drink):
           drink_str += ingredient + "." 
	   break
        if counter == 1:
            drink_str += ingredient
	    if len(drink) == 2:
                drink_str += " and "
            else:
                drink_str += ", "
        elif counter == len(drink) - 1:
            drink_str += ingredient + ", and "
        else:
            drink_str += ingredient + ", "
        counter += 1
    print drink_str
    return drink


if __name__ == "__main__":
    prefs = ask()
    construct(prefs)
