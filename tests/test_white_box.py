# python -m unittest tests/test_white_box.py
# python -m unittest discover 

import unittest
from unittest.mock import patch

from src.white_box import *


class TestFirstFour(unittest.TestCase):
    ''' Test Cases for the first excercises '''

    # categorize_product
    def test_categorize_product_A(self):
        category = categorize_product(30)
        self.assertEqual(category, "Category A")

    def test_categorize_product_B(self):
        category = categorize_product(70)
        self.assertEqual(category, "Category B")

    def test_categorize_product_C(self):
        category = categorize_product(150)
        self.assertEqual(category, "Category C")

    def test_categorize_product_D(self):
        category = categorize_product(1)
        self.assertEqual(category, "Category D")
    

    # validate_date
    def test_validate_date_Valid(self):
        date = validate_date(2000, 10, 15)
        self.assertEqual(date, "Valid Date")
        
    def test_validate_date_Invalid(self):
        date = validate_date(2200, 10, 15)
        self.assertEqual(date, "Invalid Date")
    

    # check_file_size
    def test_check_file_size_valid(self):
        size = check_file_size(500)
        self.assertEqual(size, "Valid File Size")
    
    def test_check_file_size_invalid(self):
        size = check_file_size(2000000)
        self.assertEqual(size, "Invalid File Size")


    # authenticate_user
    def test_authenticate_user_admin(self):
        user = authenticate_user("admin", "admin123")
        self.assertEqual(user, "Admin")

    def test_authenticate_user_user(self):
        user = authenticate_user("123456", "12345678")
        self.assertEqual(user, "User")

    def test_authenticate_user_invalid(self):
        user = authenticate_user("1234", "1234")
        self.assertEqual(user, "Invalid")
        


class TestVendingMachine(unittest.TestCase):
    ''' VendingMachine unittest class '''

    def setUp(self):
        self.vm = VendingMachine()


    def test_init(self):
        self.assertEqual(self.vm.state, "Ready")

    def test_insert_coin_valid(self):
        elreturn = self.vm.insert_coin()
        self.assertEqual(self.vm.state, "Dispensing")
        self.assertEqual(elreturn, "Coin Inserted. Select your drink.")

    def test_insert_coin_invalid(self):
        self.vm.insert_coin()
        elreturn = self.vm.insert_coin()
        self.assertEqual(self.vm.state, "Dispensing")
        self.assertEqual(elreturn, "Invalid operation in current state.")

    def test_select_drink_valid(self):
        self.vm.state = "Dispensing"
        elreturn = self.vm.select_drink()
        self.assertEqual(self.vm.state, "Ready")
        self.assertEqual(elreturn, "Drink Dispensed. Thank you!")

    def test_select_drink_invalid(self):
        elreturn = self.vm.select_drink()
        self.assertEqual(elreturn, "Invalid operation in current state.")
        

class TestTrafficLight(unittest.TestCase):
    ''' TrafficLight unittest class '''

    def setUp(self):
        self.tl = TrafficLight()

    def test_init(self):
        self.assertEqual(self.tl.state, "Red")

    def test_change_state_all(self):
        self.tl.change_state()
        self.assertEqual(self.tl.state, "Green")
        self.tl.change_state()
        self.assertEqual(self.tl.state, "Yellow")
        self.tl.change_state()
        self.assertEqual(self.tl.state, "Red")
        self.tl.change_state()
        self.assertEqual(self.tl.state, "Green")
    
    def test_get_current_state(self):
        elstate = self.tl.get_current_state()
        self.assertEqual(self.tl.state, elstate)
        self.assertEqual(elstate, "Red")


class TestUserAuthentication(unittest.TestCase):
    ''' User Authentication unittest class '''

    def setUp(self):
        self.ua = UserAuthentication()

    def test_init(self):
        self.assertEqual(self.ua.state, "Logged Out")

    def test_login_success(self):
        elreturn = self.ua.login()
        self.assertEqual(self.ua.state, "Logged In")
        self.assertEqual(elreturn, "Login successful")

    def test_login_invalid(self):
        self.ua.state = "something"
        elreturn = self.ua.login()
        # self.assertEqual(ua.state, "Logged In")
        self.assertEqual(elreturn, "Invalid operation in current state")

    def test_logout_success(self):
        self.ua.state = "Logged In"
        # or ua.login()
        elreturn = self.ua.logout()
        self.assertEqual(self.ua.state, "Logged Out")
        self.assertEqual(elreturn, "Logout successful")

    def test_logout_failed(self):
        elreturn = self.ua.logout()
        self.assertEqual(self.ua.state, "Logged Out")
        self.assertEqual(elreturn, "Invalid operation in current state")


