from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    # form fields
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    # created from
    CREATED_FULL_NAME = (By.XPATH, '//p[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')



class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, '#tree-node > div > button.rct-option.rct-option-expand-all')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = (By.XPATH, './/ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR,'span[class="text-success"]')


class RadioButtonLocators:
      YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
      IMPRESIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
      NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[for="noRadio"]')
      OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')