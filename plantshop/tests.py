# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286

"""
These local tests can be used to test your implementation of classes Plant and PlantShop.

Feel free to modify these tests as you wish.
"""
import unittest
import random
from plantshop import Plant, PlantShop
#​​​​‌‌‌​‌‌‌‌‌​Some test that forces plants with identical names but distinct heights and vice versa?
plantAttrs = [("Aloe Vera", 35),
              ("Cactus", 7),
              ("Ficus", 30),
              ("Citrus", 40),
              ("Fern", 40),
              ("Dryopteris filix-mas", 50),
              ("Bonsai", 25),
              ("Heather", 20),
              ("Evergreen", 200),
              ("Yucca", 135)
            ]

class Test1Plant(unittest.TestCase):
    #​​​​‌‌‌​‌‌‌‌‌​ All methods starting with 'test' in a TestCase will be run as tests.

    def test1_equality(self):
        """Only identical plants are equal. (1p)"""
        size = len(plantAttrs)
        shuffledAttrs = random.sample(plantAttrs, size)
        i = random.randint(0, size - 1)
        n, h = shuffledAttrs[i]
        duplicate = Plant(n, h)
        duplicateName = Plant(n, h - random.randint(1, h - 1))
        duplicateHeight = Plant(n * 2, h)
        plants = [Plant(t[0], t[1]) for t in shuffledAttrs]
        plants += [duplicateName, duplicateHeight]

        for j in range(len(plants)):
            plant = plants[j]
            if j == i and plant == duplicate:
                #​​​​‌‌‌​‌‌‌‌‌​This is as it should
                pass
            elif j == i:
                self.fail(
                    """Identical plants should be equal,
                       but __eq__ returned False for plants
                       {} and {}."""
                       .format(plant, duplicate)
               )
            elif j != i and plant == duplicate:
                self.fail(
                  """Distinct plants should not be equal,
                     but __eq__ returned True for plants
                     {} and {}. Did you remember to compare
                     both attributes?"""
                     .format(plant, duplicate)
             )

            else:
                 #​​​​‌‌‌​‌‌‌‌‌​This is as it should
                 pass


    def test2_similar_objs_diff_hashes(self):
        """Similar but not identical plants don't result in same hash. (1p)"""
        name, height = random.choice(plantAttrs)
        plant1 = Plant(name, height)
        plant2 = Plant(name, height - random.randint(1, height-1) ) #Is only name hashed?
        plant3 = Plant(name * 2, height) #Or only height?
        weirdPlant = Plant(height, name) #swap attribute values or not because stupid case?
        others = [plant2, plant3, weirdPlant]
        for other in others:
            self.assertFalse(hash(other) == hash(plant1),
                """When comparing hashes of {} and {},
                   the hashes collided.
                   This may imply your __hash__ is poorly implemented.
                   Because builtin hash() collides with a miniscule probability
                   despite good __hash__ solution, the failure can
                   (although highly unlikely) also be bad luck.
                   You can run the tests a couple of times
                   to see if this is the case. (hash values of plant's name string
                   will change between runs.)
                   Use both attributes for hash creation.
                   Hashes should be unique although hashed plants are similar but not identical.
                   Don't combine individual hashes of attributes with mathematical operations
                   like summation. This approach results in collisions that would be easily avoided."""
                   .format(other, plant1)
            )


stockData = [(10, 4),
             (3, 5),
             (7, 2),
             (4, 8),
             (1, 5),
             (2, 16),
             (11, 11),
             (29, 5),
             (24, 12),
             (42, 81)
            ]

def random_plants(count):
    return [Plant(t[0], t[1]) for t in random.sample(plantAttrs, count)]

def random_stock_numbers(size):
    return random.sample(stockData, size)

def random_stock(size):
    plants = random_plants(size)
    stockNums = random_stock_numbers(size)
    return plants, stockNums, {p: s for (p, s) in zip(plants, stockNums)}

