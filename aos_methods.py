import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
import datetime
import aos_locators as locators



# Using Selenium WebDriver, open the web browser.
#s = Service(executable_path='../chromedriver.exe')
#driver = webdriver.Chrome(service=s)
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def setUp():
    # print test start day and time;
    print('---------------------~*~---------------------')
    print(f'########### The test is started at {datetime.datetime.now()}')
    # Maximize the browser window.
    driver.maximize_window()
    # Add implicitly wait for 30 seconds
    driver.implicitly_wait(30)
    # Navigate to web page URL - https://advantageonlineshopping.com/ (Links to an external site.)
    driver.get(locators.home_page_url)
    print(f'{driver.current_url}')  # Tip: Use print(driver.current_url) to find the actual AOS Website URL
    print(f'{driver.title}')  # Tip: Use print(driver.title) to find the actual title.

    # Check URL and home page title are as expected.
    if driver.current_url == locators.home_page_url and driver.title == locators.home_page_title:
        print(f'{locators.home_page_url} launched successfully!')
        # print(f'The actual AOS website URL is {driver.current_url} and the actual title is {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.home_page_url} did not launch.Please check the code or website')
        print(f'Current URL is {driver.current_url}. Page title is {driver.title}')
        sleep(0.25)
        tearDown()


def tearDown():
    if driver is not None:
        print('---------------------~*~---------------------')
        print(f'########### The test is completed at {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# 5. Create Selenium Automated Scripts that will do the following
# Create New Account - using Faker library fake data
def create_new_account():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.5)
    # assert driver.find_element((By.ID,'registerPage')).is_displayed()
    # sleep(0.25)

    for i in range(len(locators.list_opt)):
        if locators.list_names[i]:
            driver.find_element(By.NAME, locators.list_names[i]).send_keys(locators.list_val[i])
            sleep(0.25)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)


# Validate New Account is created
def validate_new_account():
    # Validate New Account created (new username is displayed in the top menu)
    if driver.title == locators.home_page_title:
        sleep(0.25)
        assert driver.find_element(By.LINK_TEXT, locators.new_user_name).is_displayed()
        sleep(0.25)


def logout():
    # #Logout
    driver.find_element(By.LINK_TEXT, locators.new_user_name).click()
    #driver.find_element(By.XPATH, f'//@id="menuUserLink"/span[contains(.,"{new_user_name}")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(0.25)
    # driver.find_element(By.ID,'hrefUserIcon').click()
    # java_script=driver.find_element(By.XPATH,'//label[contains(.,Sign out")]')
    # driver.execute_script("argument[0].click()",java_script)
    # 6. Close the browser and display user-friendly messages.


# 1.  Add Login functionality
def login():
    driver.find_element(By.XPATH, '//span[contains(text(),"dvantage")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    assert driver.find_element(By.XPATH, '//button[contains(.,"SIGN IN")]').is_displayed()
    sleep(0.5)
    driver.find_element(By.NAME, 'username').send_keys(locators.new_user_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"SIGN IN")]').click()
    sleep(0.25)
    message = driver.find_element(By.XPATH,'//label[@id="signInResultMessage"]').text
    if message.find('Incorrect') != -1 :
        print('The user is valid or deleted')

