import unittest

from python_repos import get_response


class TestPythonRepos(unittest.TestCase):
    """测试python_repos.py"""
    def test_status_code(self):
        """能够正确的核实API调用成功吗"""
        self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        status_code = get_response(self.url).status_code
        self.assertEqual(status_code, 200)


unittest.main()
