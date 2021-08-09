---
layout: page
title: 2021-01-01-icloud-fb-contacts-syncing
permalink: /2021-01-01-icloud-fb-contacts-syncing
---

```python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FacebookCrawler:
    LOGIN_URL = 'https://www.facebook.com/login.php?login_attempt=1&lwv=111'

    def __init__(self, login=None, password=None):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome('./chromedriver')
        self.wait = WebDriverWait(self.driver, 10)
        
        if login:
            self.login(login, password)

    def login(self, login, password):
        self.driver.get(self.LOGIN_URL)

        # wait for the login page to load
        self.wait.until(EC.visibility_of_element_located((By.ID, "email")))

        self.driver.find_element_by_id('email').send_keys(login)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('loginbutton').click()

    def _get_friends_list(self):
        #return self.driver.find_elements_by_css_selector(".friendBrowserNameTitle > a")
        return self.driver.find_elements_by_class_name("_698")

    def get_friends(self):
        # navigate to "friends" page
        self.driver.get("https://www.facebook.com/zach.barnes.9/friends")

        # continuous scroll until no more new friends loaded
        num_of_loaded_friends = len(self._get_friends_list())
        print(self.driver.find_elements_by_class_name("_698"))
        print(self.driver.find_elements_by_class_name("_5qo4"))
        print(self.driver.find_elements_by_css_selector(By.cssSelector("img")))
        
#         while True:
#             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             try:
#                 self.wait.until(lambda driver: len(self._get_friends_list()) > num_of_loaded_friends)
#                 num_of_loaded_friends = len(self._get_friends_list())
#             except TimeoutException:
#                 break  # no more friends loaded

        return [friend.text for friend in self._get_friends_list()]
```

```python
crawler = FacebookCrawler()
crawler.login(login, password)
```

```python
all_imgs = crawler.driver.find_elements_by_css_selector("img")
```

```python
len(all_imgs)
```

```python
friend_list = []
for friend in all_friends:
    if len(friend.find_elements_by_css_selector("img")) == 0:
        continue
    friend_dict = {}
    friend_img = friend.find_elements_by_css_selector("img")[0]
    friend_dict['name'] = friend_img.get_attribute("aria-label")
    friend_dict['url'] = friend.get_attribute("href")
    friend_dict['img'] = friend_img.get_attribute("src")
    friend_list.append(friend_dict)
```

```python
for friend in friend_list:
    friend["clean_url"] = friend["url"].replace("?fref=profile_friend_list&hc_location=friends_tab","")
```

```python
import time
while(len(all_contacts_q) > 0):
    name = all_contacts_q.pop()
    if name in friend_lookup:
        friend = friend_lookup[name]
        crawler.driver.get(friend["clean_url"]+"/about")
        friend["data"] = crawler.driver.find_elements_by_class_name("_4bl7")[2].text
        time.sleep(3)
    else:
        print("not found", name)
```

```python
fb_data[fb_data.data != "nan"]
```

```python
table = driver.find_elements_by_id("sc1361")[0]
for _ in range(310):
    current_contact = table.find_elements_by_class_name("sel")[0]
    driver.find_elements_by_id("sc1750")[0].click()
    
    driver.execute_script("arguments[0].setAttribute('class','atv4 contacts sc1619 sc-view detail-row top bottom sc-static-layout')", driver.find_elements_by_id("sc1923")[0])
    driver.execute_script("arguments[0].setAttribute('class','atv4 contacts sc1619 sc-view detail-row-container')", driver.find_elements_by_id("sc1930")[0])
    driver.execute_script("arguments[0].setAttribute('class','atv4 contacts flat sc1619 sc-view sc-label-view detail-label flat-label label sc-regular-size')", driver.find_elements_by_id("sc1932")[0])
    driver.execute_script("arguments[0].setAttribute('class','atv4 contacts sc1619 sc-view sc-label-view search-label detail-field allow-select sc-hidden label')", driver.find_elements_by_id("sc1937")[0])
    driver.execute_script("arguments[0].setAttribute('class','atv4 contacts sc1619 sc-view sc-text-field-view detail-field text-field me-large-tall-size')", driver.find_elements_by_id("sc3052")[0])
    
    input_element = driver.find_elements_by_name("sc3052")[0]
    ActionChains(driver).move_to_element(input_element).click().perform()
    ActionChains(driver).move_to_element(input_element).click().perform()
    input_element.clear()
    
    try:
        birthday = fb_data[fb_data.name==current_contact.text].birthday.values[0]
        input_element.send_keys(birthday)

    except:
        print(current_contact.text)
        
    driver.find_elements_by_id("sc2025")[0].click()
    current_contact.send_keys(Keys.DOWN)
```

```python
import  urllib
for index,row in fb_data.iterrows():
    path = "imgs/"+str(row["name"]).replace(" ", "_") + ".jpg"
    urllib.urlretrieve(row.img, path)
    fb_data["pic_path"][index] = path
```

```python
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome('./chromedriver')
wait = WebDriverWait(driver, 10)
```

```python
driver.get("https://www.icloud.com/contacts/")
```

```python
frame = driver.find_element_by_id('contacts')
driver.switch_to.frame(frame)
```

```python
table = driver.find_elements_by_id("sc1361")[0]
for _ in range(310):
    current_contact = table.find_elements_by_class_name("sel")[0]
    try:
        pic_path = fb_data[fb_data.name==current_contact.text].pic_path.values[0]
        
        try:
            driver.find_elements_by_id("sc1750")[0].click()
            driver.find_elements_by_id("sc1803")[0].click()
            time.sleep(2)
            file_input = driver.find_elements_by_xpath("//input[@class = 'file-input']")[0]
            file_input.send_keys(os.path.abspath(pic_path))
            time.sleep(2)
            #done = driver.find_elements_by_xpath('//label[contains(text(), "Done")]')[0]
            #done.find_element_by_xpath("./..").click()
#             file_input.send_keys(Keys.RETURN)
#             file_input.submit()

            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        
            time.sleep(3)
            driver.find_elements_by_id("sc2025")[0].click()
            time.sleep(2)
            
        except Exception as e:
            print("Couldnt add")
            print(e)
            break
    
    except:
        print("no img", current_contact.text)
            
    current_contact.send_keys(Keys.DOWN)
```
