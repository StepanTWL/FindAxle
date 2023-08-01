from unittest import TestCase, main
from test3 import find_axle


class find_axle_test(TestCase):
    def test_0001(self): # minus axle
        str1 = '00000'
        str2 = '11100'
        str3 = '111'
        str4 = '000'
        self.assertEqual(find_axle(str1, str2, len(str1), False), 0)
        self.assertEqual(find_axle(str3, str4, len(str3), False), 1)
        find_axle()
        self.assertEqual(find_axle(str2, str1, len(str1), False), 0)
        self.assertEqual(find_axle(str4, str3, len(str3), False), -1)
        find_axle()

    def test_0002(self): # minus axle
        str1 = '00000111'
        str2 = '11100000'
        str3 = '00000111'
        str4 = '11100000'
        self.assertEqual(find_axle(str1, str2, len(str1), False), 1)
        self.assertEqual(find_axle(str3, str4, len(str3), False), 2)
        find_axle()
        self.assertEqual(find_axle(str2, str1, len(str1), False), -1)
        self.assertEqual(find_axle(str4, str3, len(str3), False), -2)
        find_axle()

    def test_0003(self): # minus axle
        str1 = '1111110000001111110'
        str2 = '0001111110000001111'
        str3 = '00000111111000000111111'
        str4 = '11000000111111000000111'
        self.assertEqual(find_axle(str1, str2, len(str1), False), 1)
        self.assertEqual(find_axle(str3, str4, len(str3), False), 3)
        find_axle()
        self.assertEqual(find_axle(str2, str1, len(str1), False), -1)
        self.assertEqual(find_axle(str4, str3, len(str3), False), -3)
        find_axle()

    def test_0004(self): # minus axle
        str1 = '1111110'
        str2 = '0001111'
        str3 = '0000011'
        str4 = '1100000'
        str5 = '11110'
        str6 = '01111'
        str7 = '00000111'
        str8 = '11000000'
        str9 = '111000000'
        str10 = '111111000'
        str11 = '111111'
        str12 = '000111'
        self.assertEqual(find_axle(str1, str2, len(str1), False), 0)
        self.assertEqual(find_axle(str3, str4, len(str3), False), 0)
        self.assertEqual(find_axle(str5, str6, len(str5), False), 1)
        self.assertEqual(find_axle(str7, str8, len(str7), False), 2)
        self.assertEqual(find_axle(str9, str10, len(str9), False), 2)
        self.assertEqual(find_axle(str11, str12, len(str11), False), 3)
        find_axle()
        self.assertEqual(find_axle(str2, str1, len(str1), False), 0)
        self.assertEqual(find_axle(str4, str3, len(str3), False), 0)
        self.assertEqual(find_axle(str6, str5, len(str5), False), -1)
        self.assertEqual(find_axle(str8, str7, len(str7), False), -2)
        self.assertEqual(find_axle(str10, str9, len(str9), False), -2)
        self.assertEqual(find_axle(str12, str11, len(str11), False), -3)
        find_axle()


if __name__ == '__main__':
    main()