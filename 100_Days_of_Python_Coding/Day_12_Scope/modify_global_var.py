enemies = 1

modifiable_enemies = 1


def increase_enemies():
    # cannot modify directly
    # enemies +=1 shows an error
    global modifiable_enemies
    modifiable_enemies += 1
    # enemies = 2
    print(f"enemies inside function: {enemies}")

    # or simply return the value as below
    return enemies + 1


increase_enemies()
print(f"enemies outside function: {enemies}")
