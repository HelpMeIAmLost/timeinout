import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

class TimeInOut(object):
    def __init__(self):
        self.login_page = "https://www.ewk.tasty-web.com/e-payStamp/A0101Action.do?gengo=J"
        self.timeinout_page = "https://www.ewk.tasty-web.com/e-payStamp/A0101Action.do"
        self.chromedriver = "2.42\\chromedriver.exe"
        self.capabilities = { "chromeOptions":  { "useAutomationExtension": False,
                                                  "args"                  : ["--disable-extensions"] }
                            }
        self.browser = webdriver.Chrome(executable_path=self.chromedriver, desired_capabilities=self.capabilities)

    def LogIn(self):
        self.browser.get(self.login_page)
        
        loginKigyoCode = self.browser.find_element_by_id("loginKigyoCode")
        shainBangoDisp = self.browser.find_element_by_id("shainBangoDisp")
        password = self.browser.find_element_by_id("password")
        
        file = open("info.txt", "r") 
        text = file.readline()
        loginKigyoCode.send_keys(text)
        text = file.readline()
        shainBangoDisp.send_keys(text)
        text = file.readline()
        password.send_keys(text)
        file.close()
        
        self.browser.find_element_by_id("btnLogin").click()

        print("\nLogging in..\n")
        
        wait = WebDriverWait(self.browser, 5)
        try:
            page_loaded = wait.until_not(
                            lambda browser: self.browser.current_url == self.login_page
                          )

            instatus = self.browser.find_element_by_id("jikoku1_1").text
            
            print("Successful login!\n")

        except NoSuchElementException:
            print("Failed logging in! Please update your info.txt file.")
            #print("\n")
            return 1

        except TimeoutException:
            print("Loading timeout expired! Please try again later.")
            #print("\n")
            return 2

        return 0

    def TimeIn(self):
        instatus = self.browser.find_element_by_id("jikoku1_1").text

        if instatus == "":
            # For time in
            self.browser.find_element_by_id("btnDakoku1").click()
            #print("Click in!")
        else:
            print("Time in already registered.")

        print("Timed in at: ", self.browser.find_element_by_id("jikoku1_1").text, "\n")

    def TimeOut(self):
        instatus = self.browser.find_element_by_id("jikoku1_1").text

        if instatus == "":
            # No time in
            print("Time in is not yet registered!\nPlease run 'timeinout in' first.\n")
            return

        print("Timed in at: ", self.browser.find_element_by_id("jikoku1_1").text)

        outstatus = self.browser.find_element_by_id("jikoku4_1").text

        if outstatus == "":
            # For time out
            browser.find_element_by_id("btnDakoku4").click()
            #print("Click out!")
        else:
            print("Time out already registered.")

        print("Timed out at: ", self.browser.find_element_by_id("jikoku4_1").text, "\n")
            
if __name__ == "__main__":
    print("TimeInOut v1.0\nby Rowen Chumacera\n")
    
    if len(sys.argv) == 2:
        page = TimeInOut()

        status = page.LogIn()

        if status == 0:
            if sys.argv[1].lower() == "in":
                page.TimeIn()
            else:
                if sys.argv[1].lower() == "out":
                    page.TimeOut()
                else:
                    print("Usage:\n   timeinout [in|out]\n")
        else:
            # Some error-handling here
            print("\n")
    else:
        print("Usage:\n   timeinout [in|out]\n")
