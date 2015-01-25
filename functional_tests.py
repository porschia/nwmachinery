from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(5)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Joe has some cranes that he needs to inspect so he goes
		# to a website to check out some software
		self.browser.get('http://localhost:8000')

		# He notices the page title and header 
		# mention the company name
		self.assertIn('Northwestern Machinery', self.browser.title)
		self.fail('Finish the test!')

		# He is instructed to provide his name and email address
		# to access the software downloads

		# He types his name into the name field

		# When he hits enter it moves him into the email field

		# He types his email into the email field

		# When he hits enter it takes him to the page 
		# that has links to the software downloads

		# He notices that the page title and 
		# header mention the software

	# Pleased with his software download he exits the 
	# browser and tells all his friends about the website

if __name__ == '__main__':
	unittest.main(warnings='ignore')
