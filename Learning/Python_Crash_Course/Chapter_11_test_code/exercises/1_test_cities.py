# 测试city_function.py

import unittest

from city_function import get_city_country


class CityTestCase(unittest.TestCase):
    """测试city_function.py"""
    def test_city_country(self):
        """能够正确地处理像Santiago Chile这样的字符串吗？"""
        formatted_name = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')

    def test_city_country_population(self):
        """能够正确地处理像Santiago Chile-population 5000000这样的字符串吗？"""
        formatted_name = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago Chile-population 5000000')


unittest.main()
