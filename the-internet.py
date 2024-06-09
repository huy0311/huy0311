from seleniumbase import BaseCase
import time
BaseCase.main(__name__, __file__)
import os

class TestSimpleLogin(BaseCase):
    def test_simple_login(self):
#         self.open("https://the-internet.herokuapp.com/add_remove_elements/")
#         self.click(".example > button:nth-child(1)")
#         self.open("https://play1.automationcamp.ir/expected_conditions.html")
#         self.wait_for_and_switch_to_alert()
#         self.open("https://the-internet.herokuapp.com/")
#         self.click("#content > ul:nth-child(4) > li:nth-child(3) > a:nth-child(1)")
#         self.open("https://the-internet.herokuapp.com/javascript_alerts")
#         self.find_element("/html/body/div[2]/div/div/ul/li[1]/button").click()
#         time.sleep(10)        
#         os.popen("taskkill /f /im chrome.exe")

#         self.open("https://the-internet.herokuapp.com/disappearing_elements")
#         self.highlight(".example > ul:nth-child(4) > li:nth-child(2) > a:nth-child(1)")
#         self.click(".example > ul:nth-child(4) > li:nth-child(2) > a:nth-child(1)")

#         self.open("https://the-internet.herokuapp.com/drag_and_drop")
#         self.highlight("#column-a")
#         self.drag_and_drop("#column-a","#column-b")
#         
#         self.highlight("#column-a")


#         self.open("https://the-internet.herokuapp.com/dropdown")
#         self.select_option_by_text("#dropdown","Option 1")

#         self.open("https://the-internet.herokuapp.com/dynamic_content")
#         if self.get_image_url('div.row:nth-child(4) > div:nth-child(1) > img:nth-child(1)') == "/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg":
#             self.highlight('div.row:nth-child(4) > div:nth-child(1) > img:nth-child(1)')
#         else:
#             print("not found")
#             brake
#         self.open("https://the-internet.herokuapp.com/add_remove_elements/")
#         self.check_window(name="The Internet", baseline=True)
#         self.click('/html/body/div[2]/div/div/button')
#         #self.highlight('/html/body/div[2]/div/div/div/button')
#         #self.click('/html/body/div[2]/div/div/div/button')
#         self.check_window(name="The Internet", level = 3)
#         time.sleep(10)        
#         os.popen("taskkill /f /im chrome.exe")
        
#         self.open("https://the-internet.herokuapp.com/dynamic_controls")
#         self.check_window(name="The Internet", baseline=True)
#         #self.highlight("/html/body/div[2]/div/div[1]/form[1]/div/input")
#         self.click('/html/body/div[2]/div/div[1]/form[1]/div/input')
#         #self.highlight('/html/body/div[2]/div/div[1]/form[1]/button')
#         self.click('/html/body/div[2]/div/div[1]/form[1]/button')
#         #self.highlight('#message')
#         self.click('#checkbox-example > button:nth-child(1)')
#         self.find_text("It's back!")        
#         self.check_window(name="The Internet", level = 3)

#         self.open("https://the-internet.herokuapp.com/dynamic_loading/2")
#         self.click('//*[@id="start"]/button')
#         if self.assert_text("Hello World!",'//*[@id="finish"]/h4', timeout=10) == True:
#             print("Found")

#         self.open("https://the-internet.herokuapp.com/entry_ad")
#         self.click('//*[@id="modal"]/div[2]/div[3]/p')
#         self.click('#restart-ad')
#         self.highlight('//*[@id="modal"]/div[2]/div[3]/p')
#         self.open("https://the-internet.herokuapp.com/floating_menu#contact")
#         self.scroll_to_bottom()
#         self.highlight('//*[@id="menu"]/ul/li[1]/a')

#         self.open("https://the-internet.herokuapp.com/nested_frames")
#         self.highlight("/html/frameset")
#         self.highlight('html > frameset:nth-child(2)')
#         print(self.get_text('html > frameset:nth-child(2)'))

# 
#         self.open("https://the-internet.herokuapp.com/iframe")
#         self.highlight("//button[@title='Align left']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']//*[name()='path' and contains(@d,'M5 5h14c.6')]")
#         time.sleep(10)

#         self.open("https://the-internet.herokuapp.com/horizontal_slider")
#         self.set_value('input[value="0"]', "3")
#         self.highlight('input[value="0"]')
#
#         self.open("https://the-internet.herokuapp.com/hovers")
#         self.highlight("//div[@class='row']//div[2]//img[1]")
#         self.hover("//div[@class='row']//div[2]//img[1]")


#         self.open("https://the-internet.herokuapp.com/inputs")
#         self.set_value("//input[@type='number']","40")
#         self.highlight("//input[@type='number']")

         self.open("https://the-internet.herokuapp.com/jqueryui/menu#")
         self.highlight("//a[normalize-space()='Enabled']")
         self.click("//a[normalize-space()='Enabled']")
         self.click("//a[normalize-space()='Downloads']")
         self.highlight("//a[normalize-space()='PDF']")
         time.sleep(3)


        os.popen("taskkill /f /im chrome.exe")
