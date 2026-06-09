def massEnergy(mass):
    c = 300000000
    energy = mass * c ** 2
    return energy

def main():

    mass = int(input("Mass: "))
    energy = massEnergy(mass)
    print(energy)

main()