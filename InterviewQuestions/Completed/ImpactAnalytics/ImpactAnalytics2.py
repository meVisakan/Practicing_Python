#
# Title - Home Page - Kayak,"//span[text()='Compare flight deals from 100s of sites']"
# Text - Populated - From - Search Box - Kayak,"//div[@class='c_neb-item-value']"
# Close - Populated - From - Search Box - Kayak,"//div[@class='c_neb-item-close']"
# Input - From - Search Box - Kayak,"//input[@aria-label='Flight origin input']"
# Input - To - Search Box - Kayak,"//input[@aria-label='Flight destination input']"
# Button - Search - Search box - Kayak,"//button[@aria-label='Search']"


# # driver.navigate.to("kayak.com)
# try:
# # driver.navigate.to("kayak.com)
# driver.wait_until_element_is_visible(Title - Home Page - Kayak, 30, "Home Page not loaded")
# driver.take_and_upload_screenshot("Hone page loaded")
# except:
# driver.get(url)
# driver.wait_until_element_is_visible(Title - Home Page - Kayak, 30, "Home Page not loaded again")
# driver.take_and_upload_screenshot("Hone page loaded")
#
# from_populated = driver.get_text(Text - Populated - From - Search Box - Kayak)
# Assertions asset.assertEquals(from, "Bengaluru (BLR)")
#
# driver.click_element(Close - Populated - From - Search Box - Kayak)
# if driver.element_enabled(Text - Populated - From - Search Box - Kayak):
#     raise AssertionError
# driver.click_element(Input - From - Search Box - Kayak)
# driver.input_text(Input - From - Search Box - Kayak, from_city)
# driver.press_keys(NONE, "ENTER")
# # driver.click_element(Input - To - Search Box - Kayak)
# driver.input_text(Input - To - Search Box - Kayak, to_city)
# driver.press_keys(NONE, "ENTER")
#
#
# driver.take_and_upload_screenshot("Flights are shown loaded")
#
# driver.click_element(Button - Search - Search box - Kayak)
# driver.wait_until_element_is_visible("Flights page", 30, "No flights found")
# driver.take_and_upload_screenshot("Flights are shown loaded")
#


