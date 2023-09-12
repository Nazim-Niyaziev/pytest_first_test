import time


def test_task_example(selenium):
    """ Test that the email input field indicator works correctly"""

    # Open main page:
    selenium.get('https://outsourcing.ankhora.co.uk/')

    time.sleep(2)

    # Click Send button:
    send_button = selenium.find_element_by_xpath('//*[@id="post-589"]/div/div/section[2]/div/div[3]/div/div[3]/div/div/div[1]/div[1]/a')
    send_button.click()

    time.sleep(2)

    # Find the field for firstname input:
    firstname_input = selenium.find_element_by_id("wpforms-551-field_0")

    # Enter firstname:
    firstname_input.clear()
    firstname_input.send_keys('Nazym')

    # Find the field for lastname input:
    lastname_input = selenium.find_element_by_id("wpforms-551-field_0-last")

    # Enter lastname:
    lastname_input.clear()
    lastname_input.send_keys('Niyaziev')

    time.sleep(1)

    # Find the field for email input:
    email_input = selenium.find_element_by_id("wpforms-551-field_1")

    # Enter correct email:
    email_input.clear()
    email_input.send_keys('n.niyaziev@gmail.com')

    time.sleep(3)

    # Make the first screenshot of browser window:
    selenium.save_screenshot('correct_email.png')

    # Enter incorrect email:
    email_input.clear()
    email_input.send_keys('gmail.com')

    time.sleep(3)

    # Click to another field:
    lastname_input.click()

    time.sleep(1)

    # Make the second screenshot of browser window:
    selenium.save_screenshot('incorrect_email.png')