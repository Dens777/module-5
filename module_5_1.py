class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floors_destination):

        if floors_destination < 0 or floors_destination > self.number_of_floors:
                print ('Такого этажа не существует, это здание имеет этажность', self.number_of_floors)
        else:
            for i in range(floors_destination):
                print (i+1)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
