# 测试Employee类

import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    def setUp(self):
        """创建一个雇员对象，供使用的测试方法使用"""
        first = 'janis'
        last = 'joplin'
        annual_salary = 100000
        self.new_employee = Employee(first, last, annual_salary)

    def test_give_default_raise(self):
        """测试默认增加年薪可以通过"""
        self.new_employee.give_raise()
        self.assertEqual(105000, self.new_employee.annual_salary)

    def test_give_custom_raise(self):
        """测试自定义增加年薪可以通过"""
        self.new_employee.give_raise(10000)
        self.assertEqual(110000, self.new_employee.annual_salary)


unittest.main()
