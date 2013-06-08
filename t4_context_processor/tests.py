from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert '42cc' in browser.title  # 42cc will pass in template base.html title by const from settings.py
browser.quit()