class TestDocumentEditingSystem(unittest.TestCase):
    ''' DES unittest class '''

    def setUp(self):
        self.des = DocumentEditingSystem()

    def test_init(self):
        self.assertEqual(self.des.state, "Editing")

    def test_save_document_success(self):
        elreturn = self.des.save_document()
        self.assertEqual(self.des.state, "Saved")
        self.assertEqual(elreturn, "Document saved successfully")

    def test_save_document_failed(self):
        self.des.state = "Saved"
        elreturn = self.des.save_document()
        self.assertEqual(elreturn, "Invalid operation in current state")

    def test_edit_document_success(self):
        self.des.state = "Saved"
        elreturn = self.des.edit_document()
        self.assertEqual(self.des.state, "Editing")
        self.assertEqual(elreturn, "Editing resumed")

    def test_edit_document_failed(self):
        elreturn = self.des.edit_document()
        self.assertEqual(self.des.state, "Editing")
        self.assertEqual(elreturn, "Invalid operation in current state")

    
class TestElevatorSystem(unittest.TestCase):
    ''' ElevatorSystem unittest class '''

    def setUp(self):
        self.es = ElevatorSystem()
    
    def test_init(self):
        self.assertEqual(self.es.state, "Idle")
    
    def test_move_up_success(self):
        elreturn = self.es.move_up()
        self.assertEqual(elreturn, "Elevator moving up")
        self.assertEqual(self.es.state, "Moving Up")
    
    def test_move_up_failed(self):
        self.es.state = "something"
        elreturn = self.es.move_up()
        self.assertEqual(elreturn, "Invalid operation in current state")

    def test_move_down_success(self):
        elreturn = self.es.move_down()
        self.assertEqual(elreturn, "Elevator moving down")
        self.assertEqual(self.es.state, "Moving Down")
    
    def test_move_down_failed(self):
        self.es.state = "something"
        elreturn = self.es.move_down()
        self.assertEqual(elreturn, "Invalid operation in current state")
    
    def test_stop_success(self):
        self.es.state = "Moving Up"
        elreturn = self.es.stop()
        self.assertEqual(self.es.state, "Idle")
        self.assertEqual(elreturn, "Elevator stopped")
        self.es.state = "Moving Down"
        elreturn = self.es.stop()
        self.assertEqual(self.es.state, "Idle")
        self.assertEqual(elreturn, "Elevator stopped")
    
    def test_stop_failed(self):
        elreturn = self.es.stop()
        self.assertEqual(elreturn, "Invalid operation in current state")
    

    
class TestBankAccount(unittest.TestCase):
    ''' BankAccount unittest class '''

    def setUp(self):
        self.ba = BankAccount(1, 50)

    def test_init(self):
        number = 2
        balance = 100
        ba = BankAccount(number, balance)
        self.assertEqual(ba.account_number, 2)
        self.assertEqual(ba.balance, 100)
    
    @patch('builtins.print')
    def test_view_account(self, mock_print):
        self.ba.view_account()
        mock_print.assert_called_with("The account 1 has a balance of 50")


class TestBankingSystem(unittest.TestCase):
    ''' BankingSystem unittest class '''

    def setUp(self):
        self.bs = BankingSystem()

    def test_init(self):
        users = {"user123": "pass123"}
        self.assertEqual(users, self.bs.users)
        self.assertEqual(self.bs.logged_in_users, set())
    
    # authenticate
    @patch('builtins.print')
    def test_authenticate_success(self, mock_print):
        elreturn = self.bs.authenticate("user123", "pass123")
        self.assertIn("user123", self.bs.logged_in_users)
        mock_print.assert_called_with("User user123 authenticated successfully.")
        self.assertTrue(elreturn)
    
    @patch('builtins.print')
    def test_authenticate_logged(self, mock_print):
        self.bs.logged_in_users.add("user123")
        elreturn = self.bs.authenticate("user123", "pass123")
        mock_print.assert_called_with("User already logged in.")
        self.assertFalse(elreturn)
    
    @patch('builtins.print')
    def test_authenticate_failed(self, mock_print):
        elreturn = self.bs.authenticate("user123", "something")
        mock_print.assert_called_with("Authentication failed.")
        self.assertFalse(elreturn)

    @patch('builtins.print')
    def test_authenticate_not_found(self, mock_print):
        elreturn = self.bs.authenticate("something", "pass123")
        mock_print.assert_called_with("Authentication failed.")
        self.assertFalse(elreturn)

    # transfer_money
    @patch('builtins.print')
    def test_transfer_money_not_auth(self, mock_print):
        elreturn = self.bs.transfer_money("user123", "user456", 100, "regular")
        mock_print.assert_called_with("Sender not authenticated.")
        self.assertFalse(elreturn)

    @patch('builtins.print')
    def test_transfer_money_invalid_type(self, mock_print):
        self.bs.logged_in_users.add("user123")
        elreturn = self.bs.transfer_money("user123", "user456", 100, "something")
        mock_print.assert_called_with("Invalid transaction type.")
        self.assertFalse(elreturn)
    
    @patch('builtins.print')
    def test_transfer_money_regular(self, mock_print):
        self.bs.logged_in_users.add("user123")
        elreturn = self.bs.transfer_money("user123", "user456", 100, "regular")
        mock_print.assert_called_with("Money transfer of $100 (regular transfer) from user123 to user456 processed successfully.")
        self.assertTrue(elreturn)
    
    @patch('builtins.print')
    def test_transfer_money_express(self, mock_print):
        self.bs.logged_in_users.add("user123")
        elreturn = self.bs.transfer_money("user123", "user456", 100, "express")
        mock_print.assert_called_with("Money transfer of $100 (express transfer) from user123 to user456 processed successfully.")
        self.assertTrue(elreturn)
    
    @patch('builtins.print')
    def test_transfer_money_regular(self, mock_print):
        self.bs.logged_in_users.add("user123")
        elreturn = self.bs.transfer_money("user123", "user456", 100, "scheduled")
        mock_print.assert_called_with("Money transfer of $100 (scheduled transfer) from user123 to user456 processed successfully.")
        self.assertTrue(elreturn)

    @patch('builtins.print')
    def test_transfer_money_insufficient(self, mock_print):
        self.bs.logged_in_users.add("user123")
        elreturn = self.bs.transfer_money("user123", "user456", 1500, "regular")
        mock_print.assert_called_with("Insufficient funds.")
        self.assertFalse(elreturn)
    


