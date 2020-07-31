import os
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
url_file = open("Final_list.txt", "r")
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(r'C:\Users\DELL\AppData\Local\Programs\Python\Python37\chromedriver.exe', chrome_options=chrome_options) #manual path
wait = WebDriverWait(driver, 5)
url_list = url_file.read().split(',')
df = pandas.DataFrame()
for url in url_list:
    url = url.replace("'", "")
    driver.get(str(url))
    institute_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblInstituteNameEnglish"]')))
    institute_name = institute_name.text
    region_type = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblRegionType"]')))
    region_type = region_type.text
    address = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblAddressEnglish"]')))
    address = address.text
    pincode = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblPincode"]')))
    pincode = pincode.text
    principal = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblPrincipalNameEnglish"]')))
    principal = principal.text
    office_phone = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblOfficePhoneNo"]')))
    office_phone = office_phone.text
    personal_phone = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblPersonalPhoneNo"]')))
    personal_phone = personal_phone.text
    resedential_phone = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblResidentialPhoneNo"]')))
    resedential_phone = resedential_phone.text
    website = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblWebAddress"]')))
    website = website.text
    email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblEMailAddress"]')))
    email = email.text
    region = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_lblRegion"]')))
    region = region.text
    row_dict = {"institute_name": institute_name, "region_type":region_type, "address":address, "pincode":pincode, "principal":principal, "office_phone":office_phone, "personal_phone":personal_phone, "resedential_phone":resedential_phone, "website":website, "email":email, "region":region}

    df = df.append(row_dict, ignore_index=True)

df.to_csv('scraped_final.csv')