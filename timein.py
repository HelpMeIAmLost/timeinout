from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import 

class TimeIn(object):
    def __init__(self):
        self.login_page = "https://www.ewk.tasty-web.com/e-payStamp/A0101Action.do?gengo=J"
        self.timeinout_page = "https://www.ewk.tasty-web.com/e-payStamp/A0101Action.do"
        self.chromedriver = "2.42\\chromedriver.exe"
        self.capabilities = { "chromeOptions":  { "useAutomationExtension": False,
                                                  "args"                  : ["--disable-extensions"] }
                            }

    def LogIn(self):
        browser = webdriver.Chrome(executable_path=self.chromedriver, desired_capabilities=self.capabilities)
        browser.get(self.login_page)
        
        loginKigyoCode = browser.find_element_by_id("loginKigyoCode")
        shainBangoDisp = browser.find_element_by_id("shainBangoDisp")
        password = browser.find_element_by_id("password")
        
        file = open("info.txt", "r") 
        text = file.readline()
        loginKigyoCode.send_keys(text)
        text = file.readline()
        shainBangoDisp.send_keys(text)
        text = file.readline()
        password.send_keys(text)
        file.close()
        
        browser.find_element_by_id("btnLogin").click()

        print("Logging in..")
        print("\n")
        
        wait = WebDriverWait(browser, 5)
        try:
            page_loaded = wait.until_not(
                            lambda browser: browser.current_url == self.login_page
                          )

            instatus = browser.find_element_by_id("jikoku1_1").text

            print("Successful login!")
            print("\n")

#            if(browser.current_url == self.timeinout_page):
#                print("Successful login!")
#               print("\n")

            if(instatus == ""):
               # For time in
               browser.find_element_by_id("btnDakoku1").click()
#                print("Click in!")

            print("Time in at: ", browser.find_element_by_id("jikoku1_1").text)
            print("\n")

        except TimeoutException:
            #self.fail("Loading timeout expired!")
            print("Loading timeout expired!")
            print("\n")
            return

        except NoSuchElementException:
            #self.fail("Failed logging in!")
            print("Failed logging in! Please update your info.txt file.")
            print("\n")
            return

#        browser.quit()
            
if __name__ == "__main__":
    page = TimeIn()
    page.LogIn()
