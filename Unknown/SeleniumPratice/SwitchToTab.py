from selenium import webdriver
import time

# Open chrome browswer
d = webdriver.Chrome()
d.maximize_window()
d.get("https://www.python.org/")
time.sleep(5)

d.execute_script('window.open("http://robotframework.org/")')
time.sleep(2)
d.execute_script("window.open('https://mail.google.com')")
time.sleep(2)
d.execute_script("window.open('https://www.amazon.in/')")
time.sleep(2)
windows = d.window_handles
print("Title is : ",windows)

print("Default Title is : ",d.title)

d.switch_to.window(windows[1])
print('\n windows[1] title is ', d.title)
time.sleep(2)
d.switch_to.window(windows[2])
print('\n windows[2] title is ', d.title)
time.sleep(2)
d.switch_to.window(windows[3])
print('\n windows[3] title is ', d.title)
time.sleep(2)
d.switch_to.window(windows[1])
print('\n windows[1] title is ', d.title)
time.sleep(2)
d.switch_to.window(windows[2])
print('\n windows[2] title is ', d.title)
d.quit()
