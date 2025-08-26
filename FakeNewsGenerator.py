import random
#2- Create subjects
subjects = [
    "Badshah",
    "Khalnayak",
    "Ghanashyam Dharsode",
    "Sudhir Deshmukh",
    "Kafru Gang",
    "Chachwal Gang",
    "Lal Bautya",
    "Circuit Panisode",
    "King Garuda",
    "Rauf Lala"
]


actions = [
    "Robbery",
    "Dances with",
    "Marry with",
    "Eats",
    "Slaps",
    "Atempts Murder",
    "Murders",
    "Bitten by",
    "slapped by"
]


places_or_things = [
    "At nikola",
    "At Bar",
    "In Budhwar Peth",
    "Plate of Samosa",
    "Inside Ladies Parlor",
    "On a Ice slab Inside Police Station",
    "On a Bike",
    "On A bridge",
    "On a street with plate"
]

# 3- Start headline generation loop 
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    Place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {Place_or_thing} "
    print("\n"+ headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
# Print good bye message 
print("\nThanks for using fake news headline Generator. Have a fun day")
    


    
    