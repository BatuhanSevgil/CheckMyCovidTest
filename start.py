from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium import webdriver
import selenium.common.exceptions as exp
from selenium.webdriver.common.keys import Keys
import winsound



# Kullanıcı Tanımları
tc = int(input("TC Kimlik numaranız : "))
password = (input("E-Nabiz Sifreniz : "))
beklenenTest = (int(input("Kaçıncı Test Sonucunuzu beklemektesiniz ? : ")))
 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# Tanımlar

path = "chromedriver.exe"
browser = webdriver.Chrome(path,options=options)
UsernameXpath = """//*[@id="username"]"""
PasswordXpath = """//*[@id="Sifre"]"""
LoginButtonXpath = """//*[@id="btnGiris"]"""
CovidSectionXpath = """//*[@id="ar-SA"]/div[2]/div[3]/div[2]/div/div[1]/div/ul/li[2]/a"""
CovidTableRowXpath = """//*[@id="Covid19TahlilTable"]/tbody/tr"""


MevcutTestSayisi = 0

# UserLogin
browser.get("https://enabiz.gov.tr/")
browser.find_element_by_xpath(UsernameXpath).send_keys(tc)
browser.find_element_by_xpath(PasswordXpath).send_keys(password)
browser.find_element_by_xpath(LoginButtonXpath).click()

# Test Sayfası


while(MevcutTestSayisi != beklenenTest):
    time.sleep(10) 
    browser.get("https://enabiz.gov.tr/HastaBilgileri/Tahliller")
    browser.implicitly_wait(3)
    browser.find_element_by_xpath(CovidSectionXpath).click()
    browser.implicitly_wait(3)
    MevcutTestSayisi = len(browser.find_elements_by_xpath(CovidTableRowXpath))
    print("Mevcut test sayisi ",MevcutTestSayisi)
    print("beklenen ",beklenenTest)

if MevcutTestSayisi == beklenenTest:
    print("Testin Açıklanma Saati : " ,datetime.now())

while(MevcutTestSayisi == beklenenTest):
    winsound.Beep(1000, 100)
