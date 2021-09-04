from selenium import webdriver 
from time import sleep
import speech_recognition as sr 

r = sr.Recognizer()

driver = webdriver.Chrome('E:\JAVA\Web Automation\chromedriver')
driver.get("https://www.google.com/maps/@17.6644422,75.8882503,15z")
sleep(7)

s = ""
d = ""
def Record_Voice():
    with sr.Microphone() as source:
        print("Enter station : ")
        audio = r.listen(source)
    
        try:
            txt = r.recognize_google(audio)
            return txt
        except:
            print("Un-recognized voice")

def Search_Place():
    global s
    voice = Record_Voice()
    s = voice
    place = driver.find_element_by_xpath("//*[@id='searchboxinput']")
    place.send_keys(voice)
    Submit = driver.find_element_by_xpath("//*[@id='searchbox-searchbutton']")
    Submit.click()

def Directions():
    sleep(7)
    global d
    direct = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div/button')
    direct.click()
    voice = Record_Voice()
    d = voice
    sleep(2)
    find = driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input')
    find.send_keys(voice)
    tap = driver.find_element_by_xpath('//*[@id="directions-searchbox-0"]/button[1]')
    tap.click()

def Distance():
    sleep(5)
    Tot_Kms = driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[2]/div')
    print("\n",s," <- To -> ", d, " : ", Tot_Kms.text,"s")
    sleep(5)
    Bus = driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[2]/div')
    print("Bus travel time : ", Bus.text, end=" ")
    Hiway_info = driver.find_element_by_xpath('//*[@id="section-directions-trip-title-0"]')
    print(Hiway_info.text)
    Train = driver.find_element_by_xpath('//*[@id="section-directions-trip-1"]/div/div[2]/div[1]/div')
    print("Train Travel time : ", Train.text)


Search_Place()
Directions()
Distance()