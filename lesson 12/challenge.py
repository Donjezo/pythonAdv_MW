class Adult:
    def __init__(self, weight, height):
        self.weight = weight      # kg
        self.height = height      # m

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)


adult = Adult(55, 1.67)
print(adult.calculate_bmi())