from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from config import base_url


def test_login_admin():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "89.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://84.252.132.251:4444/wd/hub",
        desired_capabilities=capabilities)


    #chrome_options = Options()
    #chrome_options.add_argument("--headless")

    #driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'

    driver.get(URL)
    search_input = driver.find_element_by_id('search_form_input_homepage')
    
    search_input.send_keys(PHRASE + Keys.RETURN)
    # Убедитесь, что результаты появились на странице результатов
    link_divs = driver.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0
    # Убедитесь, что как минимум один результат поиска содержит поисковый запрос
    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    phrase_results = driver.find_elements_by_xpath(xpath)
    assert len(phrase_results) > 0
    # Убедитесь, что поисковый запрос сохранился
    search_input = driver.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == PHRASE

    
