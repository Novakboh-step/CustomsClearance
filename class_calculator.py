from class_implementation import Car

class CarCalculator:
    def __init__(self, car: Car):
        self.car = car
        self.import_duty = self.calculate_import_duty()
        self.excise_tax = self.calculate_excise_tax()
        self.vat = self.calculate_vat()
        self.pension_fund = self.calculate_pension_fund()

    def calculate_import_duty(self):
        if self.car.engineType == "electro":
            return self.car.volumeValue * 5
        if self.car.country in ["EU", "UK", "US"]:
            if self.car.engineType == "gasoline":
                if self.car.volumeValue <= 1000:
                    return 0
                elif self.car.volumeValue <= 1500:
                    return self.car.price * 0.009
                return 0
            elif self.car.engineType == "diesel":
                return self.car.price * 0.009 if self.car.volumeValue <= 2500 else 0
            return self.car.price * 0.009
        return self.car.price * 0.1

    def calculate_excise_tax(self):
        base_rates = {"gasoline": (50, 100), "diesel": (75, 150)}
        if self.car.engineType not in base_rates:
            return 0
        base_rate = base_rates[self.car.engineType][0 if self.car.volumeValue <= (3000 if self.car.engineType == "gasoline" else 3500) else 1]
        engine_coef = self.car.volumeValue / 1000
        age_coef = min(2025 - self.car.year, 15)
        return base_rate * engine_coef * age_coef

    def calculate_vat(self):
        total_value = self.car.price + self.import_duty + self.excise_tax
        return total_value * 0.2

    def calculate_pension_fund(self):
        if self.car.price < 499620:
            return self.car.price * 0.03
        elif self.car.price < 877800:
            return self.car.price * 0.04
        return self.car.price * 0.05

    def total_customs_cost(self):
        return self.import_duty + self.excise_tax + self.vat + self.pension_fund

car = Car("diesel", 2000, 10, "EU", 10000, False)
calculator = CarCalculator(car)
print(f"Total customs cost: {calculator.total_customs_cost()} EUR")