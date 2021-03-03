from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
import time

driver: WebDriver = webdriver.Firefox()

driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("facebook")
driver.find_element_by_css_selector(".FPdoLc > center:nth-child(1) > input:nth-child(1)").click()
time.sleep(2)
driver.quit()

-------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
import time

driver: WebDriver = webdriver.Firefox()

driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("facebook")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
time.sleep(2)
driver.quit()

----------------------------------------------
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com/")
        print("The title is " + self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.bing.com/?FORM=Z9FD1")
        print("The title is " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()



---------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10) # waits untill time is reached or element executed
driver.get("http://www.newtours.demoaut.com/")
usr_ele = driver.find_element_by_name("userName")
print("username desplayed is" , usr_ele.is_displayed())
print("username enabled is" , usr_ele.is_enabled())
psd_ele = driver.find_element_by_name("password")
print("password enabled is", psd_ele.is_enabled())
usr_ele.send_keys("yadu")
psd_ele.send_keys("yadu")
psd_ele.send_keys(Keys.RETURN)
round_trip = driver.find_element_by_css_selector("body > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > b:nth-child(1) > font:nth-child(1) > input:nth-child(1)")
print("round trip selected is" ,round_trip.is_selected())
driver.close()

-----------------------------------------------
#select option in a drop down menu. using select

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://demo.automationtesting.in/Register.html")
ele = driver.find_element_by_id("Skills")
drop = Select(ele)
drop.select_by_visible_text("Python")
Select(driver.find_element_by_id("countries")).select_by_visible_text("india")

time.sleep(3)
driver.close()

-------------------------------------------------
#switching/operating between tabs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800,600)
driver.get("https://learn.letskodeit.com/p/practice")
driver.find_element_by_id("openwindow").click()
handle = driver.current_window_handle
handles = driver.window_handles
print("parent is ",handle)
print("all are ", handles)
for han in handles:
    if han not in handle:
        driver.switch_to.window(han)
time.sleep(2)
driver.set_window_size(800,600)
ele = driver.find_element_by_id("search-courses")
ele.send_keys("python",Keys.ENTER)
#or
#ele.send_keys(Keys.ENTER)

driver.quit()
-----------------------------
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.set_window_size(800,600)

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()
#below finds number of links on page
links = driver.find_elements_by_tag_name("a")
print(len(links))
parent = driver.current_window_handle
handles = driver.window_handles
size = len(handles)
print(size)
for x in range(size):
    if x != parent :
        driver.switch_to.window(handles[x])
        print(driver.title)



------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800,600)
driver.get("http://demo.automationtesting.in/Register.html")
driver.find_element_by_xpath("/html/body/footer/div/div/div[2]/a[1]").click()
handles = driver.window_handles
for handle in handles:
    if driver.title == "Register":
        driver.close()
time.sleep(3)

driver.quit()

----------------------------------------------
scrolling webpage


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800,600)
driver.get("https://www.w3schools.com/python/python_for_loops.asp")
#ele = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/h2[8]")
#driver.execute_script("arguments[0].scrollIntoView();",ele)
page = driver.find_element_by_tag_name("html")
page.send_keys(Keys.END)
driver

-------------------------------------------------------
#select checkboxes

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800,600)
driver.get("https://learn.letskodeit.com/p/practice")
ele = driver.find_elements_by_xpath("//input[@type='checkbox']")
size = len(ele)
print(size)
for x in ele:
    isselcted = x.is_selected()
    #x.is_selected() == False
    if not isselcted:
        x.click()

-------------------------------------------------------------
#mouse hover

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.set_window_size(800,600)
driver.get("https://learn.letskodeit.com/p/practice")
ele = driver.find_element_by_id("mousehover")
top = driver.find_element_by_xpath("//div[@class='mouse-hover-content'] //a[text()='Top']")

driver.execute_script("window.scrollBy(0 ,930);")
time.sleep(2)
actions = ActionChains(driver)

actions.move_to_element(ele).perform()
time.sleep(3)
actions.move_to_element(top).click().perform()

driver.close()
------------------------------------------------------------
# wait untill clickable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800,600)
driver.get("https://learn.letskodeit.com/p/practice")
ele = driver.find_elements_by_id("openwindow")
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.ID,'openwindow'))).click()
driver.quit()
------------------------------------------------------
#total no of rows

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800, 600)
driver.get("https://learn.letskodeit.com/p/practice")
row = driver.find_element_by_xpath("//table[@id='product']/tbody")
total_row = row.find_elements_by_tag_name("tr")
print(len(total_row))
-----------------------------------
# total no of columns

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800, 600)
driver.get("https://learn.letskodeit.com/p/practice")
row = driver.find_element_by_xpath("//table[@id='product']/tbody/tr")
total_row = row.find_elements_by_tag_name("th")
print(len(total_row))
-------------------------------------------------------
#data driven testing of login
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.set_window_size(800, 600)
driver.get('http://newtours.demoaut.com/mercurywelcome.php')

