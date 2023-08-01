from unittest import TestCase, main
from test2 import find_axle


class find_axle_test(TestCase):
    def test_0001(self): # minus axle
        str1 = '11110000001'
        str2 = '10000001111'
        self.assertEqual(find_axle(str1, str2, len(str1)), -1)
        self.assertEqual(find_axle(str2, str1, len(str1)), 1)

    def test_0002(self): # minus plus axle
        str1 = '111100000010000001111'
        str2 = '100000011111110000001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0003(self): #
        str1 = '100000111'
        str2 = '111100001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0004(self): #
        str1 = '1000000001'
        str2 = '1111001111'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0005(self): #
        str1 = '10000000001'
        str2 = '11110001111'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0006(self): #
        str1 = '10000000001'
        str2 = '10000001111'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0007(self): #
        str1 = '11100000001'
        str2 = '10000001111'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0008(self): #
        str1 = '11110000000001'
        str2 = '10000000011111'
        self.assertEqual(find_axle(str1, str2, len(str1)), -1)
        self.assertEqual(find_axle(str2, str1, len(str1)), 1)

    def test_0009(self): #
        str1 = '100000111000001111'
        str2 = '111100000111000001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 2)
        self.assertEqual(find_axle(str2, str1, len(str1)), -2)

    def test_0010(self): #
        str1 = '1000001110000001111'
        str2 = '1111000000111000001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 2)
        self.assertEqual(find_axle(str2, str1, len(str1)), -2)

    def test_0011(self): #
        str1 = '1000001111000001111'
        str2 = '1111000001111000001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 2)
        self.assertEqual(find_axle(str2, str1, len(str1)), -2)

    def test_0012(self): #
        str1 = '1000001111000001111'
        str2 = '1111000000111000001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 2)
        self.assertEqual(find_axle(str2, str1, len(str1)), -2)

    def test_0013(self): #
        str1 = '1000001110000001111'
        str2 = '1111000001111000001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 2)
        self.assertEqual(find_axle(str2, str1, len(str1)), -2)

    def test_0014(self): #
        str1 = '1000011110000001'
        str2 = '1111100000011111'
        self.assertEqual(find_axle(str1, str2, len(str1)), -1)
        self.assertEqual(find_axle(str2, str1, len(str1)), 1)

    def test_0015(self): #
        str1 = '10000111100001100001111001111'
        str2 = '01111000011110011110000110000'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0016(self): #
        str1 = '1111000011110000111100001111'
        str2 = '0011110000111100001111000011'
        self.assertEqual(find_axle(str1, str2, len(str1)), 0)
        self.assertEqual(find_axle(str2, str1, len(str1)), 0)

    def test_0017(self): #
        str1 = '111111000000111111000000111111000000111111'
        str2 = '000111111000000111111000000111111000000111'
        self.assertEqual(find_axle(str1, str2, len(str1)), 3)
        self.assertEqual(find_axle(str2, str1, len(str1)), -3)

    def test_0018(self): #
        str1 = '10000000000001111'
        str2 = '11110000111000001'
        self.assertEqual(find_axle(str1, str2, len(str1)), 1)
        self.assertEqual(find_axle(str2, str1, len(str1)), -1)


if __name__ == '__main__':
    main()