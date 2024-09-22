import de
import numpy as np # 测试导入第三方包
import importlib
import util.mytools as ts

# 第三方包
a = np.array([1,2,3]) 
print(a)
# 跨文件调用
de.pr() 
ts.tools()
# 动态导入
po = importlib.import_module("util.pt") 
po.pt_p()
# 读取文件
config_list = []
with open("config.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        config_list.append(line)
print(config_list)
p = input('---按任意键结束---')