import requests

def smartest_hero(url,heroes):
    max_smart = 0
    for names in heroes:
        response = requests.get(url+names)
        stats = int(response.json()['results'][0]['powerstats']['intelligence'])
        if stats > max_smart:
            max_smart = stats
            smartest_hero = response.json()['results'][0]['biography']['full-name']
    return print(f'Самый умный супер-герой {smartest_hero} с показателем {max_smart}')


url = 'https://superheroapi.com/api/2619421814940190/search/'
heroes_list = ['Hulk', 'Captain America', 'Thanos']
smartest_hero(url, heroes_list)