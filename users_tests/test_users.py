import unittest
from users import get_users, get_user
from unittest.mock import patch, Mock

class BasicTests(unittest.TestCase):
	#def test_request_response(self):
	#	response = get_users()

	# assert that the request-response cycle completed successfully with status code 200
	#	self.assertEqual(response.status_code, 200)

	@patch('users.requests.get') # mock 'requests' module 'get' method
	def test_request_response_with_decorator(self,mock_get):
		"""Mocking using a decorator"""
		mock_get.return_value.status_code = 200
		response = get_users()

		# assert that the request-response cycle completed successfully with status code 200
		self.assertEqual(response.status_code,200)


	# .... more tests
	def test_request_response_with_context_manager(self):
		"""Mocking using a context manager"""
		with patch('users.requests.get') as mock_get:
			#configure the mock to return a response with a status of 200
			mock_get.return_value.status_code = 200

			#call the function, which will send a request to the server
			response = get_users()

		# assert that the request-response cycle completed successfully with status code 200
		self.assertEqual(response.status_code,200)

	# ... further testing
	def test_request_response_with_patcher(self):
		"""Mocking using a patcher """
		mock_get_patcher = patch('users.requests.get')

		# start patching 'requests.get'.
		mock_get = mock_get_patcher.start()

		#configure the mock to return a response with a status of 200
		mock_get.return_value.status_code = 200

		# call the service which will send a request to the server
		response = get_users()

		# stop patching 'requests'
		mock_get_patcher.stop()

		# assert that the request-response cycle completed successfully with status code 200
		self.assertEqual(response.status_code,200)		

	#... ultimate test for the whole mock function
	def test_mock_whole_function(self):
		"""Mocking a whole function """
		mock_get_patcher = patch('users.requests.get')

		users = [{
			"id": 0,
			"first_name": "Adrian",
			"last_name": "Francis",
			"phone": "254 727 440 297"

		}]

		# start patching 'requests.get'
		mock_get = mock_get_patcher.start()

		#configure the mock to return a response with a status of 200 and a list of all users
		mock_get.return_value = Mock(status_code = 200)
		mock_get.return_value.json.return_value = users

		#call the service that will send a request to the server
		response = get_users()

		# stop patching 'requests'
		mock_get_patcher.stop()

		# assert that the request-reponse cycle completed successfully
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json(), users)

	@patch('users.get_users')
	def test_get_one_user(self,mock_get_users):
		"""
		Test for getting one user using their userID Demonstrates mocking third party functions
		"""

		users = [
			{'phone':'254787654879','first_name':'Adrian', 'last_name': 'Francis'},
			{'phone':'254703678567','first_name':'Joy', 'last_name': 'Kare'},
			{'phone':'254799090890','first_name':'Vic', 'last_name': 'Mensa'}

		]

		mock_get_users.return_value = Mock()
		mock_get_users.return_value.json.return_value = users
		user = get_user(2)
		self.assertEqual(user, users[2]) 

if __name__ == "__main__":
	unittest.main()