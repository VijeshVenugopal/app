from django.test import TestCase,Client
from data.models import *
from django.contrib.auth.models import User

class YourTestClass(TestCase):

	@classmethod
	def setUpTestData(cls):
		print("setUpTestData: Run once to set up non-modified data for all class methods.")
		new_user = User.objects.create_user(
					username = 'nabeelta123@gmail.com',
					first_name = 'nabeel',
					last_name = 'thalakkatt',
					email = 'nabeelta123@gmail.com',
					password = '1',
					is_staff = 0,
					is_active = 1,
					is_superuser = 0
					)
		new_user.save()
		pass

	def setUp(self):
	    print("setUp: Run once for every test method to setup clean data.")
	    pass

	def test_false_is_false(self):
	    print("Method: test_false_is_false.")
	    self.assertFalse(False)

	def test_false_is_true(self):
	    print("Method: test_false_is_true.")
	    self.assertTrue(True)

	def test_one_plus_one_equals_two(self):
	    print("Method: test_one_plus_one_equals_two.")
	    self.assertEqual(1 + 1, 2)

	def test_login_success(self):
		print("Method: test_login_success")
		c = Client()
		response = c.login(username='nabeelta123@gmail.com', password='1')
		print response
		user = User.objects.filter(email='nabeelta123@gmail.com',is_active=True).exists()
		print "user exists? ",user
		self.assertTrue(response)
	def test_login_fails(self):
		print("Method: test_login_fails")
		c = Client()
		response = c.login(username = 'nabeelta123@gmail.com', password = '2')
		print response
		self.assertTrue(response)