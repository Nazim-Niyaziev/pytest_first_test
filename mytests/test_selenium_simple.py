# import time
#
#
# def test_task_example(selenium):
#     """ Post some text in livejournal.com"""
#
#     # Open livejournal page:
#     selenium.get('https://www.livejournal.com')
#
#     time.sleep(2)
#
#     # Click Log in:
#     login_button = selenium.find_element_by_xpath('//*[@id="js"]/body/div[2]/header/div[1]/nav[2]/ul/li[2]/a')
#     login_button.click()
#
#     time.sleep(2)
#
#     # Find the field for login input:
#     login_input = selenium.find_element_by_id("user")
#
#     # Enter login:
#     login_input.clear()
#     login_input.send_keys('syneltest')
#
#     # Find the field for password input:
#     password_input = selenium.find_element_by_id("lj_loginwidget_password")
#
#     # Enter password:
#     password_input.clear()
#     password_input.send_keys('123qweASD')
#
#     time.sleep(1)
#
#     # Click Log in button:
#     log_in_button = selenium.find_element_by_name("action:login")
#     log_in_button.click()
#
#     time.sleep(1)
#
#     # Click Post button:
#     post_button = selenium.find_element_by_xpath('//*[@id="js"]/body/div[2]/header/div[1]/nav[2]/ul/li[4]/a')
#     post_button.click()
#
#     time.sleep(1)
#
#     # Find the field for title input:
#     title_input = selenium.find_element_by_css_selector('textarea.text-0-2-176')
#
#     # Enter title:
#     title_input.send_keys('Nazim Niyaziev')
#
#     # Find the field for post input:
#     post_text_input = selenium.find_element_by_xpath('//*[@id="editorWrapper"]/div[1]/div[2]/div/div/div[2]/div/span/br')
#
#     # Enter post text:
#     post_text_input.send_keys('Hey! I can do it!')
#
#     # Click Set and Post button:
#     set_post_button = selenium.find_element_by_xpath('/html/body/div[5]/footer/div/div/div[2]/div[2]/button')
#     set_post_button.click()
#
#     # Click Final Post button:
#     final_post_button = selenium.find_element_by_xpath('/html/body/div[5]/footer/div/div/div[2]/div[2]/div/footer/div/button')
#     final_post_button.click()
#
#     time.sleep(4)
#
#     # Make the screenshot of browser window:
#     selenium.save_screenshot('result.png')
#
