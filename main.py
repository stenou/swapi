import requests
import json
import sys
import pprint

pp = pprint.PrettyPrinter()

# valid episode numbers
episodes = ['1', '2', '3', '4', '5', '6', '7']

def starship_pilots(episode_input):
    starships = []
    film_id = 0

    if episode_input == '4':
        film_id = 1
    elif episode_input == '5':
        film_id = 2
    elif episode_input == '6':
        film_id = 3
    elif episode_input == '1':
        film_id = 4
    elif episode_input == '2':
        film_id = 5
    elif episode_input == '3':
        film_id = 6
    elif episode_input == '7':
        film_id = 7
    
    film = (requests.get(f'https://swapi.co/api/films/{film_id}')).json()
    for ship in film['starships']:
        pilot_list = []
        ship_data = (requests.get(ship)).json()
        for pilot in ship_data['pilots']:
            pilot_data = (requests.get(pilot)).json()
            pilot_list.append(pilot_data['name'])
        
        starships.append({
            "name": ship_data['name'],
            "pilots": pilot_list
        })
    return starships

if len(sys.argv) == 2 and sys.argv[1] in episodes:
    starships = starship_pilots(sys.argv[1])
    pp.pprint(starships)
else:
    print(f'"{" ".join(sys.argv[1:])}" is not a valid option. Please enter an episode number:\n'
            '1: The Phantom Menace\n'
            '2: Attack of the Clones\n'
            '3: Revenge of the Sith\n'
            '4: A New Hope\n'
            '5: The Empire Strikes Back\n'
            '6: Return of the Jedi\n'
            '7: The Force Awakens')
        
