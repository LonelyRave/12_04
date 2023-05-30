import json
import urllib.request


def get_ship_info():
    url = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    ship_info = {}

    if data["count"] > 0:
        ship = data["results"][0]
        ship_info["name"] = ship["name"]
        ship_info["max_speed"] = ship["max_atmosphering_speed"]
        ship_info["class"] = ship["starship_class"]
        ship_info["pilots"] = []
        for pilot_url in ship["pilots"]:
            pilot = get_pilot_info(pilot_url)
            ship_info["pilots"].append(pilot)
    return ship_info


def get_pilot_info(pilot_url):
    response = urllib.request.urlopen(pilot_url)
    pilot = json.loads(response.read().decode())
    pilot_info = {}
    pilot_info["name"] = pilot["name"]
    pilot_info["height"] = pilot["height"]
    pilot_info["weight"] = pilot["mass"]
    pilot_info["homeworld"] = pilot["homeworld"]
    pilot_info["homeworld_info"] = get_planet_info(pilot["homeworld"])
    return pilot_info


def get_planet_info(planet_url):
    response = urllib.request.urlopen(planet_url)
    planet = json.loads(response.read().decode())
    planet_info = {}
    planet_info["name"] = planet["name"]
    planet_info["url"] = planet["url"]
    return planet_info
