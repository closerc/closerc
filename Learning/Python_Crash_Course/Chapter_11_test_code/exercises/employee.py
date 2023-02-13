"""一个可用于模拟雇员的类"""


class Employee():
    """增加雇员薪资"""
    def __init__(self, first, last, annual_salary):
        """雇员信息

        Args:
            first (str): 名
            last (str): 姓
            annual_salary (int): 年薪
        """
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        """年薪提升

        Args:
            salary_raise (int, optional): 年薪增加量. Defaults to 5000.
        """
        self.annual_salary += salary_raise
