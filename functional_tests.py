from selenium import webdriver

browser = webdriver.Firefox()

# Joe has some cranes that he needs to inspect so he goes
# to a website to check out some software
browser.get('http://localhost:8000')

# He notices the page title and header mention the company name
assert 'Northwestern Machinery' in browser.title

# He is instructed to provide his name and email address
# to access the software downloads

# He types his name into the name field

# When he hits enter it moves him into the email field

# He types his email into the email field

# When he hits enter it takes him to the page that has links 
# to the software downloads

# He notices that the page title and header mention the software

# Pleased with his software download he exits the browser and
# tells all his friends about the website

browser.quit()
