import unittest

class IntegerArithmeticTestCase(unittest.TestCase):

        def testAdd(self):  # test method names begin with 'test'
            '''用例说明2222222222'''
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)

        def  testMultiply(self):
             '''用例说明2222222225555555555552'''
             self.assertEqual((0 * 10), 0)
             self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
        unittest.main()
