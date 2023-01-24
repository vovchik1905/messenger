import unittest
from unittest.mock import patch
from main_functions import *

test_user = user('TEST_LOGIN_1', 0, 0, 4)

#во всех последующих тестах вы сверяем реальное изменение состояния пользователя с ожидаемым

class Teststart(unittest.TestCase):
    @patch('builtins.input', side_effect=['SING_IN'])
    def test_first_var(self, users:user):
        users.state = 0
        self.assertEqual(func.func0(users), 1)
    @patch('builtins.input', side_effect=['SING_UP'])
    def test_second_var(self, users:user):
        users.state = 0
        self.assertEqual(func.func0(users), 2)
    @patch('builtins.input', side_effect=['sing_in'])
    def test_incorrect(self, users:user):
        users.state = 0
        self.assertEqual(func.func0(users), 0)

class TestLoginIn(unittest.TestCase):
    @patch('builtins.input', side_effect=['TEST_LOGIN_1'])
    def test_login_exist(self, users:user):
        users.state = 1
        self.assertEqual(func.func1(users), 3)
    @patch('builtins.input', side_effect=['NOT_EXIST'])
    def test_login_dont_exist(self, users:user):
        users.state = 1
        self.assertEqual(func.func1(users), 1)

class TestLoginUp(unittest.TestCase):
    @patch('builtins.input', side_effect=['TEST_LOGIN_1'])
    def test_login_exist(self, users:user):
        users.state = 2
        self.assertEqual(func.func2(users), 2)
    @patch('builtins.input', side_effect=['NOT_EXIST'])
    def test_login_dont_exist(self, users:user):
        users.state = 2
        self.assertEqual(func.func2(users), 4)

class PasswordIn(unittest.TestCase):
    @patch('builtins.input', side_effect=['111'])
    def test_correct_password(self, users:user):
        users.state = 3
        users.login = 'TEST_LOGIN_1'
        self.assertEqual(func.func3(users), 6)
    @patch('builtins.input', side_effect=['222'])
    def test_incorrect_password(self, users:user):
        users.state = 3
        users.login = 'TEST_LOGIN_1'
        self.assertEqual(func.func3(users), 3)

class PasswordUP(unittest.TestCase):
    @patch('builtins.input', side_effect=['111'])
    def test_correct_password(self, users:user):
        users.state = 5
        users.login = 'TEST_LOGIN_1'
        users.password = '111'
        self.assertEqual(func.func5(users), 6)
    @patch('builtins.input', side_effect=['222'])
    def test_incorrect_password(self, users:user):
        users.state = 5
        users.login = 'TEST_LOGIN_1'
        users.password = '111'
        self.assertEqual(func.func5(users), 5)


if __name__ == "__main__":
  unittest.main()
