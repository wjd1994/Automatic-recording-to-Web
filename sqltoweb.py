from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sqlite3
import time
driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(30) 
driver.get("http://passport.5any.com/Passport/WebUI/Account/Login?ReturnUrl=%2fpassport%2fWebUI%2faccount%2fCheckWebApplication%3fWebApplicationId%3dUniversityV3_Web%26AppReturnUrl%3d%252feStudy%252fPersonalCenter%252fUcMyCreate&WebApplicationId=UniversityV3_Web&AppReturnUrl=%2feStudy%2fPersonalCenter%2fUcMyCreate")
#a1 = input("please input any key")
elem = driver.find_element_by_xpath("//*[@id='Login']/div[2]/div[3]/div[5]/div")
elem.click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])#切换为最新打开的窗口
elem0 = driver.find_element_by_id("username")
elem0.send_keys("cdwy_teacher")
elem = driver.find_element_by_id("txtPPWWDD")
elem.clear()
elem.send_keys("cddec*cddec")
elem = driver.find_element_by_id("LbN")
elem.click()
driver.get("http://passport.5any.com/Passport/WebUI/Account/Login?ReturnUrl=%2fpassport%2fWebUI%2faccount%2fCheckWebApplication%3fWebApplicationId%3dUniversityV3_Web%26AppReturnUrl%3d%252feStudy%252fPersonalCenter%252fUcMyCreate&WebApplicationId=UniversityV3_Web&AppReturnUrl=%2feStudy%2fPersonalCenter%2fUcMyCreate")

elem = driver.find_element_by_xpath("//*[@id='Login']/div[2]/div[3]/div[5]/div")
elem.click()
a1 = input("please input any key")
windows = driver.window_handles
driver.switch_to.window(windows[-1])#切换为最新打开的窗口


