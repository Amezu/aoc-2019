def countFuel(mass):
    fuelSum = 0
    fuel = mass // 3 - 2
    while fuel > 0:
        fuelSum += fuel
        fuel = fuel // 3 - 2
    return fuelSum


fuelSum = 0
with open("input.txt") as file:
    for mass in file:
        fuelSum += countFuel(int(mass))
print(fuelSum)
