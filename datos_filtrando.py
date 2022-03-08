aquarium_creatures = [
  {"name": "sammy", 
  "species": "shark", 
  "tank number": 11, 
  "type": "fish"},

  {"name": "ashley", 
  "species": "crab", 
  "tank number": 25, 
  "type": "shellfish"},

  {"name": "jo", 
  "species": "guppy", 
  "tank number": 18, 
  "type": "fish"},

  {"name": "jackie", 
  "species": "lobster", 
  "tank number": 21, 
  "type": "shellfish"},

  {"name": "charlie", 
  "species": "shark", 
  "tank number": 12, 
  "type": "fish"},

  {"name": "olly", 
  "species": "green turtle", 
  "tank number": 34, 
  "type": "turtle"}
]

def main():
    peces =[pez["name"] for pez in aquarium_creatures if pez["type"]=="fish"]
    #print(peces)

    number = list(filter(lambda pescadito : pescadito["tank number"]< 20, aquarium_creatures))
  

    especie = list(map(lambda pez : print(pez['name']) if pez["species"]== "shark" else 0, number))
    print(especie)

if __name__=='__main__':
    main()
