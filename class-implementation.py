class Car():
    def __init__(self, engineType: str, volumeValue: int, year, country: str, price: float, isAuction: bool):
        self.possibleEngineTypes = {"diesel": "cm3", "gasoline": "cm3", "electro": "kw"}

        if (engineType.lower() not in self.possibleEngineTypes.keys()):
            raise Exception("No such engine type")

        if (price < 0):
            raise Exception("Price can't be negative")

        self.engineType = engineType
        self.volumeValue = volumeValue
        self.year = year
        self.country = country
        self.price = price
        self.isAuction = isAuction
