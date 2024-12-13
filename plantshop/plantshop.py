# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Exercise that trains using hash, dicts, sets and __eq__ and __hash__ implementation for a custom class."""
#​​​​‌‌‌​‌‌‌‌‌​ A class to describe a plant object
#​​​​‌‌‌​‌‌‌‌‌​ A plant object has the following attributes: name and height

class Plant:
    """A class describing plants in simple terms.
       Class instances are immutable to ensure
       that a plant's hash is constant and thus
       compatible to use in dicts and sets."""

    __slots__ = ("name", "height")

    def __init__(self, name, height):
        """A more complicated __init__
        to produce immutable objects.
        Similar to
        self.name = name
        self.height = height."""
        super().__setattr__("name", name)
        super().__setattr__("height", height)

    def __setattr__(self, name, value):
        """Inform that attributes of plant can't be altered."""
        raise AttributeError("Can't alter a plant after initialization.")

    def __str__(self):
        """A string representation of plant for e.g. printing."""
        return "{}: {} cm".format(self.name, self.height)

    def __repr__(self):
        """A string method called when printing
        a container (e.g. a list) that contains
        plants."""
        return self.__str__()

    def __eq__(self, other):
        """Determine if a plant is equal to other
           plant by comparing attributes.
           Return boolean comparison result."""
        return self.name == other.name and self.height == other.height

    def __hash__(self):
        """Return a hash for plant instance. Hash
        of plant is created by calling builtin hash() for
        its attributes combined.
        """
        return hash( (self.name, self.height) )


#​​​​‌‌‌​‌‌‌‌‌​ A class to describe a plant shop object
#​​​​‌‌‌​‌‌‌‌‌​ A plant shop object has the following attributes: stock, onSale, discount and assets
#​​​​‌‌‌​‌‌‌‌‌​ Implement the missing functions below

class PlantShop():
    def __init__(self, stock=None):
        """Plantshop's stock
           is a dict that stores information
           of sold plants, their
           quantities in stock and prices.
           Each key plant has a tuple
           (quantity, price) as corresponding value.
           E.g. stock = {plant1: (quantity1, price1), plant2: (quantity2, price2), ...}
           """
        if stock:
            self.stock = stock
        else:
            self.stock = dict()
        """onSale is a set containing plants that are put on sale.
           In other words the set is of form:
           onSale = {plant1, plant2, ...}.
           Plants that are on sale are sold for stock prices
           discounted with a common discount
           procent defined below."""
        self.onSale = set()
        self.discount = 20 #A common discount procent for items on sale.
        self.assets = 0.0 #Profits from sold plants are stored here

    def salePlants(self):
        """Return a copy of plants on sale."""
        return {x for x in self.onSale}

    def stockInfo(self, plant):
        """Return the tuple containing quantity and price for plant."""
        return self.stock[plant]

    def assetInfo(self):
        """Return current assets."""
        return self.assets

    def fillStock(self, plant, quantity=1, price=1):
        """Add plants to stock. If the plant is
        already found in the stock dict, its
        quantity data is updated and the old price
        is kept. In this case the price parameter is omitted.
        If the plant is a new one, it will be stored as a new
        key to stock, having given quantity
        and price as its corresponding value tuple."""

        raise NotImplementedError("Fix me!")


    def sell(self, plant, pieces=1):
        """Sell one or multiple plants of same kind.
           This means:
           -removing the pieces sold from stock
           -adding the money obtained to assets
           Money obtained depends on pieces sold, plant price and possible
           discount if plant happens to be on sale.
           For plants on sale, the actual price is
           reached with normal procent calculation."""
        raise NotImplementedError("Fix me!")

    def putOnSale(self, plant):
        """Add a plant to items on sale."""
        raise NotImplementedError("Fix me!")


    def removeFromSale(self, plant):
        """Remove a plant from items on sale."""
        raise NotImplementedError("Fix me!")

    def available(self):
        """Return a list of plants that are not sold out."""
        raise NotImplementedError("Fix me!")
        return []

#​​​​‌‌‌​‌‌‌‌‌​ Simple usage example
def main():
    a = Plant("Bonsai", 20)
    b = Plant("Fern", 40)
    c = Plant("Palm tree", 400)
    d = Plant("Fern", 50)
    e = Plant("Yucca", 180)
    prices = [10,
              7, 100, 9, 30]

    store = PlantShop()

    #​​​​‌‌‌​‌‌‌‌‌​ Create a list of tuples (Plant, integer)
    for plant, pr in zip([a, b, c, d, e], prices):
        store.fillStock(plant, price=pr)

    store.sell(e)

    print(store.stockInfo(e))

if __name__ == "__main__":
    main()

