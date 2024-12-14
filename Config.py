import os
"""
配置文件
"""
# 当前登录用户
CurrentUser = None

# 用户列表
UserList = []

# Cookies字典
CookiesDict = {}

# 实例
Browser = None

# 是否需要登陆，默认读取Cookie登录
login_status = False

# 标题，描述
title = ""
describe = ""

# 图片存放路径
# catalog_image = r"E:\Project\Python\小红书\image"
catalog_image = "D:\小工具\ComfyUI_windows_portable\ComfyUI\output"
# 文件后缀
suffix = ['.jpg', '.jpeg', '.png', '.webp']
## 图片索引大小
files = os.listdir(catalog_image)
image_index = len(files)