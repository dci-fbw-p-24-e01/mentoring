
import unittest


def addition(num1, num2):
    return num1 + num2

def multiplication(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError('You cannot divide by 0')
    return num1 / num2


class TestCalculator(unittest.TestCase):

    def test_addition_positive_numbers(self):
        self.assertEqual(addition(100, 200), 300)
    
    def test_addition_negative_numbers(self):     
        self.assertEqual(addition(-100, -50), -150)
        self.assertEqual(addition(-100, 0), -100)

    def test_multiplication(self):
        self.assertEqual(multiplication(100, 200), 20000)

    def test_division(self):
        self.assertEqual(divide(200, 100), 2)
        

        with self.assertRaises(ValueError):
            divide(333, 0)
            self.assertEqual(divide(200, 0), 2)
            self.assertEqual(divide(200, 0), 2)






def findmaximum(arr):
    # if type(arr) is not list:
    #     raise TypeError('The argument must be a list.')
    # elif arr == []:
    #     raise ValueError('The list is empty')
    return max(arr)


# print(findmaximum([23, 50, 2, 7, 44, 1011, 505, 20, 1]))

arr_list = [23, 50, 2, 7, 44, 1011, 505, 20, 1]
arr_empty = []


class TestMaximum(unittest.TestCase):

    def setUp(self):
        sport = 'Football is my favourite sport.'
        print(sport)

    def tearDown(self):
        food = 'Roasted beef and dunkel beer.'
        print(food)

    def test_findmaximum_with_list(self):
        self.assertEqual(findmaximum(arr_list), 1011)

    def test_findmaximum_with_empty_list(self):
        with self.assertRaises(ValueError):
            findmaximum(arr_empty)
          

    def test_findmaximum_with_number(self):
        with self.assertRaises(TypeError):
            findmaximum(300)

    def test_findmaximum_with_one_item(self):
        self.assertEqual(findmaximum([800]), 800)

    def test_findmaximum_with_negative_numbers(self):
        self.assertEqual(findmaximum([-34, -2, -60, -100, -55]), -2)
    
            


class ProductsDatabase:

    def connect(self):
        self.connection = True
        return self.connection

    def disconnect(self):
        self.connection = False
        return self.connection

    def fetchdata(self):
        return {'data': 'laptop'}
    

class TestProductsDatabase(unittest.TestCase):

    def setUp(self):
        self.db = ProductsDatabase()
        self.db.connect()

    def tearDown(self):
        self.db.disconnect()  

    def test_fetchdata(self):       
        self.assertEqual(self.db.fetchdata(), {'data': 'laptop'})


    def test_connection(self):
        self.assertTrue(self.db.connect())

    def test_disconnection(self):
        self.assertFalse(self.db.disconnect())


    # Homework

    def test_fetchdata_when_disconnected(self):
        self.db.disconnect()
        self.assertEqual(self.db.fetchdata(), {'data': 'laptop'})

        #with self.assertRaises()


    












if __name__ == '__main__':
    unittest.main()