class TestProduct(unittest.TestCase):
    ''' Producto unittest class '''

    def setUp(self):
        self.p = Product("apple", 10)

    def test_init(self):
        apple = Product("apple", 10)
        self.assertEqual(apple.name, "apple") # or only p.name
        self.assertEqual(apple.price, 10) # or only p.price
    
    @patch('builtins.print')
    def test_view_product(self, mock_print):
        self.p.view_product()
        mock_print.assert_called_with("The product apple has a price of 10")
    

class TestShoppingCart(unittest.TestCase):
    ''' ShoppingCart unittest class '''

    def setUp(self):
        self.p = Product("apple", 10)
        self.p2 = Product("pineapple", 5)
        self.sc = ShoppingCart()
    
    def test_init(self):
        self.assertEqual(self.sc.items, [])


    # add_product
    def test_add_product_new(self):
        self.sc.add_product(self.p, 5)
        self.assertEqual(len(self.sc.items), 1)
        self.assertEqual(self.sc.items[0]["product"], self.p)
        self.assertEqual(self.sc.items[0]["quantity"], 5)
    
    def test_add_product_existing(self):
        self.sc.add_product(self.p, 5)
        self.sc.add_product(self.p, 5)
        self.assertEqual(len(self.sc.items), 1)
        self.assertEqual(self.sc.items[0]["product"], self.p)
        self.assertEqual(self.sc.items[0]["quantity"], 10)
    
    def test_add_product_a_lot(self):
        self.sc.add_product(self.p, 5)
        self.sc.add_product(self.p2, 5)

        self.assertEqual(len(self.sc.items), 2)

        self.assertEqual(self.sc.items[0]["product"], self.p)
        self.assertEqual(self.sc.items[0]["quantity"], 5)
        self.assertEqual(self.sc.items[1]["product"], self.p2)
        self.assertEqual(self.sc.items[1]["quantity"], 5)
    

    # remove
    def test_remove_product_complete(self):
        self.sc.add_product(self.p, 5)
        self.sc.remove_product(self.p, 5)
        self.assertEqual(len(self.sc.items), 0)

    def test_remove_product_some(self):
        self.sc.add_product(self.p, 5)
        self.sc.remove_product(self.p, 3)

        self.assertEqual(len(self.sc.items), 1)

        self.assertEqual(self.sc.items[0]["product"], self.p)
        self.assertEqual(self.sc.items[0]["quantity"], 2)
        
    def test_remove_product_not_in_cart(self):
        self.sc.add_product(self.p, 5)
        self.sc.remove_product(self.p2, 3)

        self.assertEqual(len(self.sc.items), 1)

        self.assertEqual(self.sc.items[0]["product"], self.p)
        self.assertEqual(self.sc.items[0]["quantity"], 5)
    
    
    # View art
    @patch('builtins.print')
    def test_view_cart_one(self, mock_print):
        self.sc.add_product(self.p, 5)

        self.sc.view_cart()

        mock_print.assert_called_with("5 x apple - $50")

    @patch('builtins.print')
    def test_view_cart_lots(self, mock_print):
        self.sc.add_product(self.p, 5)
        self.sc.add_product(self.p2, 5)

        self.sc.view_cart()

        mock_print.assert_any_call("5 x apple - $50")
        mock_print.assert_any_call("5 x pineapple - $25")

    
    # checkout
    @patch('builtins.print')
    def test_checkout(self, mock_print):
        self.sc.add_product(self.p, 5)
        self.sc.add_product(self.p2, 5)

        self.sc.checkout()

        mock_print.assert_any_call("Total: $75")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")

