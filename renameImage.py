#批量重命名文件夹内图片
import os
import random
path = "D:\小工具\ComfyUI_windows_portable\ComfyUI\output"
files = os.listdir(path)
num = 0
for i in files:
    num = num+1
    newName = f"{num}.png"
    print(f"新文件的名称为 {i} ----->"+newName)
    os.rename(path+'\\'+i,path+'\\'+newName)
