
classroom = [(29, True), (24, True), (29, False)]

for temp, occupied in classroom:

    if occupied == False:
        mode = "ECO"

    elif temp > 26:
        mode = "COOL"

    elif temp < 20:
        mode = "WARM"

    else:
        mode = "IDLE"

    print("Temperature:", temp)
    print("Occupied:", occupied)
    print("Mode:", mode)
    print("----------------")
