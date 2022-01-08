game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    # Accesible outside the if loop, No block scope in python
    print(new_enemy)


create_enemy()
