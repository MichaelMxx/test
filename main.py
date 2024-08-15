from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest



class GitHubTest(unittest.TestCase):
    def setUp(self):
        # 使用Chrome浏览器
        self.driver = webdriver.Chrome()

        # 打开GitHub首页
        self.driver.get("https://github.com/")
        time.sleep(2)

    def test_github_flow(self):
        driver = self.driver

        # 点击登录按钮
        login_button = driver.find_element(By.LINK_TEXT, 'Sign in')
        login_button.click()
        time.sleep(1)

        # 输入用户名和密码登录GitHub（替换为你的账号信息）
        driver.find_element(By.ID, 'login_field').send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.NAME, 'commit').click()
        time.sleep(2)

        # 搜索一个仓库
        search_box = driver.find_element(By.CSS_SELECTOR, '[data-query-name="q"]')
        search_box.send_keys('test' + Keys.RETURN)
        time.sleep(2)

        # 点击搜索结果中的第一个仓库
        first_result = driver.find_element(By.XPATH, "//div[@class='width-full d-flex mt-2']/a")
        first_result.click()
        time.sleep(2)

        # 查看仓库的文件，输出文件名
        flies = driver.find_elements(By.XPATH, "//div[@class='react-directory-filename-column']/div/h3/div/a")
        for index, file in enumerate(flies):
            if not file.text.strip():
                continue
            print(f"file : {file.text}")
        print("------------\n")
        time.sleep(2)

        # 查看仓库的issues
        edit = driver.find_element(By.ID, 'issues-tab')
        edit.click()
        time.sleep(2)

        # 返回仓库主页
        driver.back()
        time.sleep(2)

        # 访问用户资料
        usr_inf = driver.find_element(By.XPATH, "//div[@class='AppHeader-context-full']/nav/ul/li/a")
        usr_inf.click()
        time.sleep(2)

        # 查看仓库列表
        rep_tab = driver.find_element(By.ID, "repositories-tab")
        rep_tab.click()
        time.sleep(2)

        # 输出所有仓库名字
        rep_names = driver.find_elements(By.XPATH, "//div[@class='col-10 col-lg-9 d-inline-block']/div/h3/a")
        for index, erp_name in enumerate(rep_names):
            print(f"repository {index + 1}: {erp_name.text}")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
