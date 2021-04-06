#!/usr/bin/env python
# coding: utf-8
 
# ### "https://www.kw.ac.kr/ko"URL을 열고 "입학"위로 마우스를 가져 가면 "입학"의 색상이 빨간색으로 변하고 5 초 후에 klas 링크를 열고 로그인 ID를 입력하고 2 초 후 학생 ID, 3 초 후 학생 ID 삭제, 5 초 후 현재 창 닫기, 5 초 후 브라우저 닫기 모두 선택

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


# ### 1.컴퓨터에서 브라우저 창을 여는 Chrome 브라우저 개체를 만듭니다.


driver = webdriver.Chrome(executable_path ="C:\Program Files\Python38\ChromeDriver\chromedriver")


driver.get("https://www.kw.ac.kr/ko/")


# ### 호버링 할 요소 배치


element= driver.find_element_by_link_text("입학")


# ### 배치 된 요소에서 마우스 가리 키기 작업 수행("입학")



ActionChains(driver).move_to_element(element).perform()


sleep(5)


# ### Klas 링크로 이동


element2=driver.find_element_by_link_text("KLAS 종합정보서비스")


element2.click()


# ### 현재 페이지 탭 전환



driver.switch_to.window(driver.window_handles[1])


# ### 요소 선택기를 통해 id = loginId를 찾은 후 클릭하여 콘텐츠를 입력합니다.


print (driver.current_url)


sleep(2)


ele=driver.find_element_by_id("loginId")


ele.send_keys("2017203094")



sleep(3)


# ### ID 내용 삭제



ele.send_keys(Keys.CONTROL+'a')



ele.send_keys(Keys.BACK_SPACE)


# ### 현재 창을 닫으려면 5 초 동안 기다리십시오.



sleep(5)



driver.close()


# ### 5 초 후 브라우저 닫기



sleep(5)



driver.quit()

