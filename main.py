import datetime
import calendar
import requests
from pprint import pprint as pp

# To install additional modules use the command python pip install 'name_of_package'
# pprint has been installed so that when long data structures are printed they are shown in a readable format rather
# than as one long line



today = datetime.datetime.now()
print(today)
print(today.strftime("%d/%b/%Y"))

weekday = calendar.day_name[today.weekday()]
print(weekday[:2])

user_name = input("What is your name?")
print("Hello {}, today is {}. Let's play a game! Can you find a heavy Pokemon?".format(user_name, weekday))

def rules():
    print("Remember the rule of the game. The Pokemon must be heavy to win.")

# A function called rules has been created so that the user can easily be reminded throughout what the rules of the game
# are

rules()

user_pokemon_number = input("Choose your Pokemon: Pick a number...")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(user_pokemon_number)

# Pokeapi is an open api so no authentication is needed to access this. This api will be used to get the name and weight
# of specific Pokemon.

user_response = requests.get(url)

data = user_response.json()
# pp(user_pokemon)

name = data['name']
weight = data['weight']
pp("You chose {}. {} weighs {}.".format(data['name'], data['name'], data['weight']))

with open('pokemon.txt', 'w') as text_file:
    text_file.write(data['name'] + '\n')
    text_file.write(str(data['weight']) + '\n')

while weight < 500:
    print("This Pokemon is a light Pokemon. Let's try again.")
    rules()
    user_pokemon_number = input("Choose your Pokemon: Pick a number...")
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(user_pokemon_number)

    user_response = requests.get(url)
    print(user_response)

    data = user_response.json()
    # pp(user_pokemon)

    name = data['name']
    weight = data['weight']
    pp("You chose {}. {} weighs {}.".format(data['name'], data['name'], data['weight']))

    with open('pokemon.txt', 'a') as text_file:
        text_file.write(data['name'] + '\n')
        text_file.write(str(data['weight']) + '\n')

if weight > 500:
    print("Well done. This Pokemon is a heavy Pokemon.")
else:
    print("Wow, you have found the most balanced Pokemon")

# a while loop is used to repeat the code that allows the user to choose a Pokemon, meaning they can keep going until
# they get the correct one
# they will continue until the weight > 500 unless they find a Pokemon that is exactly 500
# append is used in the while loop to ensure that as the user tries different pokemon they are all listed in the
# pokemon.txt file
