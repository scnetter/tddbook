from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
  
  def setUp(self):
    self.browser = webdriver.Chrome('Users/knetterv/Documents/chromedriver')
    self.browser.implicitly_wait(3)
  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    # A user visits the home page of the todo-list app
    self.browser.get('http://localhost:8000')

    # The user should see the title and header mention To-Do lists
    self.assertIn('To-Do', self.browser.title)
    self.fail('Finish the test!')  
    # The user is invited to enter a to-do item in immediately
    
    # The user types "Buy peacock feathers" into a text box (because
    # they have a weird hobby)

    # When the user hits enter, the page updates and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting the user to add another time. The
    # user enters "Use peacock feathers to make a fly"

    # The page updates again and now shows both items in the list.

    # The site generates a unique URL for the user's list -- there is
    # explanatory text to that effect.

    # The user visits the URL - their specific to-do list is still there

    # end of tests
    browser.quit()

if __name__ == '__main__':
  unittest.main(warnings='ignore')