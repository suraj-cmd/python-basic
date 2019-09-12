import unittest
from unittest.mock import patch
from employee import employee


class Testemployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod  # decorator A function returning another function
    def tearDownClass(cls):
            print('tearDownClass')

    def setUp(self):
            print('setUp')
            self.emp_1 = employee('suraj', 'patil', 600000)
            self.emp_2 = employee('test', 'employee', 500000)

    def tearDown(self):
            print('tearDown')

    def test_email(self):
            self.assertEqual(self.emp_1.email, 'suraj.patil@email.com')
            self.assertEqual(self.emp_2.email, 'test.employee@email.com')

    def test_fullname(self):
            self.assertEqual(self.emp_1.fullname, 'suraj.patil')
            self.assertEqual(self.emp_2.fullname, 'test.employee')

if __name__ == '__main__':
    unittest.main()
