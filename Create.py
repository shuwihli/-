import os.path
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import Config
import random

def input_content():
    # Config.title = input("请输入标题：")
    # Config.describe = input("请输入描述：")
    Config.title = "AI绘画"       
    Config.describe = "AI绘画"       
    # 等待页面加载完毕 
    Config.Browser.implicitly_wait(5)
    Config.Browser.find_element(By.CSS_SELECTOR, ".c-input_inner > div > input").send_keys(Config.title)
    Config.Browser.find_element(By.CSS_SELECTOR, ".ql-editor").send_keys(Config.describe)


def get_video():
    while True:
        path_mp4 = input("视频路径：")
        path_cover = input("封面路径(不输入使用默认封面)：")
        if not os.path.isfile(path_mp4):
            print("视频不存在！")
        if path_cover == '':
            path_cover = r"D:\小工具\ComfyUI_windows_portable\ComfyUI\output\4.png"
            if not os.path.isfile(path_cover):
                print(f"封面图片不存在{path_cover}")
            else:
                return path_mp4, path_cover
        else:
            return path_mp4


def create_video():
    # print(get_video())
    path_mp4, path_cover = get_video()

    try:
        WebDriverWait(Config.Browser, 10, 0.2).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "div.tab:nth-child(1)")).click()
    except TimeoutException:
        print("网页好像加载失败了！请重试！")

    # 点击上传视频
    Config.Browser.find_element(By.CSS_SELECTOR, ".upload-input").send_keys(path_mp4)
    time.sleep(10)
    # WebDriverWait(Config.Browser, 20).until(
    #     EC.presence_of_element_located((By.XPATH, r'//*[contains(text(),"重新上传")]'))
    # )
    # while True:
    #     time.sleep(3)
    #     try:
    #         Config.Browser.find_element(By.XPATH, r'//*[contains(text(),"重新上传")]')
    #         break
    #     except Exception:
    #         print("视频还在上传中···")

    # if path_cover != "":
    #     Config.Browser.find_element(By.CSS_SELECTOR, "button.css-k3hpu2:nth-child(3)").click()

    #     Config.Browser.find_element(By.XPATH, r'//*[text()="上传封面"]').click()
    #     # 上传封面
    #     Config.Browser.find_element(By.CSS_SELECTOR, "div.upload-wrapper:nth-child(2) > input:nth-child(1)").send_keys(
    #         path_cover)

    #     # 提交封面
    #     WebDriverWait(Config.Browser, 10, 0.2).until(
    #         lambda x: x.find_element(By.CSS_SELECTOR, ".css-8mz9r9 > div:nth-child(1) > button:nth-child(2)")).click()
    # input_content()
    # 发布
    create(".publishBtn")

index = 0
def get_image():
    while True:
        # path_image = input("图片路径：").split(",")
        base_path = "D:\小工具\ComfyUI_windows_portable\ComfyUI\output\\"
        path_image = ""
        for  i in range(0,9):
           image_index = random.randint(1,Config.image_index)
           path_image = base_path+str(image_index)+".png" +","+str(path_image)
        spath_image = path_image[:-1].split(",")    
        print(len(spath_image))
        if 0 < len(spath_image) <= 9:
            for i in spath_image:
                if not os.path.isfile(i):
                    print("图片不存在！")
                    print(i)
                    break
            else:
                return "\n".join(spath_image)
        else:
            print(f"图片最少1张，最多9张{len(spath_image)}")
            continue

def create(create_js):
    print("等待资源上传……")
    time.sleep(10)
    create_js1 = f'return document.querySelector(".publishBtn")'
    Config.Browser.execute_script(create_js1).click()
    print("发布成功！")
    print("等待页面返回！")
    time.sleep(5)
def create_image():
    path_image = get_image()
    # print(path_image)
    WebDriverWait(Config.Browser, 20).until(
        lambda x: x.find_element(By.CSS_SELECTOR, "div.header:nth-child(1) > div:nth-child(2)")).click()
        # 显式等待
    # try:
    #     code_input = 'return document.querySelector("div.header:nth-child(1) > div:nth-child(2)")'
    #     Config.Browser.execute_script(code_input).click()
        
    # except TimeoutException:
    #     print("网页好像加载失败了！请重试！")
    # #  上传图片
    
    Config.Browser.find_element(By.CSS_SELECTOR, ".upload-wrapper > div:nth-child(1) > input:nth-child(1)").send_keys(
        path_image)
    input_content()

    create(".submit > :nth-child(1)")
