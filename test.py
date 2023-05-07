from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import getpass
from selenium.webdriver.chrome.options import Options

# --------------------------ADVANCED SETTINGS--------------------------
options = Options()
options.add_argument(f"--user-data-dir=C:/Users/{getpass.getuser()}/AppData/Local/Google/Chrome/User Data/Default")
options.add_argument("--profile-directory=Default")
options.headless = False
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu/')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
options.add_argument('--hide-scrollbars')
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_experimental_option("useAutomationExtension",False)
options.add_experimental_option("debuggerAddress", "localhost:54037")

n = 16
lst = []
driver = webdriver.Chrome(options=options)
time.sleep(2)
driver.get("https://www.iitrpr.ac.in/aims/index.html#/login")
driver.maximize_window()
time.sleep(2)
ide = driver.find_element(By.XPATH,"//*[@id='login']")
ide.send_keys("") #write your entry number here
time.sleep(1)
pas = driver.find_element(By.XPATH,"//*[@id='passwd']")
pas.send_keys("") #write your password here
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='appMain']/div[3]/div/div[1]/div/div[2]/form/div[3]/button[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='navbarCollapse']/ul/li[6]/a").click()
time.sleep(2)

prof = driver.find_element(By.XPATH,"//*[@id='appMain']/div[3]/div/div[2]/div[2]/div[2]")
# prof.select_by_visible_text("Mid-sem")
time.sleep(1)
for i in lst:
    var = Select(driver.find_element(By.XPATH,"//*[@id='fb_type']"))
    var.select_by_visible_text("End-sem") 
    time.sleep(2)
    prof_sel = Select(driver.find_element(By.XPATH,"//*[@id='coe_type']"))
    time.sleep(2)
    prof_sel.select_by_visible_text(i)
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='0_0']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="1_0"]').click() 
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="2_1"]').click()
    driver.execute_script("window.scrollTo(0,700)")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="3_1"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="4_1"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="5_1"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="6_1"]').click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,1500)")
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="7_1"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="8_1"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="9_1"]').click()
    time.sleep(1)
    rit = driver.find_element(By.XPATH,"//*[@id='theform']/div/div[11]/div/div[2]/textarea")
    rit.send_keys("No")
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='theform']/div/div[12]/div[1]/button").click()
    time.sleep(1)
driver.close()


