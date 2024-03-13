# 持久化保存：文件
# list 元组 字典 ————>内存
# 用户注册
def register():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    with open(r'users.txt') as stream:
        while True:
            user_information = stream.readline()
            if not user_information:
                print('用户信息输入错误')
                break
            input_user = '{} {}\n'.format(username,password)
            if user_information == input_user:
                print('登陆成功')
                break
register()