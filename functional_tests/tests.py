from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(5)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_form_and_send_info_correctly(self):
		# Joe has some cranes that he needs to inspect so
		# he goes to a website to check out some software
		self.browser.get(self.live_server_url)

		# He notices the page title and header 
		# mention the company name
		self.assertIn('Northwestern Machinery', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Northwestern Machinery', header_text)

		# He is instructed to provide his name and email
		# address to access the software downloads
		inputbox = self.browser.find_element_by_id('id_name')
		self.assertEqual(inputbox.get_attribute('placeholder'),
			'Enter Your Name'
			)

		# He types his name into the name field
		inputbox.send_keys('Joe')

		# When he hits enter it moves him into the email field
		inputbox.send_keys(Keys.ENTER)
		
		# He sees the next input box asks for his email address
		inputbox = self.browser.find_element_by_id('id_email')
		self.assertEqual(inputbox.get_attribute('placeholder'),
			'Enter Your Email Address'
			)

		# He types his email into the email field
		inputbox.send_keys('joe@email.com')

		# When he hits enter it takes him to the page 
		# that has links to the software downloads
		inputbox.send_keys(Keys.ENTER)
		self.assertEqual('Software Download', self.browser.title)

		# He notices that the page title and 
		# header mention the software
		self.fail('Finish the test!')

	# Pleased with his software download he exits the 
	# browser and tells all his friends about the website

