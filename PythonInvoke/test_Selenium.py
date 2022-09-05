def sel():
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    s = Service('C:/Users/ADMIN/PycharmProjects/SeleniumTest/Driver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    time.sleep(5)