def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('AOSmessage.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.new_email}\t'
          f'{locators.new_user_name}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


def check_homepage_text():
    if driver.title == locators.home_page_title:
        sleep(0.25)
        for i in range(len(locators.homepage_texts)):
            if locators.homepage_textid[i]:
                assert driver.find_element(By.ID,locators.homepage_textid[i]).is_displayed()
                sleep(0.25)
        # assert driver.find_element(By.ID,'speakersTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'laptopsTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'miceTxt').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.ID,'headphonesTxt').is_displayed()
        # sleep(0.25)
        print('Homepage texts are displayed!')


def check_shopnow_button():
    if driver.title == locators.home_page_title:
        sleep(0.25)
        for i in range(len(locators.homepage_texts)):
            if locators.homepage_textid[i]:
                driver.find_element(By.ID,locators.homepage_textid[i]).click()
                sleep(0.25)
                #path=locators.homepage_texts[i]
                #print(f'{path}')
                #assert driver.find_element(By.XPATH,'f//h3[contains(text(),"{path}")]').is_displayed()
                sleep(0.5)
                driver.find_element(By.XPATH,'//a[contains(text(),"HOME")]').click()
                sleep(0.25)
                #driver.get(locators.home_page_url)
                #sleep(0.25)
        print('Shop Now button are clickable')
        sleep(0.25)


def check_main_menu():
    if driver.title == locators.home_page_title:
    #for i in range(len(locators.homepage_menu)):
        # b = driver.find_element(By.XPATH, f'//a[contains(text(),{locators.homepage_menu[i]})]')
        b = driver.find_element(By.XPATH,"//a[contains(text(),'SPECIAL OFFER')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu SPECIAL OFFER is clickable')
        sleep(0.25)
        b = driver.find_element(By.XPATH, "//a[contains(text(),'POPULAR ITEMS')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu POPULAR ITEMS is clickable')
        sleep(0.25)
        b = driver.find_element(By.XPATH, "//a[contains(text(),'CONTACT US')]")
        driver.execute_script("arguments[0].click();", b)
        print('Menu CONTACT US is clickable')
        sleep(0.25)

    print('menu item are clickable')


def check_mainlogo():
    if driver.title == locators.home_page_title:
        sleep(0.25)
        assert driver.find_element(By.XPATH,'//span[contains(text(),"dvantage")]').is_displayed()
        print('Main logo is displayed')


def check_socialmedia_link():
    driver.find_element(By.XPATH, '//span[contains(text(),"dvantage")]').click()
    #driver.get(locators.home_page_url)
    if driver.title == locators.home_page_title:
        sleep(0.5)
        driver.find_element(By.NAME,'follow_facebook').click()
        sleep(0.5)
        driver.switch_to.window(driver.window_handles[1])
        # print(f'{driver.current_url}')
        if driver.current_url == locators.fb_page_url:
            sleep(0.5)
            print("Facebook links on Homepage is clickable")
            sleep(0.5)
            driver.close()
    driver.switch_to.window(driver.window_handles[0])
    if driver.title == locators.home_page_title:
        sleep(0.5)
        driver.find_element(By.NAME,'follow_twitter').click()
        sleep(0.5)
        driver.switch_to.window(driver.window_handles[1])
        # print(f'{driver.current_url}')
        if driver.current_url == locators.tw_page_url:
            sleep(0.5)
            print("Twitter links on Homepage is clickable")
            sleep(0.5)
            driver.close()
    driver.switch_to.window(driver.window_handles[0])
    if driver.title == locators.home_page_title:
        sleep(0.5)
        driver.find_element(By.NAME,'follow_linkedin').click()
        sleep(0.5)
        driver.switch_to.window(driver.window_handles[1])
        # print(f'{driver.current_url}')
        #if driver.current_url == locators.in_page_url:
        sleep(0.5)
        print("LinkedIn links on Homepage is clickable")
        sleep(0.5)
        driver.close()
        sleep(0.5)
    driver.switch_to.window(driver.window_handles[0])


def contact_us():
    sleep(0.25)
    Select(driver.find_element(By.NAME,'categoryListboxContactUs')).select_by_visible_text('Headphones')
    sleep(0.25)
    Select(driver.find_element(By.NAME,'productListboxContactUs')).select_by_visible_text('HP H2310 In-ear Headset')
    sleep(0.25)
    driver.find_element(By.NAME,'emailContactUs').send_keys(locators.new_email)
    sleep(0.25)
    driver.find_element(By.NAME,'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(0.25)
    driver.find_element(By.ID,'send_btnundefined').click()
    assert driver.find_element(By.XPATH,'//p[contains(text(),"Thank you for contacting Advantage support.")]')
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT,'CONTINUE SHOPPING').click()
    if driver.current_url == locators.home_page_url:
        print('CONTACT US form is working properly')


def check_homepage():
    #setUp()
    check_homepage_text()
    sleep(0.25)
    check_shopnow_button()
    sleep(0.25)
    check_main_menu()
    sleep(0.25)
    check_mainlogo()
    sleep(0.25)
    check_socialmedia_link()
    sleep(0.25)
    contact_us()
    sleep(0.5)

def delete_account():
    driver.find_element(By.XPATH, '//span[contains(text(),"dvantage")]').click()
    if driver.current_url==locators.home_page_url:
        #login()
        #validate_new_account()
        driver.find_element(By.LINK_TEXT, locators.new_user_name).click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH,"//label[contains(text(),'- No orders -')]").is_displayed()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, locators.new_user_name).click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My account")]').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH,'//h3[contains(.,"MY ACCOUNT")]')
        # assert driver.find_element(By.XPATH,f'//label[contains(.,"{locators.account_first_name}")]').is_displayed()
        # sleep(0.25)
        # assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.account_last_name}")]').is_displayed()
        sleep(0.3)
        driver.find_element(By.XPATH,'//div[contains(text(),"Delete Account")]').click()
        sleep(0.5)
        driver.find_element(By.XPATH,'//div[contains(text(),"yes")]').click()
        sleep(0.5)
        #login()
        #assert driver.find_element(By.XPATH,'//label[contains(.,"Incorrect user name or password.")]').is_displayed()
        sleep(0.25)
        print(f'{locators.new_user_name} account is deleted')
        logger('deleted')


def add_shopping_cart():
    if driver.title == locators.home_page_title:
        #add shopping cart method 1
        driver.find_element(By.ID,'tabletsTxt').click()
        sleep(0.25)
        driver.find_element(By.XPATH,f'//a[contains(text(),"{locators.item1_name}")]').click()
        sleep(0.25)
        #driver.find_element(By.XPATH,'//span[contains(.,"BLACK")]').click()
        sleep(0.25)
        driver.find_element(By.CLASS_NAME,'plus').click()
        sleep(0.25)
        driver.find_element(By.NAME,'save_to_cart').click()
        sleep(0.25)
        print(f'{locators.item1_name} is added to shopping cart')
        #add shopping cart method 2
        driver.find_element(By.XPATH,'//a[contains(text(),"HOME")]').click()
        sleep(0.25)
        if driver.title == locators.home_page_title:
            driver.find_element(By.ID,'details_16').click()
            sleep(0.25)
            driver.find_element(By.NAME, 'save_to_cart').click()
            sleep(0.25)
            print(f'{locators.item2_name} is added to shopping cart')


def checkout_cart():
    driver.find_element(By.ID,'menuCart').click()
    sleep(0.25)
    #assert driver.find_element(By.XPATH,'//label[contains(.,"Your_shopping_cart_is_empty")]').is_displayed()
    # empt = driver.find_element(By.LINK_TEXT,'CONTINUE SHOPPING')
    # if empt.is_displayed():
    #      sleep(0.25)
    #      print('Shopping Cart is empty')
    #      sleep(0.25)
    #      driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
    # else:
        #driver.switch_to.window(driver.window_handles[0])
        #driver.find_element(By.XPATH,'//a[contains(.,"SHOPPING CART")]').click()
    driver.find_element(By.XPATH,'//button[@id="checkOutButton"]').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.account_first_name}")]').is_displayed()
    sleep(0.25)
    assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.account_last_name}")]').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID,'next_btn').click()
    sleep(0.25)
    driver.find_element(By.NAME,'safepay_username').send_keys(locators.sp_username)
    sleep(0.25)
    driver.find_element(By.NAME,'safepay_password').send_keys(locators.sp_password)
    sleep(0.25)
    driver.find_element(By.XPATH,'//button[@id="pay_now_btn_SAFEPAY"]').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH,'//span[contains(.,"Thank you")]').is_displayed()
    sleep(0.5)
    tracking_number = driver.find_element(By.ID,'trackingNumberLabel').text
    order_number = driver.find_element(By.ID,'orderNumberLabel').text
    print(f'Order is found,tracking number is {tracking_number}, order number is {order_number}')
    sleep(0.5)
    name=driver.find_element(By.XPATH,'//body/div[3]/section[1]/article[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]').text
    #assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.account_first_name}")]').is_displayed()
    sleep(0.5)
    if (locators.account_first_name.capitalize() in name) and (locators.account_last_name.capitalize() in name):
    #assert driver.find_element(By.XPATH, f'//label[contains(.,"{locators.account_last_name}")]').is_displayed()
    #print(f'{name}')
    # print(f'{order_lastname}')
        sleep(0.25)
    # assert driver.find_element(By.XPATH,f'//label[contains(.,"{locators.phone}")]').is_displayed()
        print('Order name is confirmed')


