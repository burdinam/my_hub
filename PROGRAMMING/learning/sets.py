cars = ["auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7"]

for car in cars:
    print(car)

cars = {"auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7"}

cars.add("auto8")

print(cars)

cars.update(["auto9", "auto10", "auto11"])

print(cars)

print(len(cars))

cars.remove("auto10")

print(cars)

print(len(cars))

x="auto20"

if (x in cars) == True:
    cars.remove(x)
else:
    print("wo don't have this car")

x="auto1"

if (x in cars) == True:
    cars.remove(x)
    print(cars)
    print(len(cars))
else:
    print("wo don't have this car")
