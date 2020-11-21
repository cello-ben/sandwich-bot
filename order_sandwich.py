import time
import sys
from selenium import webdriver

chromedriver_location = '/your/chromedriver/location'

pick_store = '//*[@id="product-details"]/div/div[2]/div/div[3]/button'
zip_input = '//*[@id="input_ZIPorCity,Stateorstorenumber42"]'
search_button = '//*[@id="body-wrapper"]/div[2]/div/div/div[2]/div[1]/form/div[1]/button'
my_publix_button = '//*[@id="body-wrapper"]/div[2]/div/div/div[2]/div[2]/div/ul/li[3]/div/button'
build_now = '//*[@id="product-details"]/div/div[2]/div/a'
whole_sandwich = '//*[@id="content_14"]/form/div[2]/div[1]/div[2]/label/div/div/div[1]'
wheat_bread = '//*[@id="input_Bread30_2"]'
no_extras_next = '//*[@id="content_32"]/form/button'
mayonnaise = '//*[@id="186-4"]/div[1]/div/label/div/div'
mayonnaise_next = '//*[@id="content_40"]/form/button'
toasted = '//*[@id="content_51"]/form/div[2]/div[1]/div[2]/label/div/div/span'
no_combo = '//*[@id="content_55"]/form/div[3]/div[1]/div[2]/label/div/div/span'
instructions = '//*[@id="label_23"]'
no_pickles_yes_spinach = '//*[@id="input_specialInstructions24"]'
add_item = '//*[@id="content_19"]/form/div[5]/div/button'
review_checkout = '//*[@id="main"]/div/div[2]/div/div[3]/div/a'
confirm_store = '//*[@id="body-wrapper"]/div[2]/div/div[2]/button[1]'
checkout = '//*[@id="main"]/section/div/div[2]/div/div[1]/div[2]/form/button'
pickup_first = '//*[@id="input_FirstName20"]'

driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.publix.com/shop-online/in-store-pickup/builder?baseProductID=BMO-DSB-538557')
time.sleep(3)

#Choose Publix location by Zip code.
driver.find_element_by_xpath(pick_store).click()
time.sleep(3)
driver.find_element_by_xpath(zip_input).send_keys('33139')
time.sleep(1)
driver.find_element_by_xpath(search_button).click()
time.sleep(3)
driver.find_element_by_xpath(my_publix_button).click()
time.sleep(5)

#Build sandwich
driver.find_element_by_xpath(build_now).click()
time.sleep(5)
driver.find_element_by_xpath(whole_sandwich).click()
time.sleep(1)
driver.find_element_by_xpath(wheat_bread).click()
time.sleep(1)
driver.find_element_by_xpath(no_extras_next).click()
time.sleep(1)
driver.find_element_by_xpath(mayonnaise).click()
time.sleep(1)
driver.find_element_by_xpath(mayonnaise_next).click()
time.sleep(1)
driver.find_element_by_xpath(toasted).click()
time.sleep(1)
driver.find_element_by_xpath(no_combo).click()
time.sleep(1)
driver.find_element_by_xpath(instructions).click()
time.sleep(1)
driver.find_element_by_xpath(no_pickles_yes_spinach).send_keys('No pickles, please. Please add spinach.')
time.sleep(1)

#Add to cart and check out.
driver.find_element_by_xpath(add_item).click()
time.sleep(5)
driver.find_element_by_xpath(review_checkout).click()
time.sleep(5)
driver.find_element_by_xpath(confirm_store).click()
time.sleep(3)
driver.find_element_by_xpath(checkout).click()
time.sleep(3)

#Get rid of the modal window asking to take a survey in case it pops up.
try:
    driver.find_element_by_xpath('//*[@id="fsrFocusFirst"]').click()
    time.sleep(3)
except:
    pass

#Enter info for person picking sandwich up.
driver.find_element_by_xpath(pickup_first).send_keys('Benjamin')

#This sleeps the program and wraps it up nicely in the event that the checkout is actually done.
time.sleep(5)
print('Sandwich ordered, payment processed...go pick it up in about 1/2 hour.')
driver.quit()
sys.exit(0)