def view_cart():
    driver.find_element(By.XPATH,'//span[contains(text(),"dvantage")]').click()
    if driver.title==locators.home_page_title:
        driver.find_element(By.LINK_TEXT, locators.new_user_name).click()
        sleep(0.25)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH,'//h3[contains(text(),"MY ORDERS")]').is_displayed()
        sleep(0.25)
        order=driver.find_element(By.XPATH,"//tbody/tr[2]/td[1]/label[1]").text
        print (f'Order {order} is found')


def cancel_order():
    driver.find_element(By.XPATH,'//a[contains(text(),"REMOVE")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH,'//label[contains(text(),"CANCEL")]').click()
    sleep(0.25)
    print('Order is canceled. The account can be deleted.')


def checkout():
    if driver.title == locators.home_page_title:
        add_shopping_cart()
        sleep(0.25)
        checkout_cart()
        sleep(0.25)



#setUp()
# #check_shopnow_button()
# #check_main_menu()
# #contact_us()
# #check_homepage_text()
# #tearDown()
# # # Create New Account
# create_new_account()
# validate_new_account()
# logger('created')
# add_shopping_cart()
#checkout()
# view_cart()
#logout()
# #delete_account()
# # # Validate New Account is created
# #validate_new_account()
# # print(f'------New account is created, Username is {locators.new_user_name}')
# #logout
# #logout()
# #sleep(0.5)
# # # Login
#login()
# # # Validate New User can login (see if you can reuse New Account Validation)
# #validate_new_account()
# #delete_account()
#
# # print(f'------New user {locators.new_user_name} can log in!')
# # logger('created')
# # # Logout
# #logout()
# # print(f'------New user {locators.new_user_name} can log out successfully!')
# # sleep(0.25)
#tearDown()
