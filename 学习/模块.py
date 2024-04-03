"""
自定义模块、系统模块
1 import 模块名
  模块名.变量 模块名.类 模块名.函数
2 from 模块名 import 变量，类，函数
  在代码中直接使用
3 from 模块名 import *
  该模块所有内容
  如果想限制可获取内容，可在模块中加入__all__=[可获取内容]
4 无论 import or from，均会将该模块内容加载（包括函数调用）
   如果不希望调用，在模块中加入if __name__=__main__（在其他模块=__模块名__)
"""
"""
文件夹:非py文件
包：py文件
项目》包》模块》类，函数，变量
包中导入：from包.模块名 import 类，函数，变量
调包默认执行init内函数且默认导入init函数
for 包 import *表示可以使用包内init文件中__all__【】中的模块
"""
from 力扣 import is_robot_bounded

print(is_robot_bounded("GGLLLGG"))
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open(r"D:\PycharmProjects\learning\学习\1234.txt", 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