'''
获取数据库内容
'''
db = sqlite3.connect('test.db')
cur = db.cursor()
cur.execute("select * from text")
l = cur.fetchall()
'''
'''
j = 0
for e in l:
     j += 1
     print(j)
     if('单项选择题' in e[1]):
         '''
         获取题型按键
         '''
         
         elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li")
         ActionChains(driver).move_to_element(elem).perform()#鼠标移动到对应位置
         elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li/ul/li[1]/a")
         elem.click()
         
         '''
         '''
         #time.sleep(1)
         windows = driver.window_handles
         driver.close()
         driver.switch_to.window(windows[-1])#切换为最新打开的窗口
         
         '''
         题目录入
         '''
         
         WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,'ewebeditor_auto_iframe_1')))#显式等待，直到发现iframe
         WebDriverWait(driver, 20,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'ewebeditor_auto_iframe_1')))#显式等待，直到切入iframe
         #driver.switch_to.frame("ewebeditor_auto_iframe_1")
         time.sleep(0.1)
         WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,"eWebEditor")))
         iframe = driver.find_element_by_xpath("//*[@id='eWebEditor']")
         driver.switch_to.frame(iframe)#切入第二层iframe
         elem = driver.find_element_by_xpath("/html/body")
         elem.send_keys(e[2])
         driver.switch_to.parent_frame()#返回父iframe
         driver.switch_to.default_content()#返回主页面

         '''
         '''
         
         elem0 = driver.find_element_by_xpath("//*[@id='CreateCourseProblem']/table[1]/tbody/tr[6]/td/div")#获取添加选项
         
         '''
         录入选项
         '''
         for i in range(4):
              elem0.click()#添加选项
              #time.sleep(1)
              s = "ewebeditor_auto_iframe_"+str(i+3)#选项框ifram的id
              #WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,s)))
              WebDriverWait(driver, 20,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,s)))
              #driver.switch_to.frame(s)
              time.sleep(0.1)
              WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,"eWebEditor")))
              #time.sleep(1)
              iframe = driver.find_element_by_xpath("//*[@id='eWebEditor']")
              driver.switch_to.frame(iframe)
              elem = driver.find_element_by_xpath("/html/body")
              elem.send_keys(e[i+3])
              driver.switch_to.parent_frame()
              driver.switch_to.default_content()

         '''
         四个确认录入按键
         '''
         for i in range(4):
             s = "//*[@id='optionBox']/li[{}]/div[3]/div[1]".format(i+1)
             elem = driver.find_element_by_xpath(s)
             elem.click()

         s = "//*[@id='optionBox']/li[{}]/div[1]/input".format(ord(e[9][0])-ord('A')+1)#获取正确答案按键id    
         elem1 = driver.find_element_by_xpath(s)
         elem1.click()
         s1 = Select(driver.find_element_by_id("DifficultDegree"))#难度设置select
         s1.select_by_value(str(e[10]))
         elem = driver.find_element_by_id("btn_submit")
         elem.click()
         WebDriverWait(driver, 20,0.5).until(EC.alert_is_present())#显式等待弹窗出现
         al = driver.switch_to_alert()
         al.accept()#弹窗处理
         #time.sleep(0.5)
         windows = driver.window_handles
         driver.switch_to.window(windows[-1])#切换为最新打开的窗口
     
     
     if('多项选择题' in e[1]):
          elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li")
          ActionChains(driver).move_to_element(elem).perform()
          elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li/ul/li[2]/a")
          elem.click()
          #time.sleep(1)
          windows = driver.window_handles
          driver.close()
          driver.switch_to.window(windows[-1])#切换为最新打开的窗口
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,'ewebeditor_auto_iframe_1')))
          WebDriverWait(driver, 20,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'ewebeditor_auto_iframe_1')))
          #driver.switch_to.frame("ewebeditor_auto_iframe_1")
          time.sleep(0.1)
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,"eWebEditor")))
          iframe = driver.find_element_by_xpath("//*[@id='eWebEditor']")
          driver.switch_to.frame(iframe)
          elem = driver.find_element_by_xpath("/html/body")
          elem.send_keys(e[2])
          driver.switch_to.parent_frame()
          driver.switch_to.default_content()
          elem0 = driver.find_element_by_xpath("//*[@id='CreateCourseProblem']/table[1]/tbody/tr[6]/td/div")
          for i in range(5):
               elem0.click()
               s = "ewebeditor_auto_iframe_"+str(i+3)
               WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,s)))
               WebDriverWait(driver, 20,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,s)))
               time.sleep(0.1)
               WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,"eWebEditor")))
               iframe = driver.find_element_by_xpath("//*[@id='eWebEditor']")
               driver.switch_to.frame(iframe)
               elem = driver.find_element_by_xpath("/html/body")
               elem.send_keys(e[i+3])
               driver.switch_to.parent_frame()
               driver.switch_to.default_content()
               
  
          for i in range(5):
               s = "//*[@id='optionBox']/li[{}]/div[3]/div[1]".format(i+1)
               elem = driver.find_element_by_xpath(s)
               elem.click()
          
          for i in range(len(e[9])-1):
               s = "//*[@id='optionBox']/li[{}]/div[1]/input".format(ord(e[9][i])-ord('A')+1)    
               elem1 = driver.find_element_by_xpath(s)
               elem1.click()
          
          #elem1 = driver.find_element_by_xpath("//*[@id='optionBox']/li[1]/div[1]/input")
          #elem1.click()
          s1 = Select(driver.find_element_by_id("DifficultDegree"))
          s1.select_by_value(str(e[10]))
          elem = driver.find_element_by_id("IncludedAttachment2")
          elem.click()
          elem = driver.find_element_by_id("btn_submit")
          elem.click()
          WebDriverWait(driver, 20,0.5).until(EC.alert_is_present())
          al = driver.switch_to_alert()
          al.accept()
          windows = driver.window_handles
          driver.switch_to.window(windows[-1])#切换为最新打开的窗口
      
     
     if('判断题' in e[1]):
          elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li")
          ActionChains(driver).move_to_element(elem).perform()
          elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li/ul/li[3]/a")
          elem.click()
          #time.sleep(1)
          windows = driver.window_handles
          driver.close()
          driver.switch_to.window(windows[-1])#切换为最新打开的窗口
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,'ewebeditor_auto_iframe_1')))
          WebDriverWait(driver, 20,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'ewebeditor_auto_iframe_1')))
          #driver.switch_to.frame("ewebeditor_auto_iframe_1")
          time.sleep(0.1)
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,"eWebEditor")))
          iframe = driver.find_element_by_xpath("//*[@id='eWebEditor']")
          driver.switch_to.frame(iframe)
          elem = driver.find_element_by_xpath("/html/body")
          elem.send_keys(e[2])
          driver.switch_to.parent_frame()
          driver.switch_to.default_content()
          #elem1 = driver.find_element_by_id("Answer1")
          elem2 = driver.find_element_by_id("Answer2")
          if('×' in e[9]):
               elem2.click()
          s1 = Select(driver.find_element_by_id("DifficultDegree"))
          s1.select_by_value(str(e[10]))
          elem = driver.find_element_by_id("btn_submit")
          elem.click()
          WebDriverWait(driver, 20,0.5).until(EC.alert_is_present())
          al = driver.switch_to_alert()
          al.accept()
          #time.sleep(0.5)
          windows = driver.window_handles
          driver.switch_to.window(windows[-1])#切换为最新打开的窗口

     if('名词解释题' in e[1] or '简答题' in e[1]):
          elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li")
          ActionChains(driver).move_to_element(elem).perform()
          if '名词解释题' in e[1]:
               elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li/ul/li[4]/a")
          elif '简答题' in e[1]:
               elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div/div[2]/ul/li/ul/li[5]/a")
          elem.click()
          windows = driver.window_handles
          driver.close()
          driver.switch_to.window(windows[-1])#切换为最新打开的窗口
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,'ewebeditor_auto_iframe_1')))
          WebDriverWait(driver, 20,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'ewebeditor_auto_iframe_1')))
          #driver.switch_to.frame("ewebeditor_auto_iframe_1")
          time.sleep(0.1)
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,"eWebEditor")))
          iframe = driver.find_element_by_xpath("//*[@id='eWebEditor']")
          driver.switch_to.frame(iframe)
          elem = driver.find_element_by_xpath("/html/body")
          elem.send_keys(e[2])
          driver.switch_to.parent_frame()
          driver.switch_to.default_content()
          
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,'ewebeditor_auto_iframe_2')))
          WebDriverWait(driver, 20,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.ID,'ewebeditor_auto_iframe_2')))
          time.sleep(0.1)
          WebDriverWait(driver, 20,0.5).until(EC.presence_of_element_located((By.ID,"eWebEditor")))
          iframe = driver.find_element_by_xpath("//*[@id='eWebEditor']")
          driver.switch_to.frame(iframe)
          elem = driver.find_element_by_xpath("/html/body")
          elem.send_keys(e[9])
          driver.switch_to.parent_frame()
          driver.switch_to.default_content()
          s1 = Select(driver.find_element_by_id("DifficultDegree"))
          s1.select_by_value(str(e[10]))
          elem = driver.find_element_by_id("IncludedAttachment2")
          elem.click()
          elem = driver.find_element_by_id("btn_submit")
          elem.click()
          WebDriverWait(driver, 20,0.5).until(EC.alert_is_present())
          al = driver.switch_to_alert()
          al.accept()
          windows = driver.window_handles
          driver.switch_to.window(windows[-1])#切换为最新打开的窗口
     print("ok")

a1 = input("please input any key to quit")
cur.close()
db.close()
driver.quit()
