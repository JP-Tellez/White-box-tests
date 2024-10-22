# python -m unittest tests/test_book_store.py
# python -m unittest discover

import unittest
from unittest.mock import patch

from src.white_box import VendingMachine, TrafficLight, UserAuthentication, DocumentEditingSystem, ElevatorSystem, BankAccount, BankingSystem, Product, ShoppingCart
from src.white_box import categorize_product, validate_date, check_file_size, authenticate_user


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
        self.ba = BankAccount(1, 50)
        self.bs = BankingSystem()

    def test_init(self):
        ''' something '''






# class TestBook(unittest.TestCase):
#     ''' Book unittest class '''

#     def setUp(self):
#         self.title = "Title1"
#         self.author = "Author1"
#         self.price = 100
#         self.quantity = 50


#     def test_init(self):
#         title = "Title"
#         author = "Author"
#         price = 100
#         quantity = 50
#         the_book = Book(title, author, price, quantity)
#         self.assertEqual(the_book.title, title)
#         self.assertEqual(the_book.author, author)
#         self.assertEqual(the_book.price, price)
#         self.assertEqual(the_book.quantity, quantity)

#         # el prode uso el setUP para crear el libro
#         # book = Book(self.title, self.author, self.price, self.quantity)
#         # y ya luego los mismos assertEqual pero como assertEqual(book.title, self.title)


#     @patch('builtins.print')
#     def test_display(self, mock_print):
#         title = "Title"
#         author = "Author"
#         price = 100
#         quantity = 50
#         the_book = Book(title, author, price, quantity)

#         the_book.display()
#         mock_print.assert_any_call(f"Title: {title}")
#         mock_print.assert_any_call(f"Author: {author}")
#         mock_print.assert_any_call(f"Price: ${price}")
#         mock_print.assert_any_call(f"Quantity: {quantity}")

#         # Lo del profe
#         # lo mismo del patch y eso pero primero crea el book asi
#         # book = Book(self.title, self.author, self.price, self.quantity)
#         # book.display()
#         # self.assertTrue(mock_print.called) #Checa si fue llamado el print
#         # self.assertEqual(mock_print.call_count, 4) #Checa si se llamo 4 veces
#         # mock_print.assert_any_call(f"Title: {title}") # el mismo que yo 
#         # assert any call significa que checa en cualquiera pero con que este
#         # mock_print.assert_called_with(f"Quantity: {quantity}") #Checa nomas el ultimo








    
# class TestBookStore(unittest.TestCase):
#     '''BookStore unittest class'''

#     def test_init(self):
#         bookstore = BookStore()
#         self.assertEqual(bookstore.books, [])
    

#     def test_add_book(self):
#         bookstore = BookStore()
#         book = Book("Title", "Author", 100, 50)

#         bookstore.add_book(book)

#         self.assertEqual(bookstore.books[0].title, "Title")
#         self.assertEqual(bookstore.books[0].author, "Author")
#         self.assertEqual(bookstore.books[0].price, 100)
#         self.assertEqual(bookstore.books[0].quantity, 50)

#         # Rodrigo
#         self.assertIn(book, bookstore.books)
#         # or
#         self.assertEqual(bookstore.books[0], book)


#     @patch('src.book_store.Book.display')
#     def test_display_books_w_books(self, mock_print):
#         ''' In process '''
#         bookstore = BookStore()
#         book1 = Book("Title1", "Author1", 100, 50)
#         book2 = Book("Title2", "Author2", 100, 50)
#         book3 = Book("Title3", "Author3", 100, 50)

#         # idk if you can use add_book in here (not recomended)
#         bookstore.add_book(book1)
#         bookstore.add_book(book2)
#         bookstore.add_book(book3)

#         bookstore.display_books()

#         # mock_print.assert_any_call("Books available in the store:")
#         # mock_print.assert_any_call("Title: Title1")
#         # mock_print.assert_any_call("Title: Title2")
#         # mock_print.assert_any_call("Title: Title3")
#         self.assertEqual(mock_print.call_count, 3)





#     @patch('builtins.print')
#     def test_display_books_no_books(self, mock_print):
#         ''' In process '''
#         # display is not called

#         bookstore = BookStore()
#         # book1 = Book("Title1", "Author1", 100, 50)
#         # book2 = Book("Title2", "Author2", 100, 50)
#         # book3 = Book("Title3", "Author3", 100, 50)

#         bookstore.display_books()

#         mock_print.assert_any_call("No books in the store.")


#     @patch('builtins.print')
#     def test_search_book_found(self, mock_print):
#         bookstore = BookStore()
#         book1 = Book("Title1", "Author1", 100, 50)
#         book2 = Book("Title2", "Author2", 100, 50)
#         book3 = Book("Title3", "Author3", 100, 50)

#         # idk if you can use add_book in here
#         bookstore.add_book(book1)
#         bookstore.add_book(book2)
#         bookstore.add_book(book3)

#         bookstore.search_book("Title1")

#         mock_print.assert_any_call("Found 1 book(s) with title 'Title1':")
#         # mock_print.assert_any_call("Found 1 book(s) with title 'Title1':")


#     @patch('builtins.print')
#     def test_search_book_not_found(self, mock_print):
#         bookstore = BookStore()
#         book1 = Book("Title1", "Author1", 100, 50)
#         book2 = Book("Title2", "Author2", 100, 50)
#         book3 = Book("Title3", "Author3", 100, 50)

#         # idk if you can use add_book in here
#         bookstore.add_book(book1)
#         bookstore.add_book(book2)
#         bookstore.add_book(book3)

#         bookstore.search_book("Title4")

#         mock_print.assert_any_call("No book found with title 'Title4'.")


# # falto agregar cuando no hay libros e intentas buscar
