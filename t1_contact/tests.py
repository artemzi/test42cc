from selenium import webdriver
from pyvirtualdisplay import Display

display = Display()
display.start()

browser = webdriver.Firefox()

try:
    browser.get('http://localhost:8000')
    assert 'Index' in browser.title

finally:
    browser.quit()
    display.stop()