def second_ex_not_implemented():
    try:
        shop = PlantShop()
        shop.fillStock(Plant("Yucca", 135))
    except NotImplementedError:
        return True
    except:
        pass
    return False


@unittest.skipIf(second_ex_not_implemented(), "Second exercise is not implemented.")
class Test2PlantShop(unittest.TestCase):

    def test1_fill_stock(self):
        """Stock is updated correctly when calling fillStock(). (1p)"""
        shop = PlantShop()
        r = random.randint(4, 7)
        plants, stockNums, model_stock = random_stock(r)
        #​​​​‌‌‌​‌‌‌‌‌​Also test default quantity when not specified
        #​​​​‌‌‌​‌‌‌‌‌​Test default price or take it off?
        for i in range(r):
            q, p = stockNums[i]
            shop.fillStock(plants[i], q, p)
        #​​​​‌‌‌​‌‌‌‌‌​Convert to ordered lists for item to item matching?
        self.assertEqual(
            shop.stock,
            model_stock,
            """After adding {0} plants to stock
               your stock and model differ.
               your stock was:
               {1}
               The model was:
               {2}""".format(r, shop.stock, model_stock)
        )


    def test2_put_on_sale(self):
        """Plants are added on sale correctly. (1p)"""
        r = random.randint(4, 7)
        plants, stockNums, test_stock = random_stock(r)
        shop = PlantShop(test_stock)
        r2 = random.randint(1, r)
        modelSale = set(random.sample(plants, r2) )
        for p in modelSale:
            shop.putOnSale(p)
        self.assertEqual(
            shop.salePlants(),
            modelSale,
            """After putting {0} plants on sale
               your sale and model differ.
               your sale was:
               {1}
               The model was:
               {2}""".format(r2, shop.salePlants(), modelSale)
        )


    def test3_remove_from_sale(self):
        """Plants are removed from sale correctly. (1p)"""
        r = random.randint(6, 10)
        plants, stockNums, test_stock = random_stock(r)
        shop = PlantShop(test_stock)
        r2 = random.randint(3, r)
        modelSale = random.sample(plants, r2)
        r3 = random.randint(1, r2)

        for p in modelSale:
            shop.putOnSale(p)

        toRemove = random.sample(modelSale, r3)

        for p in toRemove:
            shop.removeFromSale(p)
            modelSale.remove(p)

        submissionSale = shop.salePlants()
        #​​​​‌‌‌​‌‌‌‌‌​Convert to set for equality comparison
        modelSet = set(modelSale)

        self.assertEqual(
            submissionSale,
            modelSet,
            """After removing {0} plants from sale
               your sale and model differ.
               Your sale was:
               {1}
               The model was:
               {2}""".format(r3, submissionSale, modelSet)
        )


    def test4_sell_full_price(self):
        """Selling plants not on sale updates stock and assets accordingly. (1p)"""
        r = random.randint(4, 10)
        plants, stockNums, test_stock = random_stock(r)
        shop = PlantShop(test_stock)
        sold = []
        for (plant, stockRecord) in zip(plants, stockNums):
            soldCount = random.randint(1, stockRecord[0])
            shop.sell(plant, soldCount)
            sold.append(soldCount)

        valueSold = 0.0
        for (plant, oldStockRecord, soldPieces) in zip(plants, stockNums, sold):
            newQuantity, price = shop.stockInfo(plant)
            oldQuantity = oldStockRecord[0]
            oldUpdated = oldQuantity - soldPieces
            valueSold += soldPieces * price
            self.assertEqual(
                oldUpdated,
                newQuantity,
                """After selling {0} pieces of plant {1},
                   there should be {2} pieces in stock.
                   However, there were {3}."""
                   .format(soldPieces, plant, oldUpdated, newQuantity)
            )

        self.assertAlmostEqual(
            shop.assetInfo(),
            valueSold,
            3,
            """After selling plants for {0} euros,
               there should be an equal amount of assets.
               However the shop's assets were {1}."""
               .format(valueSold, shop.assetInfo())
        )


    def test5_sell_on_sale(self):
        """Selling plants on sale updates stock and assets correctly. (1p)"""
        r = random.randint(4, 10)
        plants, stockNums, test_stock = random_stock(r)
        shop = PlantShop(test_stock)
        r2 = random.randint(1, r)
        modelSale = random.sample(plants, r2)
        modelSet = set(modelSale)
        saleStock = [test_stock[x] for x in modelSale]

        sold = []

        for (plant, stockNumbers) in zip(modelSale, saleStock):
            shop.putOnSale(plant)
            soldCount = random.randint(1, stockNumbers[0])
            shop.sell(plant, soldCount)
            sold.append(soldCount)

        valueSold = 0.0

        for (plant, oldStock, soldPieces) in zip(modelSale, saleStock, sold):
            newQuantity, fullPrice = shop.stockInfo(plant)
            oldQuantity = oldStock[0]
            oldUpdated = oldQuantity - soldPieces
            valueSold += 0.8 * soldPieces * fullPrice
            self.assertEqual(
                oldUpdated,
                newQuantity,
                """After selling {0} pieces of plant {1} that is on sale,
                   there should be {2} pieces in stock.
                   However, there were {3}."""
                   .format(soldPieces, plant, oldUpdated, newQuantity)
            )

        self.assertAlmostEqual(
            shop.assetInfo(),
            valueSold,
            3,
            """After selling plants on sale for {0} euros,
               there should be an equal amount of assets.
               However the shop's assets were {1}."""
               .format(valueSold, shop.assetInfo())
        )


    def test6_available(self):
        """available() returns correct plants. (1p)"""
        r = random.randint(5, 10)
        r2 = random.randint(2, r-1)
        plants = random_plants(r)
        availableNums = random_stock_numbers(r2)
        availablePlants = plants[:r2]
        soldOut = plants[r2:]
        availableStock = {p: s for (p, s) in zip(availablePlants, availableNums)}
        outStock = {p: (0, 1) for p in soldOut}
        testStock = availableStock.copy() #Merge availableStock and outStock
        testStock.update(outStock)
        shop = PlantShop(testStock)

        availableRes = shop.available()
        resLength = len(availableRes)
        modelLength = len(availablePlants)

        self.assertEqual(
            resLength,
            modelLength,
            """There should be {0} available plants,
               but there were {1}."""
               .format(modelLength, resLength)
        )

        #​​​​‌‌‌​‌‌‌‌‌​Implement <= to plant for better testing?

        resSet = set(availableRes)
        modelSet = set(availablePlants)

        self.assertEqual(
            resLength,
            len(resSet),
            """Set made of returned available plants
               had length {0} but the returned list
               had length {1}. It seems that there were
               duplicate plants in the list returned."""
               .format(len(resSet), resLength)
        )

        self.assertEqual(
            resSet,
            modelSet,
            """After creating sets from model and
               returned plant list, the contents differ.
               Model had plants:
               {0}
               available() returned:
               {1}"""
               .format(modelSet, resSet)

        )


#​​​​‌‌‌​‌‌‌‌‌​ The if checks below prevent the tests from being run if this file is for example imported
#​​​​‌‌‌​‌‌‌‌‌​ True when running tests from the command line or the Eclipse PyDev unittest tool
if __name__ in ("__main__", "tests"):
    import sys
    #​​​​‌‌‌​‌‌‌‌‌​ If this test is being run with a Python version that is older than version 3,
    #​​​​‌‌‌​‌‌‌‌‌​ raise an exception. This skips the tests.
    if sys.version_info.major < 3:
        class VersionError(BaseException): pass
        raise VersionError("You are using Python version {:d}.{:d}, please use version 3 instead."
                           .format(sys.version_info.major, sys.version_info.minor))


#​​​​‌‌‌​‌‌‌‌‌​ True when running tests from the command line
if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​ Run the tests with increased output verbosity.
    #​​​​‌‌‌​‌‌‌‌‌​ You can change the verbosity to for example 1 and see what happens.
    unittest.main(verbosity = 2)