df = pd.read_excel('usrdetails.xls')
#print(df)
for ind in df.index:

    usr = driver.find_element_by_xpath("//input[@name='userName']")
    pwd = driver.find_element_by_xpath("//input[@name='password']")
    hom = driver.find_element_by_css_selector(
        "tr.mouseOut:nth-child(1) > td:nth-child(2) > font:nth-child(1) > a:nth-child(1)")

    print("username is:" + df['USERNAME'][ind],"      " "password is:", df['PASSWORD'][ind])
    usr.send_keys(df['USERNAME'][ind])
    pwd.send_keys(df['PASSWORD'][ind],Keys.RETURN)
    time.sleep(2)
    if driver.find_element_by_xpath(
        "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p/font/a").is_displayed():
        print('test failed')
    elif driver.find_element_by_xpath("//*[contains(text(),'Find a Flight: Mercury Tours:')]").is_displayed():
        print('passed')
    driver.find_element_by_link_text("Home").click()
    time.sleep(2)

driver.quit()
---------------------------------------------

#switching tabs and wating
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

driver = webdriver.Firefox()
driver.implicitly_wait(10)
# driver.set_window_size(800, 600)
driver.get('https://learn.letskodeit.com/p/practice')
wait = WebDriverWait(driver,10)
Op = driver.find_element_by_id("opentab")
Op.click()
# time.sleep(5)
handle = driver.current_window_handle
handles = driver.window_handles
print(len(handles))
print(driver.title)
for x in handles:
    driver.switch_to.window(x)
    if driver.title == "Let's Kode It":
        pass
print(driver.title)
sellik = driver.find_element_by_xpath("//div[@title='Selenium WebDriver With Java']")
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Selenium WebDriver With Java']")))
driver.find_element_by_xpath("//div[@title='Selenium WebDriver With Java']").click()
practice = "//a[contains(text(),'Practice')]"

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Practice')]")))
driver.find_element_by_xpath("//a[contains(text(),'Practice')]").click()
time.sleep(5)
driver.quit()
-------------------------------------------------------------------
#take screenshot
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd


class Screenshots():

    def test(self):

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.set_window_size(800, 600)
        driver.get('https://learn.letskodeit.com/p/practice')
        Op = driver.find_element_by_id("opentab")
        Op.click()
        self.takescreenshot(driver)

    def takescreenshot(self, driver):
        filename = str(round(time.time() * 1000)) + ".png"
        destination = "/home/yadu/PycharmProjects/DDT/venv"
        finaldestination = destination + filename

        try:
            driver.save_screenshot(finaldestination)
            print("screenshot taken")
        except NotADirectoryError:
            print("there was an error")


ff = Screenshots()
ff.test()
---------------------------------------------------------
#scrolling into webpage using javascript

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd


class Screenshots():

    def test(self):

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.set_window_size(800, 600)
        driver.get('https://learn.letskodeit.com/p/practice')
        #scrolling to bottom using javascript
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        # scrolling to top using javascript
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)
        element = driver.find_element_by_id("mousehover")
        # scrolling into view
        element.location_once_scrolled_into_view
        #scrolling to avoid header into view using javascript
        driver.execute_script("window.scrollBy(0,-40);")
        element.click()

ff = Screenshots()
ff.test()
--------------------------------------------------------------------
#switching between frames

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd


class Screenshots():

    def test(self):

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.set_window_size(800, 600)
        driver.get('https://learn.letskodeit.com/p/practice')
        driver.execute_script("window.scrollBy(0,1000);")
        driver.switch_to.frame("courses-iframe")
        driver.find_element_by_id("search-courses").send_keys("python")
        time.sleep(2)
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        driver.find_element_by_id("name").send_keys("test completed")

ff = Screenshots()
ff.test()

------------------------------------------------------------------------
#handling alerts


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd


class Screenshots():

    def test(self):

        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.set_window_size(800, 600)
        driver.get('https://learn.letskodeit.com/p/practice')
        driver.find_element_by_id("name").send_keys("test completed")
        time.sleep(1)
        driver.find_element_by_id("alertbtn").click()
        time.sleep(3)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("test completed")
        time.sleep(1)
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        alert2.dismiss()


ff = Screenshots()
ff.test()
--------------------------------------------------------------
#