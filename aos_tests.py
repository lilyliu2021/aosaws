import unittest
import aos_locators as locators
import aos_methods as methods


class AOSAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_aos():
        methods.setUp()
        methods.check_homepage()
        methods.create_new_account()
        methods.validate_new_account()
        print(f'------New account is created, Username is {locators.new_user_name}')
        methods.logout()
        methods.login()
        methods.validate_new_account()
        methods.logger('created')
        methods.checkout()
        methods.logout()
        methods.login()
        methods.validate_new_account()
        methods.view_cart()
        methods.cancel_order()
        methods.delete_account()
        methods.tearDown()