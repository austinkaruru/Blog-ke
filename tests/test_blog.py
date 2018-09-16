import unittest
from app.blogs import Blog, User


class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(1234, 'Python Must Be Crazy',
                             'A thrilling new Python Series', '/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))


class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))
